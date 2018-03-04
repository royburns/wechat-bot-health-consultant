# -*- coding: UTF-8 -*-

import re #正则表达式
import time

str = '''{'MsgId': '7933785621170830256', 'FromUserName': '@08becc317763c10eec198e77b477884f', 'ToUserName': '@2cda32fb6c02c4eae87d0ddb9959c9f5438856c5cf917e7fa67e3018b2c9afaf', 'MsgType': 49, 'Content': '<msg> <appmsg appid="" sdkver="0"> \t<title><![CDATA[电商系统风险点]]></title> \t<des><![CDATA[啦啦啦啦啦]]></des> \t<action></action> \t<type>5</type> \t<showtype>1</showtype>     <soundtype>0</soundtype> \t<content><![CDATA[]]></content> \t<contentattr>0</contentattr> \t<url><![CDATA[http://mp.weixin.qq.com/s?__biz=MjM5MjE3NzUyMQ==&mid=100000003&idx=1&sn=1f391a15f4011e8bab88a8fe6c6c6373&chksm=26ab0d1d11dc840b4b1689a2fc1ba425c7db20d6db699e69046fba6744d6bd64d9a04f26f0b2&scene=0&previewkey=YEHKUIfveo90nBrI6dkdI8NS9bJajjJKzz%25252F0By7ITJA%25253D#rd]]></url> \t<lowurl><![CDATA[]]></lowurl> \t<appattach> \t\t<totallen>0</totallen> \t\t<attachid></attachid> \t\t<fileext></fileext> \t\t<cdnthumburl><![CDATA[]]></cdnthumburl> \t\t<cdnthumbaeskey><![CDATA[]]></cdnthumbaeskey> \t\t<aeskey><![CDATA[]]></aeskey> \t</appattach> \t<extinfo></extinfo> \t<sourceusername></sourceusername> \t<sourcedisplayname><![CDATA[]]></sourcedisplayname> \t<mmreader> \t\t<category type="20" count="1"> \t\t\t<name><![CDATA[创业未遂]]></name> \t\t\t<topnew> \t\t\t\t<cover><![CDATA[http://mmbiz.qpic.cn/mmbiz_jpg/yBGia0YD6LEdNpFBWFjMz2CZ9dQLeD9xAzSBMiciacTaiaQibqPqs3oNp3QJia6qYRjj0eOicD8jECnic0MJb2Y4gnBRZw/640?wxtype=jpeg&wxfrom=0]]></cover> \t\t\t\t<width>0</width> \t\t\t\t<height>0</height> \t\t\t\t<digest><![CDATA[]]></digest> \t\t\t</topnew> \t\t\t\t<item> \t<itemshowtype>0</itemshowtype> \t<title><![CDATA[电商系统风险点]]></title> \t<url><![CDATA[http://mp.weixin.qq.com/s?__biz=MjM5MjE3NzUyMQ==&tempkey=OTQ2X2tTU1BFaW5hMk4vb0oxQll6Ymg4eUlsSUJaYjJMZFN5UVloQ1p4aEV0UGxJUVktOWphSVdhbndDRkhCa21yVUdpdkZhQVhpV0NYcUxZY2hDU21GRnNwN0RVTkVyMk05S0xPY2toMVhvMEtyX0FFVzBRcnY0ZjE1UWNwQkN3c0I1dDdTZ1VNVFduQV8zaTJTSW9vVnliRFZxcmlqbVJWdEhPTWctMGd%2Bfg%3D%3D&chksm=26ab0d1d11dc840b4b1689a2fc1ba425c7db20d6db699e69046fba6744d6bd64d9a04f26f0b2&scene=0&previewkey=YEHKUIfveo90nBrI6dkdI8NS9bJajjJKzz%252F0By7ITJA%253D#rd]]></url> \t<shorturl><![CDATA[]]></shorturl> \t<longurl><![CDATA[]]></longurl> \t<pub_time>1520140859</pub_time> \t<cover><![CDATA[http://mmbiz.qpic.cn/mmbiz_jpg/yBGia0YD6LEdNpFBWFjMz2CZ9dQLeD9xAzSBMiciacTaiaQibqPqs3oNp3QJia6qYRjj0eOicD8jECnic0MJb2Y4gnBRZw/640?wxtype=jpeg&wxfrom=0|0|0]]></cover> \t<tweetid></tweetid> \t<digest><![CDATA[啦啦啦啦啦]]></digest> \t<fileid>100000002</fileid> \t<sources> \t<source> \t<name><![CDATA[创业未遂]]></name> \t</source> \t</sources> \t<styles></styles>\t<native_url></native_url>    <del_flag>0</del_flag>     <contentattr>0</contentattr>     <play_length>0</play_length> \t<play_url><![CDATA[]]></play_url> \t<player><![CDATA[]]></player> \t<template_op_type>0</template_op_type> \t<weapp_username><![CDATA[]]></weapp_username> \t<weapp_path><![CDATA[]]></weapp_path> \t<weapp_version>0</weapp_version> \t<weapp_state>0</weapp_state>     <music_source>0</music_source>     <pic_num>0</pic_num> \t<show_complaint_button>0</show_complaint_button> \t</item> \t\t</category> \t\t<publisher> \t\t\t<username></username> \t\t\t<nickname><![CDATA[创业未遂]]></nickname> \t\t</publisher> \t\t<template_header></template_header> \t\t<template_detail></template_detail> \t    <forbid_forward>0</forbid_forward> \t</mmreader> \t<thumburl><![CDATA[http://mmbiz.qpic.cn/mmbiz_jpg/yBGia0YD6LEdNpFBWFjMz2CZ9dQLeD9xAzSBMiciacTaiaQibqPqs3oNp3QJia6qYRjj0eOicD8jECnic0MJb2Y4gnBRZw/640?wxtype=jpeg&wxfrom=0]]></thumburl> \t                               \t </appmsg><fromusername></fromusername><appinfo><version>0</version><appname><![CDATA[创业未遂]]></appname><isforceupdate>1</isforceupdate></appinfo></msg>', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1520140864, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '电商系统风险点', 'FileSize': '0', 'MediaId': '', 'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5MjE3NzUyMQ==&amp;mid=100000003&amp;idx=1&amp;sn=1f391a15f4011e8bab88a8fe6c6c6373&amp;chksm=26ab0d1d11dc840b4b1689a2fc1ba425c7db20d6db699e69046fba6744d6bd64d9a04f26f0b2&amp;scene=0&amp;previewkey=YEHKUIfveo90nBrI6dkdI8NS9bJajjJKzz%25252F0By7ITJA%25253D#rd', 'AppMsgType': 5, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 7933785621170830256, 'OriContent': '', 'EncryFileName': '%E7%94%B5%E5%95%86%E7%B3%BB%E7%BB%9F%E9%A3%8E%E9%99%A9%E7%82%B9', 'Type': 'Sharing', 'Text': '电商系统风险点'}'''

