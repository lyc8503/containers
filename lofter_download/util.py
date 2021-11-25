import logging
import re

import html2text


def parse_info(favs_info, fav_str):
    format_fav_info = []

    for fav_info in favs_info:
        blog_info = {}
        # 博客链接
        try:
            url = re.search('s\d{1,5}.blogPageUrl="(.*?)"', fav_info).group(1)
        except:
            logging.error(f"博客{favs_info.index(fav_info)}信息丢失, 跳过")
            continue
        blog_info["url"] = url

        blog_hot = int(re.search('s\d{1,5}.hot=(.*?);', fav_info).group(1))
        blog_info["hot"] = blog_hot

        # 作者名
        author_name_search = re.search('s\d{1,5}.blogNickName="(.*?)"', fav_info)

        if author_name_search:
            author_name = author_name_search.group(1).encode('latin-1').decode('unicode_escape', errors="replace")
        # 正则没有匹配出来的话说明这一页的前面也有这个作者的博客，作者信息在前面，找到id再在前面搜索作者信息
        else:
            info_id = re.search("s\d{1,5}.blogInfo=(s\d{1,5})", fav_info).group(1)
            test_names = re.findall(info_id + '.blogNickName="(.*?)"', fav_str.split('blogPageUrl="' + url + '"')[0])
            author_name = test_names[-1].encode('latin-1').decode('unicode_escape', errors="replace")
        blog_info["author"] = author_name.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")

        # 作者id
        author_id = re.search("http[s]{0,1}://(.*?).lofter.com", url).group(1)
        blog_info["author_id"] = author_id
        # 发表时间
        public_timestamp = re.search('s\d{1,5}.publishTime=(.*?);', fav_info).group(1)
        blog_info["publish_time"] = public_timestamp
        # tags
        tags = re.search('s\d{1,5}.tag[s]{0,1}="(.*?)";', fav_info).group(1).strip().encode('utf-8').decode(
            'unicode_escape', errors="replace").encode("utf-8", errors="ignore").decode("utf-8", errors="ignore").split(",")
        if tags[0] == "":
            tags = []
        lower_tags = []
        for tag in tags:
            # 转小写，全角空格转半角
            lower_tag = tag.lower().replace(" ", " ").strip()
            lower_tags.append(lower_tag)
        blog_info["tags"] = lower_tags
        # 标题
        try:
            title = re.search('s\d{1,5}.title="(.*?)"', fav_info).group(1).encode('latin-1').decode('unicode_escape',
                                                                                                    errors="ignore")
        except Exception as e:
            title = ""
        blog_info["title"] = title.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")

        # 图片链接
        img_urls = []
        urls_search = re.search('originPhotoLinks="(\[.*?\])"', fav_info)
        if urls_search:
            urls_str = urls_search.group(1).replace("\\", "").replace("false", "False").replace("true", "True")
            urls_infos = eval(urls_str)
            for url_info in urls_infos:
                # raw是没有任何后缀的原图，但有的没有raw，取orign
                try:
                    url = url_info["raw"]
                except:
                    url = url_info["orign"].split("?imageView")[0]
                if "netease" in url:
                    url = url_info["orign"].split("?imageView")[0]
                img_urls.append(url)
        blog_info["img"] = img_urls

        # 正文内容
        tmp_content1 = re.search('s\d{1,5}.content="(.*?)";', fav_info).group(1)
        content = html2text.html2text(tmp_content1.encode('latin-1').decode("unicode_escape", errors="ignore"))
        blog_info["content"] = content.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")

        format_fav_info.append(blog_info)

    return format_fav_info


def parse_url(url):
    r = re.match(r"^https://(.*).lofter.com/post/(.*)$", url)
    return r.group(1), r.group(2)
