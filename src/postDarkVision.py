import requests
multipart_form_data = {    "file": ("videos_s_9", open('videos_s_9.mp4', 'rb'), "video/mp4"),    "title": ("", "videos_s_9.mp4"),    "language_model": ("", "en-US_BroadbandModel")}
multipart_form_data = {    "file": ("agent", open('agent.jpg', 'rb'), "image/jpeg")}
r = requests.post("https://openwhisk-darkvisionapp-ics.mybluemix.net/upload",        files = multipart_form_data    )
print (r.text)print ("URL: " + "https://openwhisk-darkvisionapp-ics.mybluemix.net/#!/videos/" + r.json()['id'])
notifyURL = "https://openwhisk-darkvisionapp-ics.mybluemix.net/#!/videos/" + r.json()['id']headers={'Content-Type': 'application/json'}data='{"URL": %s}' % (notifyURL)
r = requests.post("https://iot-platform-ics.mybluemix.net/notification", data=data, headers=headers)
print (r.text)
