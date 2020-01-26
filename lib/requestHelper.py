import urllib3
http = urllib3.PoolManager()

class RequestHelper:
    
    def __init__(self):
        self.__header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "mysessionname=0971v8l2pp0c7opo7ffjq223k1; _ga=GA1.2.571054001.1565702820; __zlcmid=tliSVTIv8Nthfj; language=en; free_access=2; token=327482f52f26b36632b312d347856527; currency=EUR; _gid=GA1.2.1442214568.1579788653; _gat=1",
            "Host": "corner-stats.com",
            "Origin": "https://corner-stats.com",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        }


    def getHeadToHeadData(self, home_team_id, away_team_id):
        with http.Session() as s:
            url = "https://corner-stats.com/index.php?route=module/getmatches/getTeamsAjax&event_type=corners"    

            parameter = 'a:4:{s:8:"table_id";s:22:"table_corners_personal";s:11:"filter_team";s:' + str(len(str(home_team_id))) + ':"' + str(home_team_id) + '";s:15:"filter_opponent";s:' + str(len(str(away_team_id))) + ':"' + str(away_team_id) + '";s:10:"is_filters";i:1;}'

            data = {
            'tour[]': 1,
            'seasons[]': [17, 20, 21, 40],
            'm_type[]': [1, 2],
            'show': 'all',
            'team_id': home_team_id,
            'parameter': parameter,
            'event_type': 'filter',
            'event_value': 0
            }

            req = s.post(url, headers=self.__header, data=data)

            print(req)

            
