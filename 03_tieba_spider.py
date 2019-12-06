import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                                      "AppleWebKit/605.1.15 (KHTML,like Gecko) Version/13.0.3 Safari/605.1.15"
            , "Accept-Language": "zh-cn"}

    def get_url_list(self):
        return [self.url_temp.format(i * 50) for i in range(1000)]

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}--第{}页".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    tieba_spider = TiebaSpider("python")
    tieba_spider.run()
