import json
import requests
from hyper.contrib import HTTP20Adapter
# 百度翻译使用http2，也做了反爬虫，目前学习不深，无法调用成功。

class Fanyi:

    def __init__(self, query_string):
        post_data = {
            "query": query_string,
            "from": "zh",
            "to": "en"
        }

        data_string = ''
        for key, value in post_data.items():
            data_string += key + "=" + value.replace("?", "%3F").replace("/", "%2F").replace("%2B", "%252B").replace(
                ":", "%3A") + "&"
        data_string = data_string[0:-1]
        content_length = len(data_string)

        self.url = "https://fanyi.baidu.com/basetrans"
        self.query_string = query_string
        self.headers = {
            ":authority": "fanyi.baidu.com",
            ":method": "POST",
            ":path": "/basetrans",
            ":scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN, zh;q=0.9",
            "content-length": str(content_length),
            "content-type": "application/-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://fanyi.baidu.com/?aldtype=16047",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "core",
            "origin": "https://fanyi.baidu.com",
            "cookie": "BAIDUID=08B0075C023EEF2162704B0CC41B9207:FG=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1575969574; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1575969574; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1575969576; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1575969576"
        }

    def get_post_data(self):
        post_data = {
            "query": self.query_string,
            "from": "zh",
            "to": "en"
        }
        return post_data

    def parse_url(self, url, data):
        s = requests.session()
        s.mount("https://fanyi.baidu.com/", HTTP20Adapter())
        response = s.post(url, data=data, headers=self.headers)
        return response.content.decode()

    def get_ret(self, json_str):
        temp_dict = json.loads(json_str)
        ret = temp_dict["trans"][0]["dst"]
        print("{}的翻译结果是：{}".format(self.query_string, ret))

    def run(self):
        # 1.url post_data
        post_data = self.get_post_data()
        # 2.发送请求
        json_str = self.parse_url(self.url, post_data)
        # 3.提取数据
        self.get_ret(json_str)


if __name__ == "__main__":
    fanyi = Fanyi("好好学习天天向上")
    fanyi.run()
