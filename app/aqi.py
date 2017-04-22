# -*- coding: utf-8 -*-

import requests
import json

aqi_token = "ef6bc8b53769124c36402b20a91b104f6677a4c8" #TODO: use mongo
aqi_url = "https://api.waqi.info/feed/madrid/?token=" + aqi_token #TODO: dynamic?
aqi_data = {
    # "token": aqi_token,
    # "city": "madrid"
}

response = requests.post(aqi_url, data=aqi_data)

if response.status_code == 200:
    print(response.status_code, response.text)
else:
    response.raise_for_status()
