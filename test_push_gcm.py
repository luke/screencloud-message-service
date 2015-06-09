import urllib2
import json

# project number 832169791377 use in android app
url = 'https://android.googleapis.com/gcm/send'
apiKey = 'AIzaSyCoxAqTTstjSZgi2vH_JihkpCOySqnY30M' # my api key
myKey = "key=" + apiKey
# this is register device id for test
regid = 'd8qq98PfHuY:APA91bHEoSboVx_n0_3mdCSWY2-LR24Wd7hh8qcFWXpHyX43QWkDcISS8DQwalf2pjCMGCI4W-wZLf2RQ5MFcLgMi9nTbRnrqDqvFckuRxdCr1U86L29Lapt847M7xuayWUC7eE_ZZWz'

# make header
headers = {'Content-Type': 'application/json', 'Authorization': myKey}

# make json data
data = {}
data['registration_ids'] = (regid,)
data['data'] = {'data':'hello screen cloud!'}
json_dump = json.dumps(data)
# print json.dumps(data, indent=4)

req = urllib2.Request(url, json_dump, headers)
result = urllib2.urlopen(req).read()
print json.dumps(result)