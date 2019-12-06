import requests
tieba_name = input(":")
# 1. 准备url列表
url_temp = "https://tieba.baidu.com/f?kw"+ tieba_name +"&ie=utf-8&pn={}"
url_list = [url_temp.format(i*50) for i in range(1000)]
print(url_list[:3])

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                         "AppleWebKit/605.1.15 (KHTML,like Gecko) Version/13.0.3 Safari/605.1.15"
        , "Accept-Language": "zh-cn"}
for url in url_list:
    resp = requests.get(url, headers=headers)
    file_path = "{}_第{}页.html".format(tieba_name, url_list.index(url)+1)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(resp.content.decode())
