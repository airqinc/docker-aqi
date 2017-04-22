FROM python:2.7
WORKDIR /app
#ENV IP_BROKER "172.17.0.4"
#ENV IP_MONGO "172.17.0.5"
ADD requeriments.txt ./requeriments.txt
RUN pip install -r ./requeriments.txt
ADD * /app/
ADD app/mqtt_pub.py app/mqtt_pub.py
CMD python app/mqtt_pub.py -b $IP_BROKER #-m $IP_MONGO
