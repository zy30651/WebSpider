import requests

# url = "http://img.52z.com/upload/news/image/20180621/20180621055734_59936.jpg"
# response = requests.get(url)

# w 是write , b是可以接受byte类型
# with open("baidu.png", 'wb') as f:
#     f.write(response.content)

# print(response.url)
# print(response.request.url)
# print(response.request.headers)
# print(response.headers)

# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X "
#                          "10_15_1) AppleWebKit/605.1.15 (KHTML, "
#                          "like Gecko) Version/13.0.3 Safari/605.1.15"}
# response = requests.get('http://www.baidu.com', headers=headers)
# print(response.content.decode())

params = {"wd": "ss"}

url = "https://www.baidu.com/s?"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                         "AppleWebKit/605.1.15 (KHTML,like Gecko) Version/13.0.3 Safari/605.1.15"
    , "Accept-Language": "zh-cn"}
response = requests.get(url, params=params, headers=headers)
print(response.status_code)
print(response.url)
print(response.request.url)

# url地址编码-解码