# regx = re.compile('</?\w+[^>]*>')
# title
regx = re.compile('<title><!\[CDATA\[(\w+)\]\]></title>')
result = regx.findall(str)
print(result)

# des
regx = re.compile('<des><!\[CDATA\[(\w+)\]\]></des>')
result = regx.findall(str)
print(result)

# url
regx = re.compile('<url><!\[CDATA\[(\S+)\]\]></url>')
result = regx.findall(str)
print(result)

# name
regx = re.compile('<name><!\[CDATA\[(\w+)\]\]></name>')
result = regx.findall(str)
print(result)

# cover
regx = re.compile('<cover><!\[CDATA\[(\S+)\]\]></cover>')
result = regx.findall(str)
print(result)

# 'CreateTime': 1520140864,
regx = re.compile('\'CreateTime\': (\d+),')
result = regx.findall(str)
print(result)
time_local = time.localtime(int(result[0]))
print(time.strftime('%Y-%m-%d %H:%M:%S', time_local))

result = '1520148209'
print(result)
time_local = time.localtime(int(result))
print(time.strftime('%Y-%m-%d %H:%M:%S', time_local))

# 1520148209
# 1519801769975
result = '1519801769975'
print(result)
time_local = time.localtime(float(result)/1000)
print(time.strftime('%Y-%m-%d %H:%M:%S', time_local))




