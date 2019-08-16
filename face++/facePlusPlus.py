import requests
from json import JSONDecoder

class FaceParameter:
    def __init__(self,
    _inJson,
    _inFace_token,
    _inGender,
    _inAge,
    _inEthnicity,
    _inSmile,
    _inSadness,
    _inNeutral,
    _inDisgust,
    _inAnger,
    _inSurprise,
    _inFear,
    _inHappiness,
    _inBeauty_f,
    _inBearty_m,
    _inDark_circle,
    _inStain,
    _inAcne,
    _inHealth,
    _inClose,
    _inSurgical_mask_or_respirator,
    _inOpen,
    _inOther_occlusion,
    _inFacequality,
    _inLeft,
    _inTop,
    _inWidth,
    _inHeight):
        self.json = _inJson
        self.token = _inFace_token
        self.gender = _inGender
        self.age = _inAge
        self.ethnicity = _inEthnicity
        self.smile = _inSmile
        self.sadness = _inSadness
        self.neutral = _inNeutral
        self.disgust = _inDisgust
        self.anger = _inAnger
        self.surprise = _inSurprise
        self.fear = _inFear
        self.happiness = _inHappiness
        self.beauty_f = _inBeauty_f
        self.beauty_m = _inBearty_m
        self.dark_circle = _inDark_circle
        self.stain = _inStain
        self.acne = _inAcne
        self.health = _inHealth
        self.close = _inClose
        self.surgical_mask_or_respirator = _inSurgical_mask_or_respirator
        self.open = _inOpen
        self.other_occlusion = _inOther_occlusion
        self.facequality = _inFacequality
        self.x = _inLeft
        self.y = _inTop
        self.w = _inWidth
        self.h = _inHeight

    def print(self):
        print('token:'+self.token)
        print('gender:'+self.gender)
        print('age:'+str(self.age))
        print('ethnicity:'+self.ethnicity)
        print('smile:'+str(self.smile))
        print('emotion:')
        print('  sadness:'+str(self.sadness))
        print('  neutral:'+str(self.neutral))
        print('  disgust:'+str(self.disgust))
        print('  anger:'+str(self.anger))
        print('  surprise:'+str(self.surprise))
        print('  fear:'+str(self.fear))
        print('  happiness:'+str(self.happiness))
        print('beauty:')
        print('  female_score:'+str(self.beauty_f))
        print('  male_score:'+str(self.beauty_m))
        print('skinstatus:')
        print('  dark_circle:'+str(self.dark_circle))
        print('  stain:'+str(self.stain))
        print('  acne:'+str(self.acne))
        print('  health:'+str(self.health))
        print('mouthstatus:')
        print('  close:'+str(self.close))
        print('  surgical_mask_or_respirator:'+str(self.surgical_mask_or_respirator))
        print('  open:'+str(self.open))
        print('  other_occlusion:'+str(self.other_occlusion))
        print('facequality:'+str(self.facequality))
        print('x:'+str(self.x))
        print('y:'+str(self.y))
        print('w:'+str(self.w))
        print('h:'+str(self.h))

    def getEmotion(self):
        emotion = 'none'
        if self.happiness >= self.surprise and self.happiness >= self.neutral and self.happiness >= self.fear and self.happiness >= self.sadness and self.happiness >= self.anger and self.happiness >= self.disgust :
            emotion = 'happiness'
        elif self.surprise >= self.happiness and self.surprise >= self.neutral and self.surprise >= self.fear and self.surprise >= self.sadness and self.surprise >= self.anger and self.surprise >= self.disgust :
            emotion = 'surprise'
        elif self.neutral >= self.happiness and self.neutral >= self.surprise and self.neutral >= self.fear and self.neutral >= self.sadness and self.neutral >= self.anger and self.neutral >= self.disgust :
            emotion = 'neutral'
        elif self.fear >= self.happiness and self.fear >= self.surprise and self.fear >= self.neutral and self.fear >= self.sadness and self.fear >= self.anger and self.fear >= self.disgust :
            emotion = 'fear'
        elif self.sadness >= self.happiness and self.sadness >= self.surprise and self.sadness >= self.neutral and self.sadness >= self.fear and self.sadness >= self.anger and self.sadness >= self.disgust :
            emotion = 'sadness'
        elif self.anger >= self.happiness and self.anger >= self.surprise and self.anger >= self.neutral and self.anger >= self.fear and self.anger >= self.sadness and self.anger >= self.disgust :
            emotion = 'anger'
        elif self.disgust >= self.happiness and self.disgust >= self.surprise and self.disgust >= self.neutral and self.disgust >= self.fear and self.disgust >= self.sadness and self.disgust >= self.anger :
            emotion = 'disgust'
        return emotion


def getFaceParameterList(_inImgName):
    proxies = {
        # プロキシの有効なユーザー名とパスワードを入れる
        'http':'http://username:password@proxy.com:0000',
        'https':'http://username:password@proxy.com:0000'
    }

    url ='https://api-us.faceplusplus.com/facepp/v3/detect'
    # face++のconsoleからそれぞれAPI KeyとAPI Secretをとってくる
    key ='key'
    secret ='secret'

    data = {'api_key': key, 'api_secret': secret, 'return_landmark':'0', 'return_attributes':'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus'}
    filename = _inImgName
    files = {'image_file': open(filename, 'rb')}

    response = requests.post(url, data=data, files=files, proxies=proxies)

    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)

    faceList = []

    print(response)
    print(req_con)
    faces_num = len(req_dict['faces'])
    for i in range(faces_num):
        if len( req_dict['faces'][i]) >= 3:
            face = FaceParameter(
            req_dict,
            req_dict['faces'][i]['face_token'],
            req_dict['faces'][i]['attributes']['gender']['value'],
            req_dict['faces'][i]['attributes']['age']['value'],
            req_dict['faces'][i]['attributes']['ethnicity']['value'],
            req_dict['faces'][i]['attributes']['smile']['value'],
            req_dict['faces'][i]['attributes']['emotion']['sadness'],
            req_dict['faces'][i]['attributes']['emotion']['neutral'],
            req_dict['faces'][i]['attributes']['emotion']['disgust'],
            req_dict['faces'][i]['attributes']['emotion']['anger'],
            req_dict['faces'][i]['attributes']['emotion']['surprise'],
            req_dict['faces'][i]['attributes']['emotion']['fear'],
            req_dict['faces'][i]['attributes']['emotion']['happiness'],
            req_dict['faces'][i]['attributes']['beauty']['female_score'],
            req_dict['faces'][i]['attributes']['beauty']['male_score'],
            req_dict['faces'][i]['attributes']['skinstatus']['dark_circle'],
            req_dict['faces'][i]['attributes']['skinstatus']['stain'],
            req_dict['faces'][i]['attributes']['skinstatus']['acne'],
            req_dict['faces'][i]['attributes']['skinstatus']['health'],
            req_dict['faces'][i]['attributes']['mouthstatus']['close'],
            req_dict['faces'][i]['attributes']['mouthstatus']['surgical_mask_or_respirator'],
            req_dict['faces'][i]['attributes']['mouthstatus']['open'],
            req_dict['faces'][i]['attributes']['mouthstatus']['other_occlusion'],
            req_dict['faces'][i]['attributes']['facequality']['value'],
            req_dict['faces'][i]['face_rectangle']['left'],
            req_dict['faces'][i]['face_rectangle']['top'],
            req_dict['faces'][i]['face_rectangle']['width'],
            req_dict['faces'][i]['face_rectangle']['height'])
            faceList.append(face)

    return faceList

