import requests
import datetime

NBRB_ENDPOINT = "https://www.nbrb.by/api/exrates/rates/"
next_day = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
next_day_bgpb = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')

params = {
    "periodicity": 0,
    "ondate": next_day,
    "parammode": 2,
}

#RUB REQUEST
response = requests.get(url=f"{NBRB_ENDPOINT}RUB", params=params)
RUB_rate = response.json()['Cur_OfficialRate']/100

#USD REQUEST
response = requests.get(url=f"{NBRB_ENDPOINT}USD", params=params)
USD_rate = response.json()['Cur_OfficialRate']

#EUR REQUEST
response = requests.get(url=f"{NBRB_ENDPOINT}EUR", params=params)
EUR_rate = response.json()['Cur_OfficialRate']

#PLN REQUEST
response = requests.get(url=f"{NBRB_ENDPOINT}PLN", params=params)
PLN_rate = response.json()['Cur_OfficialRate']/10

#Make_text

text = f"{next_day_bgpb},810,{RUB_rate}\n" \
       f"{next_day_bgpb},840,{USD_rate}\n" \
       f"{next_day_bgpb},978,{EUR_rate}\n" \
       f"{next_day_bgpb},985,{PLN_rate}"

#Write rates in file

with open("curr_NBRB.txt", mode="w") as file:
    file.write(text)
