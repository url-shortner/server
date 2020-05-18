import requests
from bs4 import BeautifulSoup as bs

class Tenping:
    def __init__(self, id, pw):
        self.session = requests.session()
        res = self.session.post('https://tenping.kr/Member/ActionLogin',
                                {"MemberID": id, "Password": pw, "AutoLogin": "Y"}, verify=False)
        self.headers = {"Cookie": res.headers['Set-Cookie']}
    def getInfo(self):
        html = self.session.get("https://tenping.kr/Setting/ModifyInfo", headers=self.headers)
        soup = bs(html.text, 'html.parser')
        return {"NickName": soup.select('#content #NickName')[0]["value"],
                "Member_Mobile": soup.select('#content #Member_Mobile')[0]["value"]}



if __name__ == "__main__":
    tenping = Tenping("id", "pw")
    user_profile = tenping.getInfo()
    print(user_profile)

