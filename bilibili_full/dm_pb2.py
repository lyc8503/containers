# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08my.proto\x12 bilibili.community.service.dm.v1\"d\n\x06\x41vatar\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x41\n\x0b\x61vatar_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.AvatarType\"#\n\x06\x42ubble\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\xc6\x01\n\x08\x42ubbleV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x41\n\x0b\x62ubble_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.BubbleType\x12\x15\n\rexposure_once\x18\x04 \x01(\x08\x12\x45\n\rexposure_type\x18\x05 \x01(\x0e\x32..bilibili.community.service.dm.v1.ExposureType\"&\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"X\n\x0e\x42uzzwordConfig\x12\x46\n\x08keywords\x18\x01 \x03(\x0b\x32\x34.bilibili.community.service.dm.v1.BuzzwordShowConfig\"x\n\x12\x42uzzwordShowConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x03\x12\x13\n\x0b\x62uzzword_id\x18\x05 \x01(\x03\x12\x13\n\x0bschema_type\x18\x06 \x01(\x05\"{\n\x08\x43heckBox\x12\x0c\n\x04text\x18\x01 \x01(\t\x12<\n\x04type\x18\x02 \x01(\x0e\x32..bilibili.community.service.dm.v1.CheckboxType\x12\x15\n\rdefault_value\x18\x03 \x01(\x08\x12\x0c\n\x04show\x18\x04 \x01(\x08\"?\n\nCheckBoxV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x15\n\rdefault_value\x18\x03 \x01(\x08\"\x82\x02\n\x0b\x43lickButton\x12\x15\n\rportrait_text\x18\x01 \x03(\t\x12\x16\n\x0elandscape_text\x18\x02 \x03(\t\x12\x1b\n\x13portrait_text_focus\x18\x03 \x03(\t\x12\x1c\n\x14landscape_text_focus\x18\x04 \x03(\t\x12\x41\n\x0brender_type\x18\x05 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x0c\n\x04show\x18\x06 \x01(\x08\x12\x38\n\x06\x62ubble\x18\x07 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Bubble\"\xd5\x01\n\rClickButtonV2\x12\x15\n\rportrait_text\x18\x01 \x03(\t\x12\x16\n\x0elandscape_text\x18\x02 \x03(\t\x12\x1b\n\x13portrait_text_focus\x18\x03 \x03(\t\x12\x1c\n\x14landscape_text_focus\x18\x04 \x03(\t\x12\x13\n\x0brender_type\x18\x05 \x01(\x05\x12\x17\n\x0ftext_input_post\x18\x06 \x01(\x08\x12\x15\n\rexposure_once\x18\x07 \x01(\x08\x12\x15\n\rexposure_type\x18\x08 \x01(\x05\"\xa1\x01\n\tCommandDm\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\r\n\x05\x65xtra\x18\t \x01(\t\x12\r\n\x05idStr\x18\n \x01(\t\"P\n\rDanmakuAIFlag\x12?\n\x08\x64m_flags\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuFlag\"\xad\x02\n\x0b\x44\x61nmakuElem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08progress\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x10\n\x08\x66ontsize\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\r\x12\x0f\n\x07midHash\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\x0e\n\x06weight\x18\t \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04pool\x18\x0b \x01(\x05\x12\r\n\x05idStr\x18\x0c \x01(\t\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\x12\x11\n\tanimation\x18\x16 \x01(\t\x12\x42\n\x08\x63olorful\x18\x18 \x01(\x0e\x32\x30.bilibili.community.service.dm.v1.DmColorfulType\")\n\x0b\x44\x61nmakuFlag\x12\x0c\n\x04\x64mid\x18\x01 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\"K\n\x11\x44\x61nmakuFlagConfig\x12\x10\n\x08rec_flag\x18\x01 \x01(\x05\x12\x10\n\x08rec_text\x18\x02 \x01(\t\x12\x12\n\nrec_switch\x18\x03 \x01(\x05\"\xe4\x06\n\x18\x44\x61nmuDefaultPlayerConfig\x12)\n!player_danmaku_use_default_config\x18\x01 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12$\n\x1cinline_player_danmaku_switch\x18\x10 \x01(\x08\x12)\n!player_danmaku_senior_mode_switch\x18\x11 \x01(\x05\x12.\n&player_danmaku_ai_recommended_level_v2\x18\x12 \x01(\x05\x12\x98\x01\n*player_danmaku_ai_recommended_level_v2_map\x18\x13 \x03(\x0b\x32\x64.bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig.PlayerDanmakuAiRecommendedLevelV2MapEntry\x1aK\n)PlayerDanmakuAiRecommendedLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x8f\x08\n\x11\x44\x61nmuPlayerConfig\x12\x1d\n\x15player_danmaku_switch\x18\x01 \x01(\x08\x12\"\n\x1aplayer_danmaku_switch_save\x18\x02 \x01(\x08\x12)\n!player_danmaku_use_default_config\x18\x03 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12&\n\x1eplayer_danmaku_enableblocklist\x18\x10 \x01(\x08\x12$\n\x1cinline_player_danmaku_switch\x18\x11 \x01(\x08\x12$\n\x1cinline_player_danmaku_config\x18\x12 \x01(\x05\x12&\n\x1eplayer_danmaku_ios_switch_save\x18\x13 \x01(\x05\x12)\n!player_danmaku_senior_mode_switch\x18\x14 \x01(\x05\x12.\n&player_danmaku_ai_recommended_level_v2\x18\x15 \x01(\x05\x12\x91\x01\n*player_danmaku_ai_recommended_level_v2_map\x18\x16 \x03(\x0b\x32].bilibili.community.service.dm.v1.DanmuPlayerConfig.PlayerDanmakuAiRecommendedLevelV2MapEntry\x1aK\n)PlayerDanmakuAiRecommendedLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"0\n\x16\x44\x61nmuPlayerConfigPanel\x12\x16\n\x0eselection_text\x18\x01 \x01(\t\"K\n\x18\x44\x61nmuPlayerDynamicConfig\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\"\x90\x03\n\x15\x44\x61nmuPlayerViewConfig\x12\x61\n\x1d\x64\x61nmuku_default_player_config\x18\x01 \x01(\x0b\x32:.bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig\x12R\n\x15\x64\x61nmuku_player_config\x18\x02 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmuPlayerConfig\x12\x61\n\x1d\x64\x61nmuku_player_dynamic_config\x18\x03 \x03(\x0b\x32:.bilibili.community.service.dm.v1.DanmuPlayerDynamicConfig\x12]\n\x1b\x64\x61nmuku_player_config_panel\x18\x04 \x01(\x0b\x32\x38.bilibili.community.service.dm.v1.DanmuPlayerConfigPanel\"\xd8\x04\n\x14\x44\x61nmuWebPlayerConfig\x12\x11\n\tdm_switch\x18\x01 \x01(\x08\x12\x11\n\tai_switch\x18\x02 \x01(\x08\x12\x10\n\x08\x61i_level\x18\x03 \x01(\x05\x12\x10\n\x08\x62locktop\x18\x04 \x01(\x08\x12\x13\n\x0b\x62lockscroll\x18\x05 \x01(\x08\x12\x13\n\x0b\x62lockbottom\x18\x06 \x01(\x08\x12\x12\n\nblockcolor\x18\x07 \x01(\x08\x12\x14\n\x0c\x62lockspecial\x18\x08 \x01(\x08\x12\x14\n\x0cpreventshade\x18\t \x01(\x08\x12\r\n\x05\x64mask\x18\n \x01(\x08\x12\x0f\n\x07opacity\x18\x0b \x01(\x02\x12\x0e\n\x06\x64marea\x18\x0c \x01(\x05\x12\x11\n\tspeedplus\x18\r \x01(\x02\x12\x10\n\x08\x66ontsize\x18\x0e \x01(\x02\x12\x12\n\nscreensync\x18\x0f \x01(\x08\x12\x11\n\tspeedsync\x18\x10 \x01(\x08\x12\x12\n\nfontfamily\x18\x11 \x01(\t\x12\x0c\n\x04\x62old\x18\x12 \x01(\x08\x12\x12\n\nfontborder\x18\x13 \x01(\x05\x12\x11\n\tdraw_type\x18\x14 \x01(\t\x12\x1a\n\x12senior_mode_switch\x18\x15 \x01(\x05\x12\x13\n\x0b\x61i_level_v2\x18\x16 \x01(\x05\x12\x61\n\x0f\x61i_level_v2_map\x18\x17 \x03(\x0b\x32H.bilibili.community.service.dm.v1.DanmuWebPlayerConfig.AiLevelV2MapEntry\x1a\x33\n\x11\x41iLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"Y\n\nDmColorful\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x30.bilibili.community.service.dm.v1.DmColorfulType\x12\x0b\n\x03src\x18\x02 \x01(\t\"A\n\x0f\x44mExpoReportReq\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\r\n\x05spmid\x18\x04 \x01(\t\"\x11\n\x0f\x44mExpoReportRes\"\xe3\x0c\n\x11\x44mPlayerConfigReq\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x45\n\x06switch\x18\x02 \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuSwitch\x12N\n\x0bswitch_save\x18\x03 \x01(\x0b\x32\x39.bilibili.community.service.dm.v1.PlayerDanmakuSwitchSave\x12[\n\x12use_default_config\x18\x04 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuUseDefaultConfig\x12\x61\n\x15\x61i_recommended_switch\x18\x05 \x01(\x0b\x32\x42.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedSwitch\x12_\n\x14\x61i_recommended_level\x18\x06 \x01(\x0b\x32\x41.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevel\x12I\n\x08\x62locktop\x18\x07 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.PlayerDanmakuBlocktop\x12O\n\x0b\x62lockscroll\x18\x08 \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockscroll\x12O\n\x0b\x62lockbottom\x18\t \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockbottom\x12S\n\rblockcolorful\x18\n \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuBlockcolorful\x12O\n\x0b\x62lockrepeat\x18\x0b \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockrepeat\x12Q\n\x0c\x62lockspecial\x18\x0c \x01(\x0b\x32;.bilibili.community.service.dm.v1.PlayerDanmakuBlockspecial\x12G\n\x07opacity\x18\r \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.PlayerDanmakuOpacity\x12S\n\rscalingfactor\x18\x0e \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuScalingfactor\x12\x45\n\x06\x64omain\x18\x0f \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuDomain\x12\x43\n\x05speed\x18\x10 \x01(\x0b\x32\x34.bilibili.community.service.dm.v1.PlayerDanmakuSpeed\x12W\n\x0f\x65nableblocklist\x18\x11 \x01(\x0b\x32>.bilibili.community.service.dm.v1.PlayerDanmakuEnableblocklist\x12^\n\x19inlinePlayerDanmakuSwitch\x18\x12 \x01(\x0b\x32;.bilibili.community.service.dm.v1.InlinePlayerDanmakuSwitch\x12[\n\x12senior_mode_switch\x18\x13 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuSeniorModeSwitch\x12\x64\n\x17\x61i_recommended_level_v2\x18\x14 \x01(\x0b\x32\x43.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevelV2\"/\n\x0b\x44mSegConfig\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"\xe4\x01\n\x10\x44mSegMobileReply\x12<\n\x05\x65lems\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\x12\r\n\x05state\x18\x02 \x01(\x05\x12@\n\x07\x61i_flag\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.DanmakuAIFlag\x12\x41\n\x0b\x63olorfulSrc\x18\x05 \x03(\x0b\x32,.bilibili.community.service.dm.v1.DmColorful\"\xa6\x01\n\x0e\x44mSegMobileReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\x12\x16\n\x0eteenagers_mode\x18\x05 \x01(\x05\x12\n\n\x02ps\x18\x06 \x01(\x03\x12\n\n\x02pe\x18\x07 \x01(\x03\x12\x11\n\tpull_mode\x18\x08 \x01(\x05\x12\x12\n\nfrom_scene\x18\t \x01(\x05\"]\n\rDmSegOttReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegOttReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"]\n\rDmSegSDKReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegSDKReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"\xde\x06\n\x0b\x44mViewReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12\x39\n\x04mask\x18\x02 \x01(\x0b\x32+.bilibili.community.service.dm.v1.VideoMask\x12\x41\n\x08subtitle\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.VideoSubtitle\x12\x13\n\x0bspecial_dms\x18\x04 \x03(\t\x12\x44\n\x07\x61i_flag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12N\n\rplayer_config\x18\x06 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.DanmuPlayerViewConfig\x12\x16\n\x0esend_box_style\x18\x07 \x01(\x05\x12\r\n\x05\x61llow\x18\x08 \x01(\x08\x12\x11\n\tcheck_box\x18\t \x01(\t\x12\x1a\n\x12\x63heck_box_show_msg\x18\n \x01(\t\x12\x18\n\x10text_placeholder\x18\x0b \x01(\t\x12\x19\n\x11input_placeholder\x18\x0c \x01(\t\x12\x1d\n\x15report_filter_content\x18\r \x03(\t\x12\x41\n\x0b\x65xpo_report\x18\x0e \x01(\x0b\x32,.bilibili.community.service.dm.v1.ExpoReport\x12I\n\x0f\x62uzzword_config\x18\x0f \x01(\x0b\x32\x30.bilibili.community.service.dm.v1.BuzzwordConfig\x12\x42\n\x0b\x65xpressions\x18\x10 \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\x12?\n\npost_panel\x18\x11 \x03(\x0b\x32+.bilibili.community.service.dm.v1.PostPanel\x12\x15\n\ractivity_meta\x18\x12 \x03(\t\x12\x42\n\x0bpost_panel2\x18\x13 \x03(\x0b\x32-.bilibili.community.service.dm.v1.PostPanelV2\"X\n\tDmViewReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\r\n\x05spmid\x18\x04 \x01(\t\x12\x14\n\x0cis_hard_boot\x18\x05 \x01(\x05\"\xc4\x04\n\x0e\x44mWebViewReply\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\ttext_side\x18\x03 \x01(\t\x12=\n\x06\x64m_sge\x18\x04 \x01(\x0b\x32-.bilibili.community.service.dm.v1.DmSegConfig\x12\x41\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12\x13\n\x0bspecial_dms\x18\x06 \x03(\t\x12\x11\n\tcheck_box\x18\x07 \x01(\x08\x12\r\n\x05\x63ount\x18\x08 \x01(\x03\x12?\n\ncommandDms\x18\t \x03(\x0b\x32+.bilibili.community.service.dm.v1.CommandDm\x12M\n\rplayer_config\x18\n \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.DanmuWebPlayerConfig\x12\x1d\n\x15report_filter_content\x18\x0b \x03(\t\x12\x42\n\x0b\x65xpressions\x18\x0c \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\x12?\n\npost_panel\x18\r \x03(\x0b\x32+.bilibili.community.service.dm.v1.PostPanel\x12\x15\n\ractivity_meta\x18\x0e \x03(\t\"*\n\nExpoReport\x12\x1c\n\x14should_report_at_end\x18\x01 \x01(\x08\"d\n\nExpression\x12\x0f\n\x07keyword\x18\x01 \x03(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x38\n\x06period\x18\x03 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Period\"I\n\x0b\x45xpressions\x12:\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32,.bilibili.community.service.dm.v1.Expression\"*\n\x19InlinePlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\"\'\n\x05Label\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\"W\n\x07LabelV2\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\x12\x15\n\rexposure_once\x18\x03 \x01(\x08\x12\x15\n\rexposure_type\x18\x04 \x01(\x05\"$\n\x06Period\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"0\n\x1fPlayerDanmakuAiRecommendedLevel\x12\r\n\x05value\x18\x01 \x01(\x08\"2\n!PlayerDanmakuAiRecommendedLevelV2\x12\r\n\x05value\x18\x01 \x01(\x05\"1\n PlayerDanmakuAiRecommendedSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockbottom\x12\r\n\x05value\x18\x01 \x01(\x08\"+\n\x1aPlayerDanmakuBlockcolorful\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockrepeat\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockscroll\x12\r\n\x05value\x18\x01 \x01(\x08\"*\n\x19PlayerDanmakuBlockspecial\x12\r\n\x05value\x18\x01 \x01(\x08\"&\n\x15PlayerDanmakuBlocktop\x12\r\n\x05value\x18\x01 \x01(\x08\"$\n\x13PlayerDanmakuDomain\x12\r\n\x05value\x18\x01 \x01(\x02\"-\n\x1cPlayerDanmakuEnableblocklist\x12\r\n\x05value\x18\x01 \x01(\x08\"%\n\x14PlayerDanmakuOpacity\x12\r\n\x05value\x18\x01 \x01(\x02\"+\n\x1aPlayerDanmakuScalingfactor\x12\r\n\x05value\x18\x01 \x01(\x02\".\n\x1dPlayerDanmakuSeniorModeSwitch\x12\r\n\x05value\x18\x01 \x01(\x05\"#\n\x12PlayerDanmakuSpeed\x12\r\n\x05value\x18\x01 \x01(\x05\"8\n\x13PlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\x12\x12\n\ncan_ignore\x18\x02 \x01(\x08\"(\n\x17PlayerDanmakuSwitchSave\x12\r\n\x05value\x18\x01 \x01(\x08\".\n\x1dPlayerDanmakuUseDefaultConfig\x12\r\n\x05value\x18\x01 \x01(\x08\"\x8c\x03\n\tPostPanel\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x10\n\x08priority\x18\x03 \x01(\x03\x12\x0e\n\x06\x62iz_id\x18\x04 \x01(\x03\x12\x44\n\x08\x62iz_type\x18\x05 \x01(\x0e\x32\x32.bilibili.community.service.dm.v1.PostPanelBizType\x12\x43\n\x0c\x63lick_button\x18\x06 \x01(\x0b\x32-.bilibili.community.service.dm.v1.ClickButton\x12?\n\ntext_input\x18\x07 \x01(\x0b\x32+.bilibili.community.service.dm.v1.TextInput\x12=\n\tcheck_box\x18\x08 \x01(\x0b\x32*.bilibili.community.service.dm.v1.CheckBox\x12\x36\n\x05toast\x18\t \x01(\x0b\x32\'.bilibili.community.service.dm.v1.Toast\"\xcb\x03\n\x0bPostPanelV2\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x10\n\x08\x62iz_type\x18\x03 \x01(\x05\x12\x45\n\x0c\x63lick_button\x18\x04 \x01(\x0b\x32/.bilibili.community.service.dm.v1.ClickButtonV2\x12\x41\n\ntext_input\x18\x05 \x01(\x0b\x32-.bilibili.community.service.dm.v1.TextInputV2\x12?\n\tcheck_box\x18\x06 \x01(\x0b\x32,.bilibili.community.service.dm.v1.CheckBoxV2\x12\x38\n\x05toast\x18\x07 \x01(\x0b\x32).bilibili.community.service.dm.v1.ToastV2\x12:\n\x06\x62ubble\x18\x08 \x01(\x0b\x32*.bilibili.community.service.dm.v1.BubbleV2\x12\x38\n\x05label\x18\t \x01(\x0b\x32).bilibili.community.service.dm.v1.LabelV2\x12\x13\n\x0bpost_status\x18\n \x01(\x05\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xf9\x02\n\x0cSubtitleItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06id_str\x18\x02 \x01(\t\x12\x0b\n\x03lan\x18\x03 \x01(\t\x12\x0f\n\x07lan_doc\x18\x04 \x01(\t\x12\x14\n\x0csubtitle_url\x18\x05 \x01(\t\x12:\n\x06\x61uthor\x18\x06 \x01(\x0b\x32*.bilibili.community.service.dm.v1.UserInfo\x12<\n\x04type\x18\x07 \x01(\x0e\x32..bilibili.community.service.dm.v1.SubtitleType\x12\x15\n\rlan_doc_brief\x18\x08 \x01(\t\x12\x41\n\x07\x61i_type\x18\t \x01(\x0e\x32\x30.bilibili.community.service.dm.v1.SubtitleAiType\x12\x45\n\tai_status\x18\n \x01(\x0e\x32\x32.bilibili.community.service.dm.v1.SubtitleAiStatus\"\xe8\x02\n\tTextInput\x12\x1c\n\x14portrait_placeholder\x18\x01 \x03(\t\x12\x1d\n\x15landscape_placeholder\x18\x02 \x03(\t\x12\x41\n\x0brender_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x18\n\x10placeholder_post\x18\x04 \x01(\x08\x12\x0c\n\x04show\x18\x05 \x01(\x08\x12\x38\n\x06\x61vatar\x18\x06 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Avatar\x12\x41\n\x0bpost_status\x18\x07 \x01(\x0e\x32,.bilibili.community.service.dm.v1.PostStatus\x12\x36\n\x05label\x18\x08 \x01(\x0b\x32\'.bilibili.community.service.dm.v1.Label\"\xfb\x01\n\x0bTextInputV2\x12\x1c\n\x14portrait_placeholder\x18\x01 \x03(\t\x12\x1d\n\x15landscape_placeholder\x18\x02 \x03(\t\x12\x41\n\x0brender_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x18\n\x10placeholder_post\x18\x04 \x01(\x08\x12\x38\n\x06\x61vatar\x18\x05 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Avatar\x12\x18\n\x10text_input_limit\x18\x06 \x01(\x05\"o\n\x05Toast\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\x0c\n\x04show\x18\x03 \x01(\x08\x12\x38\n\x06\x62utton\x18\x04 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Button\"-\n\rToastButtonV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"s\n\x07ToastV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12H\n\x0ftoast_button_v2\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.ToastButtonV2\"\\\n\x08UserInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\x12\x0c\n\x04rank\x18\x06 \x01(\x05\"S\n\tVideoMask\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04plat\x18\x02 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08mask_url\x18\x05 \x01(\t\"o\n\rVideoSubtitle\x12\x0b\n\x03lan\x18\x01 \x01(\t\x12\x0e\n\x06lanDoc\x18\x02 \x01(\t\x12\x41\n\tsubtitles\x18\x03 \x03(\x0b\x32..bilibili.community.service.dm.v1.SubtitleItem*3\n\nAvatarType\x12\x12\n\x0e\x41vatarTypeNone\x10\x00\x12\x11\n\rAvatarTypeNFT\x10\x01*Y\n\nBubbleType\x12\x12\n\x0e\x42ubbleTypeNone\x10\x00\x12\x19\n\x15\x42ubbleTypeClickButton\x10\x01\x12\x1c\n\x18\x42ubbleTypeDmSettingPanel\x10\x02*X\n\x0c\x43heckboxType\x12\x14\n\x10\x43heckboxTypeNone\x10\x00\x12\x19\n\x15\x43heckboxTypeEncourage\x10\x01\x12\x17\n\x13\x43heckboxTypeColorDM\x10\x02*L\n\tDMAttrBit\x12\x14\n\x10\x44MAttrBitProtect\x10\x00\x12\x15\n\x11\x44MAttrBitFromLive\x10\x01\x12\x12\n\x0e\x44MAttrHighLike\x10\x02*5\n\x0e\x44mColorfulType\x12\x0c\n\x08NoneType\x10\x00\x12\x15\n\x0fVipGradualColor\x10\xe1\xd4\x03*<\n\x0c\x45xposureType\x12\x14\n\x10\x45xposureTypeNone\x10\x00\x12\x16\n\x12\x45xposureTypeDMSend\x10\x01*\xc1\x01\n\x10PostPanelBizType\x12\x18\n\x14PostPanelBizTypeNone\x10\x00\x12\x1d\n\x19PostPanelBizTypeEncourage\x10\x01\x12\x1b\n\x17PostPanelBizTypeColorDM\x10\x02\x12\x19\n\x15PostPanelBizTypeNFTDM\x10\x03\x12\x1d\n\x19PostPanelBizTypeFragClose\x10\x04\x12\x1d\n\x19PostPanelBizTypeRecommend\x10\x05*8\n\nPostStatus\x12\x14\n\x10PostStatusNormal\x10\x00\x12\x14\n\x10PostStatusClosed\x10\x01*N\n\nRenderType\x12\x12\n\x0eRenderTypeNone\x10\x00\x12\x14\n\x10RenderTypeSingle\x10\x01\x12\x16\n\x12RenderTypeRotation\x10\x02*6\n\x10SubtitleAiStatus\x12\x08\n\x04None\x10\x00\x12\x0c\n\x08\x45xposure\x10\x01\x12\n\n\x06\x41ssist\x10\x02*+\n\x0eSubtitleAiType\x12\n\n\x06Normal\x10\x00\x12\r\n\tTranslate\x10\x01*\x1e\n\x0cSubtitleType\x12\x06\n\x02\x43\x43\x10\x00\x12\x06\n\x02\x41I\x10\x01*N\n\x11ToastFunctionType\x12\x19\n\x15ToastFunctionTypeNone\x10\x00\x12\x1e\n\x1aToastFunctionTypePostPanel\x10\x01\x32\xa0\x05\n\x02\x44M\x12s\n\x0b\x44mSegMobile\x12\x30.bilibili.community.service.dm.v1.DmSegMobileReq\x1a\x32.bilibili.community.service.dm.v1.DmSegMobileReply\x12\x64\n\x06\x44mView\x12+.bilibili.community.service.dm.v1.DmViewReq\x1a-.bilibili.community.service.dm.v1.DmViewReply\x12q\n\x0e\x44mPlayerConfig\x12\x33.bilibili.community.service.dm.v1.DmPlayerConfigReq\x1a*.bilibili.community.service.dm.v1.Response\x12j\n\x08\x44mSegOtt\x12-.bilibili.community.service.dm.v1.DmSegOttReq\x1a/.bilibili.community.service.dm.v1.DmSegOttReply\x12j\n\x08\x44mSegSDK\x12-.bilibili.community.service.dm.v1.DmSegSDKReq\x1a/.bilibili.community.service.dm.v1.DmSegSDKReply\x12t\n\x0c\x44mExpoReport\x12\x31.bilibili.community.service.dm.v1.DmExpoReportReq\x1a\x31.bilibili.community.service.dm.v1.DmExpoReportResb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._options = None
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_options = b'8\001'
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._options = None
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_options = b'8\001'
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._options = None
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_options = b'8\001'
  _AVATARTYPE._serialized_start=12885
  _AVATARTYPE._serialized_end=12936
  _BUBBLETYPE._serialized_start=12938
  _BUBBLETYPE._serialized_end=13027
  _CHECKBOXTYPE._serialized_start=13029
  _CHECKBOXTYPE._serialized_end=13117
  _DMATTRBIT._serialized_start=13119
  _DMATTRBIT._serialized_end=13195
  _DMCOLORFULTYPE._serialized_start=13197
  _DMCOLORFULTYPE._serialized_end=13250
  _EXPOSURETYPE._serialized_start=13252
  _EXPOSURETYPE._serialized_end=13312
  _POSTPANELBIZTYPE._serialized_start=13315
  _POSTPANELBIZTYPE._serialized_end=13508
  _POSTSTATUS._serialized_start=13510
  _POSTSTATUS._serialized_end=13566
  _RENDERTYPE._serialized_start=13568
  _RENDERTYPE._serialized_end=13646
  _SUBTITLEAISTATUS._serialized_start=13648
  _SUBTITLEAISTATUS._serialized_end=13702
  _SUBTITLEAITYPE._serialized_start=13704
  _SUBTITLEAITYPE._serialized_end=13747
  _SUBTITLETYPE._serialized_start=13749
  _SUBTITLETYPE._serialized_end=13779
  _TOASTFUNCTIONTYPE._serialized_start=13781
  _TOASTFUNCTIONTYPE._serialized_end=13859
  _AVATAR._serialized_start=46
  _AVATAR._serialized_end=146
  _BUBBLE._serialized_start=148
  _BUBBLE._serialized_end=183
  _BUBBLEV2._serialized_start=186
  _BUBBLEV2._serialized_end=384
  _BUTTON._serialized_start=386
  _BUTTON._serialized_end=424
  _BUZZWORDCONFIG._serialized_start=426
  _BUZZWORDCONFIG._serialized_end=514
  _BUZZWORDSHOWCONFIG._serialized_start=516
  _BUZZWORDSHOWCONFIG._serialized_end=636
  _CHECKBOX._serialized_start=638
  _CHECKBOX._serialized_end=761
  _CHECKBOXV2._serialized_start=763
  _CHECKBOXV2._serialized_end=826
  _CLICKBUTTON._serialized_start=829
  _CLICKBUTTON._serialized_end=1087
  _CLICKBUTTONV2._serialized_start=1090
  _CLICKBUTTONV2._serialized_end=1303
  _COMMANDDM._serialized_start=1306
  _COMMANDDM._serialized_end=1467
  _DANMAKUAIFLAG._serialized_start=1469
  _DANMAKUAIFLAG._serialized_end=1549
  _DANMAKUELEM._serialized_start=1552
  _DANMAKUELEM._serialized_end=1853
  _DANMAKUFLAG._serialized_start=1855
  _DANMAKUFLAG._serialized_end=1896
  _DANMAKUFLAGCONFIG._serialized_start=1898
  _DANMAKUFLAGCONFIG._serialized_end=1973
  _DANMUDEFAULTPLAYERCONFIG._serialized_start=1976
  _DANMUDEFAULTPLAYERCONFIG._serialized_end=2844
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_start=2769
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_end=2844
  _DANMUPLAYERCONFIG._serialized_start=2847
  _DANMUPLAYERCONFIG._serialized_end=3886
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_start=2769
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_end=2844
  _DANMUPLAYERCONFIGPANEL._serialized_start=3888
  _DANMUPLAYERCONFIGPANEL._serialized_end=3936
  _DANMUPLAYERDYNAMICCONFIG._serialized_start=3938
  _DANMUPLAYERDYNAMICCONFIG._serialized_end=4013
  _DANMUPLAYERVIEWCONFIG._serialized_start=4016
  _DANMUPLAYERVIEWCONFIG._serialized_end=4416
  _DANMUWEBPLAYERCONFIG._serialized_start=4419
  _DANMUWEBPLAYERCONFIG._serialized_end=5019
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_start=4968
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_end=5019
  _DMCOLORFUL._serialized_start=5021
  _DMCOLORFUL._serialized_end=5110
  _DMEXPOREPORTREQ._serialized_start=5112
  _DMEXPOREPORTREQ._serialized_end=5177
  _DMEXPOREPORTRES._serialized_start=5179
  _DMEXPOREPORTRES._serialized_end=5196
  _DMPLAYERCONFIGREQ._serialized_start=5199
  _DMPLAYERCONFIGREQ._serialized_end=6834
  _DMSEGCONFIG._serialized_start=6836
  _DMSEGCONFIG._serialized_end=6883
  _DMSEGMOBILEREPLY._serialized_start=6886
  _DMSEGMOBILEREPLY._serialized_end=7114
  _DMSEGMOBILEREQ._serialized_start=7117
  _DMSEGMOBILEREQ._serialized_end=7283
  _DMSEGOTTREPLY._serialized_start=7285
  _DMSEGOTTREPLY._serialized_end=7378
  _DMSEGOTTREQ._serialized_start=7380
  _DMSEGOTTREQ._serialized_end=7456
  _DMSEGSDKREPLY._serialized_start=7458
  _DMSEGSDKREPLY._serialized_end=7551
  _DMSEGSDKREQ._serialized_start=7553
  _DMSEGSDKREQ._serialized_end=7629
  _DMVIEWREPLY._serialized_start=7632
  _DMVIEWREPLY._serialized_end=8494
  _DMVIEWREQ._serialized_start=8496
  _DMVIEWREQ._serialized_end=8584
  _DMWEBVIEWREPLY._serialized_start=8587
  _DMWEBVIEWREPLY._serialized_end=9167
  _EXPOREPORT._serialized_start=9169
  _EXPOREPORT._serialized_end=9211
  _EXPRESSION._serialized_start=9213
  _EXPRESSION._serialized_end=9313
  _EXPRESSIONS._serialized_start=9315
  _EXPRESSIONS._serialized_end=9388
  _INLINEPLAYERDANMAKUSWITCH._serialized_start=9390
  _INLINEPLAYERDANMAKUSWITCH._serialized_end=9432
  _LABEL._serialized_start=9434
  _LABEL._serialized_end=9473
  _LABELV2._serialized_start=9475
  _LABELV2._serialized_end=9562
  _PERIOD._serialized_start=9564
  _PERIOD._serialized_end=9600
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_start=9602
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_end=9650
  _PLAYERDANMAKUAIRECOMMENDEDLEVELV2._serialized_start=9652
  _PLAYERDANMAKUAIRECOMMENDEDLEVELV2._serialized_end=9702
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_start=9704
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_end=9753
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_start=9755
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_end=9796
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_start=9798
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_end=9841
  _PLAYERDANMAKUBLOCKREPEAT._serialized_start=9843
  _PLAYERDANMAKUBLOCKREPEAT._serialized_end=9884
  _PLAYERDANMAKUBLOCKSCROLL._serialized_start=9886
  _PLAYERDANMAKUBLOCKSCROLL._serialized_end=9927
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_start=9929
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_end=9971
  _PLAYERDANMAKUBLOCKTOP._serialized_start=9973
  _PLAYERDANMAKUBLOCKTOP._serialized_end=10011
  _PLAYERDANMAKUDOMAIN._serialized_start=10013
  _PLAYERDANMAKUDOMAIN._serialized_end=10049
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_start=10051
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_end=10096
  _PLAYERDANMAKUOPACITY._serialized_start=10098
  _PLAYERDANMAKUOPACITY._serialized_end=10135
  _PLAYERDANMAKUSCALINGFACTOR._serialized_start=10137
  _PLAYERDANMAKUSCALINGFACTOR._serialized_end=10180
  _PLAYERDANMAKUSENIORMODESWITCH._serialized_start=10182
  _PLAYERDANMAKUSENIORMODESWITCH._serialized_end=10228
  _PLAYERDANMAKUSPEED._serialized_start=10230
  _PLAYERDANMAKUSPEED._serialized_end=10265
  _PLAYERDANMAKUSWITCH._serialized_start=10267
  _PLAYERDANMAKUSWITCH._serialized_end=10323
  _PLAYERDANMAKUSWITCHSAVE._serialized_start=10325
  _PLAYERDANMAKUSWITCHSAVE._serialized_end=10365
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_start=10367
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_end=10413
  _POSTPANEL._serialized_start=10416
  _POSTPANEL._serialized_end=10812
  _POSTPANELV2._serialized_start=10815
  _POSTPANELV2._serialized_end=11274
  _RESPONSE._serialized_start=11276
  _RESPONSE._serialized_end=11317
  _SUBTITLEITEM._serialized_start=11320
  _SUBTITLEITEM._serialized_end=11697
  _TEXTINPUT._serialized_start=11700
  _TEXTINPUT._serialized_end=12060
  _TEXTINPUTV2._serialized_start=12063
  _TEXTINPUTV2._serialized_end=12314
  _TOAST._serialized_start=12316
  _TOAST._serialized_end=12427
  _TOASTBUTTONV2._serialized_start=12429
  _TOASTBUTTONV2._serialized_end=12474
  _TOASTV2._serialized_start=12476
  _TOASTV2._serialized_end=12591
  _USERINFO._serialized_start=12593
  _USERINFO._serialized_end=12685
  _VIDEOMASK._serialized_start=12687
  _VIDEOMASK._serialized_end=12770
  _VIDEOSUBTITLE._serialized_start=12772
  _VIDEOSUBTITLE._serialized_end=12883
  _DM._serialized_start=13862
  _DM._serialized_end=14534
# @@protoc_insertion_point(module_scope)
