# 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
from pip._vendor.distlib.compat import raw_input


def trans(q,fromL,toL):
    # 百度appid和密钥需要通过注册百度【翻译开放平台】账号后获得
    appid = '20230601001696604'  # 填写你的appid
    secretKey = 'YavLlDTtG5eAluZ3pTQB'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址

    fromLang = fromL  # 原文语种
    toLang = toL  # 译文语种
    salt = random.randint(32768, 65536)
    # 手动录入翻译内容，q存放
    #q = raw_input("please input the word you want to translate:")
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign


# 建立会话，返回结果
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        #print(result['from']+'\n'+result['to']+'\n'+result['trans_result'][0]['src']+'\n'+result['trans_result'][0]['dst'])
        return result['from'], result['to'], result['trans_result'][0]['src'], result['trans_result'][0]['dst']
    finally:
        if httpClient:
            httpClient.close()
