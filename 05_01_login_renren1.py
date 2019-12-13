import requests


url = "http://www.renren.com/736049291/profile"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15",
    "Cookie": "wp_fold=0; jebe_key=886a1bc4-9fef-4d3f-8d56-87b0d9e8722d%7C756818b659178fb9f13242d793d5652e%7C1576119238583%7C1%7C1576119238617; wpsid=15671591298352; loginfrom=null; ver=7.0; _de=DCF60391464BEF547DE1374C26B60001; first_login_flag=1; id=736049291; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; ln_uact=zy30651@qq.com; p=47d8e7db3b392bdba925a7f215fd596d1; societyguester=004354799652a3329c59479029a3bacd1; t=004354799652a3329c59479029a3bacd1; xnsid=7f90c97; _r01_=1; anonymid=k424os9k-i3554p; depovince=GW; ick_login=1ed393b1-3487-48e4-b988-c010e2774424; jebecookies=a494fb7f-f178-49fd-bb60-14e964ce4d55|||||"
}

response = requests.get(url, headers=headers)
print(response.content.decode())