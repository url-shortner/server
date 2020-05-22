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
                "category": {"location": tmp.select_one("a > dl > dd.txt-nation.tooltipped.tooltipped-n")["aria-label"]},
                "url": tmp.select_one("a")["href"],
            })
        return result
'''

var nation_code = "";
            var campaign_Category = "0";
            var orderType = "8001";
            var campaign_Type = "1153";
            var searchWord = "";
            var memberID = "2017042823510015";
            var currentPage = $("#hdCurrentPage").val();
            var pageSize = $("#hdPageSize").val();
            var favoriteStatus = $("#hdFavoriteStatus").val();
            var mdStatus = $("#hdMDStatus").val();
            var popularity_Date = $("#hdPopularity_Date").val();
            var strSort_name = "8001";

            $.ajax({
                url: "/Home/CampaignList",
                type: "POST",
                data: { "Nation_Code": nation_code, "Campaign_Category": campaign_Category, "OrderType": orderType, "SearchWord": searchWord, "MemberID": memberID, "CurrentPage": currentPage, "PageSize": pageSize, "CampaignType": campaign_Type, "FavoriteStatus": favoriteStatus, "MDStatus": mdStatus, "Popularity_Date": popularity_Date, "SortName": strSort_name },
                dataType: "html",
                success: function (data) {
                    var liLength = $("#campaign-list>li").length;
                    var divLength = $("#campaign-list>div.list-cont").length;
                    console.log(liLength + " / " + divLength);
                    if (data.indexOf("txt-nodata") != -1) {

                        //데이터가 없을 경우 스크롤 N, 검색어가 있을 경우 [검색 결과가 없습니다. ] 노출
                        //$("#hdScrollYN").val("N");
                        //$("#campaign-list").after("<p class=\"txt-nodata s1\">ALERT_검색된_결과가_없습니다</p>");
                        if (liLength == 0 && divLength == 0) {
                            $("#campaign-list").append(data);
                        }
                        $("#divSpinner").hide();
                    } else {
                        $("#hdScrollYN").val("Y");
                        $("#divSpinner").hide();
                        $("#campaign-list").append(data);
                        totalData = totalData.concat(data);
                    }
'''
