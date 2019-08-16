from base64 import b64encode
#from sys import argv
import json
from json import JSONDecoder
import requests

class FaceParameter:
    def __init__(self,
    _inJson,
    _inX1,
    _inX2,
    _inY1,
    _inY2,
    _inJoy,
    _inSorrow,
    _inAnger,
    _inSurprise,
    _inUnderExposed,
    _inblurred,
    _inheadwear
    ):
        self.json = _inJson
        self.x1 = _inX1
        self.x2 = _inX2
        self.y1 = _inY1
        self.y2 = _inY2
        self.joy = _inJoy
        self.sorrow = _inSorrow
        self.anger = _inAnger
        self.surprise = _inSurprise
        self.underExposed = _inUnderExposed
        self.blurred = _inblurred
        self.headwear = _inheadwear

    def print(self):
        print('x1:' + str(self.x1))
        print('x2:' + str(self.x2))
        print('y1:' + str(self.y1))
        print('y2:' + str(self.y2))
        print('joy:' + str(self.joy))
        print('sorrow:' + str(self.sorrow))
        print('anger:' + str(self.anger))
        print('surprise:' + str(self.surprise))
        print('underExposed:' + str(self.underExposed))
        print('blurred:' + str(self.blurred))
        print('headwear:' + str(self.headwear))
      

def getFaceParameterList(_inImgName):

    URL = 'https://vision.googleapis.com/v1/images:annotate'
    api_key = 'key'

    img_requests = []
    with open(_inImgName, 'rb') as f:
        ctxt = b64encode(f.read()).decode()
        img_requests.append({
                'image': {'content': ctxt},
                'features': [{
                    'type': 'FACE_DETECTION',
                    'maxResults': 5
                }]
        })

    response = requests.post(URL,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})

    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)

    #print(req_dict)
    faceList = []

    if len(req_dict['responses'][0]) >= 1:
        faces_num = len(req_dict['responses'][0]['faceAnnotations'])
        for i in range(faces_num):
            #print(req_dict['responses'][0]['faceAnnotations'][i])
            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0

            if 'x' in req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][0]:
                x1 = req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][0]['x']
            if 'x' in req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][2]:
                x2 = req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][2]['x']
            if 'y' in req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][0]:
                y1 = req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][0]['y']
            if 'y' in req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][2]:
                y2 = req_dict['responses'][0]['faceAnnotations'][i]['fdBoundingPoly']['vertices'][2]['y']

            face = FaceParameter(
                req_con,
                x1,
                x2,
                y1,
                y2,
                req_dict['responses'][0]['faceAnnotations'][i]['joyLikelihood'],
                req_dict['responses'][0]['faceAnnotations'][i]['sorrowLikelihood'],
                req_dict['responses'][0]['faceAnnotations'][i]['angerLikelihood'],
                req_dict['responses'][0]['faceAnnotations'][i]['surpriseLikelihood'],
                req_dict['responses'][0]['faceAnnotations'][i]['underExposedLikelihood'],
                req_dict['responses'][0]['faceAnnotations'][i]['blurredLikelihood'],
                req_dict['responses'][0]['faceAnnotations'][i]['headwearLikelihood']
            )
            faceList.append(face)

    return faceList