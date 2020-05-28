import requests
from bs4 import BeautifulSoup

class Web:

    def connectToWeb(self):
        URL = 'https://www.amazon.com/dp/B082MS1JDP/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B082MS1JDP&pd_rd_w=DXGc1&pf_rd_p=48d372c1-f7e1-4b8b-9d02-4bd86f5158c5&pd_rd_wg=gBj2Y&pf_rd_r=WMBWCAW4QWJXPMR5CHP8&pd_rd_r=c103f93b-8ad6-4092-934c-30a16b896061&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHNDVRMUpWVTkzTDgmZW5jcnlwdGVkSWQ9QTAyMTk1ODdNMElTUjRTOEZYSTImZW5jcnlwdGVkQWRJZD1BMDg4NjgxMjJJQUJWTUlWM0dJT1kmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

        headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        page = requests.get(URL, headers = headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        return soup
