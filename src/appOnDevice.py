#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import postDarkVision as postdv

videofile = "waterfall-free-video1.mp4"

broker = ""
organization = "mf14an"     # 6桁の「組織ID」を指定します
applId = "appOnDevice"
username = "a-mf14an-3byqlkfrgm" #APIキーを指定します。
password = "dN9)kK6zA*D1uo@uy-"  # 英数字18桁の「認証トークン」を指定します

topic = "iot-2/type/camera-device/id/camera-device-001/evt/alert/fmt/json"   # /type/の次にデバイスタイプを指定します。

def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    print("video uploading...")
    notifyURL = postdv.postDarkVision(videofile)
    postdv.postNotification(notifyURL)

clientID = "a:" + organization + ":" + applId
broker = organization + ".messaging.internetofthings.ibmcloud.com"
mqttc = mqtt.Client(clientID)

if username is not "":
    mqttc.username_pw_set(username, password=password)

mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(host=broker, port=1883, keepalive=60)

mqttc.loop_forever()
