import os
import requests
from json import JSONDecoder

class FaceParameter:
    def __init__(self,
    _inJson,
    _inFaceId,
    _inTop,
    _inLeft,
    _inWidth,
    _inHeight,
    _inSmile,
    _inGender,
    _inAge,
    _inFacialHair_moustache,
    _inFacialHair_beard,
    _inFacialHair_sideburns,
    _inGlasses,
    _inEmotion_anger,
    _inEmotion_contempt,
    _inEmotion_disgust,
    _inEmotion_fear,
    _inEmotion_happiness,
    _inEmotion_neutral,
    _inEmotion_sadness,
    _inEmotion_surprise,
    _inMakeup_eyeMakeup,
    _inMakeup_lipMakeup,
    _inHair_bald,
    _inHair_invisible,
    _inHair_hairColor_black,
    _inHair_hairColor_gray,
    _inHair_hairColor_brown,
    _inHair_hairColor_other,
    _inHair_hairColor_blond,
    _inHair_hairColor_red):
        self.json = _inJson
        self.faceId = _inFaceId
        self.x = _inLeft
        self.y = _inTop
        self.w = _inWidth
        self.h = _inHeight
        self.smile = _inSmile
        self.gender = _inGender
        self.age = _inAge
        self.moustache = _inFacialHair_moustache
        self.beard = _inFacialHair_beard
        self.sideburns = _inFacialHair_sideburns
        self.glesses = _inGlasses
        self.anger = _inEmotion_anger
        self.contempt = _inEmotion_contempt
        self.disgust = _inEmotion_disgust
        self.fear = _inEmotion_fear
        self.happiness = _inEmotion_happiness
        self.neutral = _inEmotion_neutral
        self.sadness = _inEmotion_sadness
        self.surprise = _inEmotion_surprise
        self.eyeMakeup = _inMakeup_eyeMakeup
        self.lipMakeup = _inMakeup_lipMakeup
        self.bald = _inHair_bald
        self.hair_invisible = _inHair_invisible
        self.hairColor_black = _inHair_hairColor_black
        self.hairColor_gray = _inHair_hairColor_gray
        self.hairColor_brown = _inHair_hairColor_brown
        self.hairColor_other = _inHair_hairColor_other
        self.hairColor_blond = _inHair_hairColor_blond
        self.hairColor_red = _inHair_hairColor_red

    def print(self):
        print('faceId:' + str(self.faceId))
        print('x:' + str(self.x))
        print('y:' + str(self.y))
        print('w:' + str(self.w))
        print('h:' + str(self.h))
        print('smile:' + str(self.smile))
        print('gender:' + str(self.gender))
        print('age:' + str(self.age))
        print('moustache:' + str(self.moustache))
        print('bread:' + str(self.beard))
        print('sideburns:' + str(self.sideburns))
        print('glesses:' + str(self.glesses))
        print('anger:' + str(self.anger))
        print('contempt:' + str(self.contempt))
        print('disgust:' + str(self.disgust))
        print('fear:' + str(self.fear))
        print('happiness:' + str(self.happiness))
        print('neutral:' + str(self.neutral))
        print('sadness:' + str(self.sadness))
        print('surprise:' + str(self.surprise))
        print('eyeMakeup:' + str(self.eyeMakeup))
        print('lipMakeup:' + str(self.lipMakeup))
        print('bald:' + str(self.bald))
        print('hair_invisible:' + str(self.hair_invisible))
        print('hairColor_black:' + str(self.hairColor_black))
        print('hairColor_gray:' + str(self.hairColor_gray))
        print('hairColor_brown:' + str(self.hairColor_brown))
        print('hairColor_other:' + str(self.hairColor_other))
        print('hairColor_blond:' + str(self.hairColor_blond))
        print('hairColor_red:' + str(self.hairColor_red))

    def getEmotion(self):
        emotion = 'none'
        if self.happiness >= self.surprise and self.happiness >= self.neutral and self.happiness >= self.fear and self.happiness >= self.sadness and self.happiness >= self.anger and self.happiness >= self.disgust and self.happiness >= self.contempt:
            emotion = 'happiness'
        elif self.surprise >= self.happiness and self.surprise >= self.neutral and self.surprise >= self.fear and self.surprise >= self.sadness and self.surprise >= self.anger and self.surprise >= self.disgust and self.surprise >= self.contempt:
            emotion = 'surprise'
        elif self.neutral >= self.happiness and self.neutral >= self.surprise and self.neutral >= self.fear and self.neutral >= self.sadness and self.neutral >= self.anger and self.neutral >= self.disgust and self.neutral >= self.contempt:
            emotion = 'neutral'
        elif self.fear >= self.happiness and self.fear >= self.surprise and self.fear >= self.neutral and self.fear >= self.sadness and self.fear >= self.anger and self.fear >= self.disgust and self.fear >= self.contempt:
            emotion = 'fear'
        elif self.sadness >= self.happiness and self.sadness >= self.surprise and self.sadness >= self.neutral and self.sadness >= self.fear and self.sadness >= self.anger and self.sadness >= self.disgust and self.sadness >= self.contempt:
            emotion = 'sadness'
        elif self.anger >= self.happiness and self.anger >= self.surprise and self.anger >= self.neutral and self.anger >= self.fear and self.anger >= self.sadness and self.anger >= self.disgust and self.anger >= self.contempt:
            emotion = 'anger'
        elif self.disgust >= self.happiness and self.disgust >= self.surprise and self.disgust >= self.neutral and self.disgust >= self.fear and self.disgust >= self.sadness and self.disgust >= self.anger and self.disgust >= self.contempt:
            emotion = 'disgust'
        elif self.contempt >= self.happiness and self.contempt >= self.surprise and self.contempt >= self.neutral and self.contempt >= self.fear and self.contempt >= self.sadness and self.contempt >= self.anger and self.contempt >= self.disgust:
            emotion = 'contempt'
        return emotion

