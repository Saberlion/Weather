import urllib.request
import time
#url1 = 'http://m.weather.com.cn/data5/city.xml'
#content1 = urllib.request.urlopen(url1).read()
#print (content1)
#content1 = content1.decode('utf‐8')
#print (content1)
start = time.monotonic() 
rfile = open("provinces.txt",'r')
content1 = rfile.read()
rfile.close()
print (content1)
provinces = content1.split(',')

url = 'http://m.weather.com.cn/data3/city%s.xml'
result = 'city = {\n'
f = open('city.txt', 'w')
f.write(result)
f.close()
for p in provinces:
    i = 0
    result1 =''   
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib.request.urlopen(url2).read()
    content2 = content2.decode('utf‐8')
    cities = content2.split(',')
    for c in cities:
        c_code = c.split('|')[0]
        url3 = url % c_code
        content3 = urllib.request.urlopen(url3).read()
        content3 = content3.decode('utf‐8')
        districts = content3.split(',')
        
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib.request.urlopen(url4).read()
            content4 = content4.decode('utf‐8')
            #print (content4)
            #print (len(content4))
            if (len(content4)>0) and (len(content4) <20):
                code = content4.split('|')[1]
                line = "    '%s': '%s',\n" % (name, code)
            f = open('city.txt', 'a')
            f.write(line)
            f.close()
            print ( name + ':' + code)
            i = i + 1
            if i == 20:
                print ("休眠5秒")
                time.sleep(5)
    usetime = (time.monotonic()  - start)
    print ("用时"+str(usetime))
    print ("休眠20秒")
    time.sleep(20)
#result += '}'
result = '}'
f = open('city.txt', 'a')
f.write(result)
f.close()
print("successed!")
usetime = (time.monotonic()  - start)
print ("用时"+str(usetime))