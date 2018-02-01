#coding:utf-8
import alpha_modules.get_weather as get_weather
import os,time

weather={}
weather['weatherStatus']=get_weather.get_status()
weather['weatherMax']=get_weather.get_max_temperature()
weather['weatherMin']=get_weather.get_min_temperature()
filename=os.path.join(os.path.dirname(__file__),'index.html')
htmlfile=open(filename,'r',encoding='UTF-8')
htmlcontent=htmlfile.read()
htmlfile.close()
indexDick={}
indexDick['nowTime']=time.strftime('%Y-%m-%d %H:%M:%S')
indexDick.update(weather)
print("Content-type:text/html")
print()
print(htmlcontent.format_map(indexDick))