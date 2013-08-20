import urllib.request

url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib.request.urlopen(url1).read()
content1 = content1.decode('utf‐8')
print (content1)
wfile = open("provinces.txt",'w')
wfile.writelines(content1)
wfile.close()

#rfile = open("provinces.txt",'r')
#provences_text= rfile.readlines()
#rfile.close()
#print (provences_text)