# -*- coding: utf-8 -*-
from optparse import OptionParser
import paho.mqtt.publish as publish
import requests
# publish.single("topic1", "boo", hostname="172.17.0.3")

if __name__=='__main__':
    parser= OptionParser(usage="%prog -b <broker-IP> -m <mongo-IP>")
    parser.add_option("-b", "--brokerip", action="store", dest="brokerip", metavar="<broker-IP>",default="localhost",
                      help= "IP del broker MQTT al que se conectará este cliente. Por defecto es localhost")

    (opciones, args) = parser.parse_args()
    ip_broker = opciones.brokerip

    #publish.single("topic1", "boo", hostname=ip_broker)

    aqi_token = "ef6bc8b53769124c36402b20a91b104f6677a4c8"                  #TODO: use mongo
    aqi_url = "https://api.waqi.info/feed/madrid/?token=" + aqi_token       #TODO: dynamic?
    aqi_data = {
        # "token": aqi_token,
        # "city": "madrid"
    }

    response = requests.post(aqi_url, data=aqi_data)
    if response.status_code == 200:
        publish.single("sensor_data", response.text, hostname = ip_broker)
    else:
        response.raise_for_status()
#134.168.47.209
