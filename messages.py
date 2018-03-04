# -*- coding: utf-8 -*-

import io
import requests
from lxml import etree
import json
import random
# import apiai
#
# from api_tokens import *
# APIAI_TOKEN = 'APIAI_TOKEN'

TULING_TOKEN = '7abbe8dddc3243429212fae4e8ecc102'


def tuling_reply(msg_content, user_id):
    url_api = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': TULING_TOKEN,
        'info': msg_content.encode('utf-8'),
        'userid': user_id,
    }
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

    print("use Tuling reply")
    # s = requests.post(url_api, data=data).json()
    s = requests.get(url_api, params=data, headers=headers).json()
    print('return code: ' + str(s['code']))
    if s['code'] == 100000:
        return s['text']
    if s['code'] == 200000:
        return s['text'] + s['url']
    if s['code'] == 302000:
        news = random.choice(s['list'])
        return news['article'] + '\n' + news['detailurl']
    if s['code'] == 308000:
        menu = random.choice(s['list'])
        return menu['name'] + '\n' + menu['detailurl'] + '\n' + menu['info']
    if s['code'] == 40004:
        return '今天好累了，明天再聊吧😄'
    if s['code'] == 40007:
        print('数据格式异常')
        return '数据格式异常😭'


def tulingChat(msg_content, user_id):
    KEY = '8afba6fdc75544f0bebc465615da1e0b'  # change to your API KEY
    url = 'http://www.tuling123.com/openapi/api'
    req_info = msg_content.encode('utf-8')

    query = {'key': KEY, 'info': req_info}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

    try:
        # 方法一、用requests模块已get方式获取内容
        r = requests.get(url, params=query, headers=headers)
        res = r.text
        result = json.loads(res).get('text').replace('<br>', '\n')
    except Exception :
        # result=choice(self.no_answer)
        result = 'unknow error'

    return result


# def apiai_reply(msg_content, user_id):
#     print("try APIAI reply...")
#     ai = apiai.ApiAI(APIAI_TOKEN)
#     request = ai.text_request()
#     request.lang = 'zh-CN'
#     request.session_id = user_id
#     request.query = msg_content
#
#     response = request.getresponse()
#     s = json.loads(response.read().decode('utf-8'))
#
#     if s['result']['action'] == 'input.unknown':
#         raise Exception('api.ai cannot reply this message')
#     if s['status']['code'] == 200:
#         print("use APIAI reply")
#         print('return code: ' + str(s['status']['code']))
#         return s['result']['fulfillment']['speech']


def emotions_reply(keyword):
    print("try gif reply...")
    res = requests.get('https://www.doutula.com/search', {'keyword': keyword})
    html = etree.HTML(res.text)
    urls = html.xpath('//div[@class="image-container"][1]//img[contains(@class, "img-responsive")]/@data-original')
    if len(urls) < 1:
        raise Exception('doutula cannot reply this message')
    url = 'http:' + random.choice(urls)

    return url
