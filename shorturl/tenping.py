import requests
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
    def playAd_list(self):
        query_parameter = {"Campaign_Category": 0,
                   "CampaignType": 288,
                   "FavoriteStatus": 8702}
        html = self.get("/Home/List", params=query_parameter)
        soup = bs(html.text, "html.parser")
        #select_list = soup.select(html.text, "#campaign-list")
        print(soup)
        # result = []
        # for el in select_list:
        #     result.append({
        #         el.a["href"]
        #     })
        # return result



if __name__ == "__main__":
    tenping = Tenping("id", "pw")
    user_profile = tenping.getInfo()
    print(user_profile)
    pl = tenping.playAd_list()
    print(pl)


