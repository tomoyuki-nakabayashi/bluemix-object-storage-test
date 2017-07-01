# -*- coding: utf-8 -*-

import sys
import requests

DARK_VISION_BASE = "https://openwhisk-darkvisionapp-ics.mybluemix.net/"
DARK_VISION_UPLOAD = "upload"
DARK_VISION_VIDEO = "#!/videos/"
BM_NOTIFICATION = "https://iot-platform-ics.mybluemix.net/notification"

def postDarkVision(videofile):
    multipart_form_data = {
        "file": (videofile, open(videofile, 'rb'), "video/mp4"),
        "title": ("", videofile),
        "language_model": ("", "en-US_BroadbandModel")
    }

    upload_url = DARK_VISION_BASE + DARK_VISION_UPLOAD
    r = requests.post(upload_url, files = multipart_form_data)

    print ("URL: " + DARK_VISION_BASE + DARK_VISION_VIDEO + r.json()['id'])
    return DARK_VISION_BASE + DARK_VISION_VIDEO + r.json()['id']

def postNotification(notifyURL):
    headers={'Content-Type': 'application/json'}
    data='{"URL": "%s"}' % (notifyURL)
    r = requests.post(BM_NOTIFICATION, data=data, headers=headers)

    print (r.text)

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print ('Usage: # python %s [video file]' % argv[0])
        quit()

    notifyURL = postDarkVision(argv[1])
    postNotification(notifyURL)