def getFaceParameterList(_inImgName):
    os.environ["https_proxy"] = "http://username:password@proxy.com:0000"
    subscription_key = "key"
    assert subscription_key
    face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect'
    filename = _inImgName

    headers = {
        #If localfiles
        'Content-Type': 'application/octet-stream',
        #If URL delete 'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }
    data = open(filename,'rb')
    response = requests.post(face_api_url, params=params, headers=headers, data=data)
    req_dict = response.json()
    faces_num = len(req_dict)
    faceList = []
    print(response)
    #print(str(req_dict))
    for i in range(faces_num):
        hairColor_0 = 0.0
        hairColor_1 = 0.0
        hairColor_2 = 0.0
        hairColor_3 = 0.0
        hairColor_4 = 0.0
        hairColor_5 = 0.0
        if not req_dict[i]['faceAttributes']['hair']['invisible']:
            hairColor_0 = req_dict[i]['faceAttributes']['hair']['hairColor'][0]['confidence']
            hairColor_1 = req_dict[i]['faceAttributes']['hair']['hairColor'][1]['confidence']
            hairColor_2 = req_dict[i]['faceAttributes']['hair']['hairColor'][2]['confidence']
            hairColor_3 = req_dict[i]['faceAttributes']['hair']['hairColor'][3]['confidence']
            hairColor_4 = req_dict[i]['faceAttributes']['hair']['hairColor'][4]['confidence']
            hairColor_5 = req_dict[i]['faceAttributes']['hair']['hairColor'][5]['confidence']

        face = FaceParameter(
        req_dict,
        req_dict[i]['faceId'],
        req_dict[i]['faceRectangle']['top'],
        req_dict[i]['faceRectangle']['left'],
        req_dict[i]['faceRectangle']['width'],
        req_dict[i]['faceRectangle']['height'],
        req_dict[i]['faceAttributes']['smile'],
        req_dict[i]['faceAttributes']['gender'],
        req_dict[i]['faceAttributes']['age'],
        req_dict[i]['faceAttributes']['facialHair']['moustache'],
        req_dict[i]['faceAttributes']['facialHair']['beard'],
        req_dict[i]['faceAttributes']['facialHair']['sideburns'],
        req_dict[i]['faceAttributes']['glasses'],
        req_dict[i]['faceAttributes']['emotion']['anger'],
        req_dict[i]['faceAttributes']['emotion']['contempt'],
        req_dict[i]['faceAttributes']['emotion']['disgust'],
        req_dict[i]['faceAttributes']['emotion']['fear'],
        req_dict[i]['faceAttributes']['emotion']['happiness'],
        req_dict[i]['faceAttributes']['emotion']['neutral'],
        req_dict[i]['faceAttributes']['emotion']['sadness'],
        req_dict[i]['faceAttributes']['emotion']['surprise'],
        req_dict[i]['faceAttributes']['makeup']['eyeMakeup'],
        req_dict[i]['faceAttributes']['makeup']['lipMakeup'],
        req_dict[i]['faceAttributes']['hair']['bald'],
        req_dict[i]['faceAttributes']['hair']['invisible'],
        hairColor_0,
        hairColor_1,
        hairColor_2,
        hairColor_3,
        hairColor_4,
        hairColor_5)
        faceList.append(face)
    return faceList