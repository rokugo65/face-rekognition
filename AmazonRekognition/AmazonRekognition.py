from json import JSONDecoder
import boto3

class FaceParameter:
	def __init__(self,
	_inJson,
	_inWidth,
	_inHeight,
	_inLeft,
	_inTop,
	_inLow,
	_inHigh,
	_inSmile,
	_inEyeglasses,
	_inSunglasses,
	_inGender,
	_inBeard,
	_inMustache,
	_inEyesOpen,
	_inMouthOpen,
	_inCalm,
	_inHappy,
	_inSad):
		self.json = _inJson
		self.w = _inWidth
		self.h = _inHeight
		self.x = _inLeft
		self.y = _inTop
		self.age_low = _inLow
		self.age_high = _inHigh
		self.smile = _inSmile
		self.eyeglasses = _inEyeglasses
		self.sunglasses = _inSunglasses
		self.gender = _inGender
		self.beard = _inBeard
		self.mustache = _inMustache
		self.eyeopen = _inEyesOpen
		self.mouthopen = _inMouthOpen
		self.calm = _inCalm
		self.happy = _inHappy
		self.sad = _inSad

	def print(self):
		#print('json:' + str(self.json))
		print('w:' + str(self.w))
		print('h:' + str(self.h))
		print('x:' + str(self.x))
		print('y:' + str(self.y))
		print('age_low:' + str(self.age_low))
		print('age_high:' + str(self.age_high))
		print('smile:' + str(self.smile))
		print('eyeglasses:' + str(self.eyeglasses))
		print('sunglasses:' + str(self.sunglasses))
		print('gender:' + str(self.gender))
		print('beard:' + str(self.beard))
		print('mustache:' + str(self.mustache))
		print('eyeopen:' + str(self.eyeopen))
		print('mouthopen:' + str(self.mouthopen))
		print('calm:' + str(self.calm))
		print('happy:' + str(self.happy))
		print('sad:' + str(self.sad))

	def getEmotion(self):
		emotion = 'none'
		if self.calm >= self.happy and self.calm >= self.sad:
			emotion = 'calm'
		elif self.happy >= self.calm and self.happy >= self.sad:
			emotion = 'happy'
		elif self.sad >= self.calm and self.sad >= self.happy:
			emotion = 'sad'
		return emotion



def getFaceParameterList(_inImgName):
	bucket = "buketname" #S3に作成したバケット名を入れる
	name = _inImgName #作成したバケットに保存したファイルパスを入れる
	attributes=['ALL']
	region="region"

	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_faces(
	    Image={
			"S3Object": {
				"Bucket": bucket, #S3に作成したバケット名を入れる
				"Name": name, #作成したバケットに保存したファイルパスを入れる
			}
		},
	    Attributes=attributes,
	)

	faceList = []
	#print(response)
	faces_num = len(response['FaceDetails'])
	for i in range(faces_num):
		face = FaceParameter(
		response,
		response['FaceDetails'][i]['BoundingBox']['Width'],
		response['FaceDetails'][i]['BoundingBox']['Height'],
		response['FaceDetails'][i]['BoundingBox']['Left'],
		response['FaceDetails'][i]['BoundingBox']['Top'],
		response['FaceDetails'][i]['AgeRange']['Low'],
		response['FaceDetails'][i]['AgeRange']['High'],
		response['FaceDetails'][i]['Smile']['Value'],
		response['FaceDetails'][i]['Eyeglasses']['Value'],
		response['FaceDetails'][i]['Sunglasses']['Value'],
		response['FaceDetails'][i]['Gender']['Value'],
		response['FaceDetails'][i]['Beard']['Value'],
		response['FaceDetails'][i]['Mustache']['Value'],
		response['FaceDetails'][i]['EyesOpen']['Value'],
		response['FaceDetails'][i]['MouthOpen']['Value'],
		response['FaceDetails'][i]['Emotions'][0]['Confidence'],
		response['FaceDetails'][i]['Emotions'][1]['Confidence'],
		response['FaceDetails'][i]['Emotions'][2]['Confidence'])
		faceList.append(face)
	return faceList

if __name__ == '__main__':
	faceList = getFaceParameterList('1.jpg')
	for face in faceList:
		face.print()

