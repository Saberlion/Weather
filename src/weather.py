'''
Created on 2013年7月22日

@author: Arthur
'''
# -*- coding: utf-8 -*-
import urllib.request
import json
from city import city
exit = False
while not exit:
    cityname = input('你想查哪个城市的天气？\n')
    if cityname == 'q':
        exit = True
    else:
        citycode = city.get(cityname)
        if citycode:
            try:
                url = ('http://m.weather.com.cn/data/%s.html' % citycode)
                content = urllib.request.urlopen(url).read()
                content = content.decode('utf-8')
                data = json.loads(content)
                result = data['weatherinfo']
                
                str_temp1 = ('今天天气%s\n气温%s') % (
                result['weather1'],
                result['temp1']
                )
                print (str_temp1)
                
                str_temp2 = ('明天天天气%s\n气温%s') % (
                result['weather2'],
                result['temp2']
                )
                print (str_temp2)
                
                str_temp3 = ('后天天气%s\n气温%s') % (
                result['weather3'],
                result['temp3']
                )
                print (str_temp3)
            except:
                print ('查询失败')
        else:
            print ('没有找到该城市')
