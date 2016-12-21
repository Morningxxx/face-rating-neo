import json
from poster.encode import multipart_encode

import urllib2

def getFaces(fliename):
    datagen, headers = multipart_encode({"api_key": 'Hy9qUZOzFb0ix6JxWG9a_UYm10jjiJRs',
                                         "api_secret": 'L7K3AjMJBbQYnkJCvH7KxLPKhKexvTRL',
                                         "image_file": open(fliename, "rb"),
                                         'return_landmark': 1,
                                         'return_attributes': 'gender,age,smiling,glass,headpose,facequality,blur'
                                         })

    request = urllib2.Request("https://api-cn.faceplusplus.com/facepp/v3/detect", datagen, headers)

    try:
        resp = urllib2.urlopen(request).read()
        token = json.loads(resp)["faces"]
        return token
    except urllib2.HTTPError, e:
        print e.fp.read()
        return None
    except urllib2.URLError, e:
        print e.reason
        return None
