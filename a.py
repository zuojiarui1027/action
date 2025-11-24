import requests
import os
import sys
print("Hello\n")
def luogu_punch():
    cookie_str="_uid=1961636; __client_id=cf007453e012b6456ff5f1dc6afd720550c17bda; C3VK=525612" # 这行自己改
    url="https://www.luogu.com.cn/index/ajax_punch"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie":cookie_str,
        "Referer":"https://www.luogu.com.cn/",
        "x-requested-with":"XMLHttpRequest" 
    }
    try:
        print("try...")
        response= requests.get(url,headers=headers,timeout=10)
        # print(response)
        try:
            data=response.json()
        except:
            print("JSON fill")
            return
        if response.status_code==200:
            code=data.get('code')
            if code==200:
                print(f"ok:")
            elif code==201:
                print("you are get")
            else:
                print(f"no")
        else:
            print(f"fill")
    except Exception as e:
        print(f"fill")

if __name__=="__main__":
    luogu_punch()
