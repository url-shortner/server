import requests
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup as bs

class Tenping:
    apiUrl = "https://tenping.kr"

    def __init__(self, id, pw):
        self.session = requests.session()
        res = self.session.post(self.apiUrl + '/Member/ActionLogin',
                                {"MemberID": id, "Password": pw, "AutoLogin": "Y"}, verify=False)
        self.headers = {"Cookie": res.headers['Set-Cookie']}

    def get(self, url, params=None):
        return self.session.get(self.apiUrl + url, headers=self.headers, params=params)

    def getInfo(self):
        html = self.get("/Setting/ModifyInfo")
        soup = bs(html.text, "html.parser")
        return {"NickName": soup.select('#content #NickName')[0]["value"],
                "Member_Mobile": soup.select('#content #Member_Mobile')[0]["value"]}

    def getPlayList(self):
        query_parameter = {"Campaign_Category": 0,
                   "CampaignType": 288,
                   "FavoriteStatus": 8702}
        html = self.get("/Home/List", params=query_parameter)
        soup = bs(html.text, "html.parser")
        select_list = soup.select("#campaign-list>li")
        result = list()
        for el in select_list:
            tmp = bs(str(el), "html.parser")
            result.append({
                "title": tmp.select_one(".list-tit").text.strip(),
                "price": tmp.select_one("ul:nth-child(5) > li:nth-child(1)").text.strip(),
                "category": {
                    "location": tmp.select_one("a > dl > dd.txt-nation.tooltipped.tooltipped-n")["aria-label"],
                    "method": tmp.select_one("dl > dd:nth-child(6)").text,
                },
                "url": tmp.select_one("a")["href"],
                "id": parse_qs(urlparse(tmp.select_one("a")["href"]).query)["CampaignID"][0],
            })
        return result
    def getAd(self, id):
        query_parameter = {"CampaignID": id}
        html = self.get("/Home/Send_Campaign_SNS", params=query_parameter)
        soup = bs(html.text, "html.parser")

        return {
            "title": soup.select_one("#contentsboxMessage").text.strip(),
            "imgUrl": soup.select_one("#contentsboxMessage img")["src"],
            "adUrl": soup.select_one("#contentsboxMessage a")["href"],
        }

