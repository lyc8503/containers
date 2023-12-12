import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType

from fetch import UA
from util import wechat_push_img, wechat_push


def cookie_to_str(cookies_dict):
    login_cookie = ''
    for item in cookies_dict:
        login_cookie += item["name"] + '=' + item['value'] + '; '
    print("Cookie Got: " + login_cookie)
    return login_cookie


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("UA=" + UA)

    # 使用客户端快速登录接口, 需要指定一个代理, 代理将请求传递本地的 QQ 客户端
    if 'CLIENT_PROXY' in os.environ:
        options.add_argument('--proxy-server=socks5://' + os.environ['CLIENT_PROXY'])

    driver = webdriver.Remote(command_executor=os.environ['WEBDRIVER_URL'], options=options)
    return driver


def client_login(username):
    print("尝试代理快速登录...")
    with get_driver() as driver:
        login_timeout = 60
        driver.set_page_load_timeout(login_timeout)
        driver.set_script_timeout(login_timeout)

        driver.get('https://i.qq.com/')
        driver.implicitly_wait(login_timeout)

        try:
            driver.switch_to.frame('login_frame')
        except Exception as e:
            logging.exception('切换到 login_frame 失败: ' + driver.get_screenshot_as_base64())
            raise e

        driver.find_element(By.XPATH, f"//a[@uin='{username}']").click()
        
        for i2 in range(0, 20):
            time.sleep(1)
            if "user.qzone.qq.com" in driver.current_url:
                break
        else:
            wechat_push("代理快速登录失败!")
            wechat_push_img(driver.get_screenshot_as_base64())
            raise Exception("代理快速登录失败!")

        return cookie_to_str(driver.get_cookies())



def password_login(username, password):
    print("尝试账号密码登录...")
    with get_driver() as driver:
        # 登录
        login_timeout = 60

        driver.set_page_load_timeout(login_timeout)
        driver.set_script_timeout(login_timeout)

        driver.get('https://i.qq.com/')
        driver.implicitly_wait(login_timeout)

        try:
            driver.switch_to.frame('login_frame')
        except Exception as e:
            wechat_push("切换到 login_frame 失败: " + str(e))
            wechat_push_img(driver.get_screenshot_as_base64())

        driver.find_element(By.ID, 'switcher_plogin').click()
        driver.find_element(By.ID, 'u').clear()
        driver.find_element(By.ID, 'u').send_keys(username)
        driver.find_element(By.ID, 'p').clear()
        driver.find_element(By.ID, 'p').send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID, 'login_button').click()
        time.sleep(5)

        for i2 in range(0, 20):
            time.sleep(1)
            if "user.qzone.qq.com" in driver.current_url:
                break
        else:
            wechat_push("登录失败! 凭据错误/触发风控")
            wechat_push_img(driver.get_screenshot_as_base64())
            raise Exception("登录失败! 凭据错误/触发风控")

        return cookie_to_str(driver.get_cookies())


def qr_login():
    with get_driver() as driver:
        # 登录
        login_timeout = 60

        driver.set_page_load_timeout(login_timeout)
        driver.set_script_timeout(login_timeout)
        driver.get('https://i.qq.com/')
        driver.implicitly_wait(login_timeout)

        driver.switch_to.frame('login_frame')
        time.sleep(3)
        b64 = driver.find_element(By.ID, "qrlogin_img").screenshot_as_base64
        print("二维码: " + b64)
        wechat_push_img(b64)

        for i2 in range(0, 120):
            time.sleep(1)
            if "user.qzone.qq.com" in driver.current_url:
                break
        else:
            wechat_push_img(driver.get_screenshot_as_base64())
            raise Exception("登录失败! 二维码登录超时!")

        global last_cookie
        last_cookie = driver.get_cookies()

        return cookie_to_str(driver.get_cookies())
