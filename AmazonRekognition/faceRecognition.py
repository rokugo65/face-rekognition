import os
import re
import csv
import numpy as np
import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont

import AmazonRekognition
from AmazonRekognition import getFaceParameterList


files = os.listdir(os.path.join('..', 'img'))
imgNum = 0
for file in files:
    index = re.search('.png', file)
    if index:
        imgNum = imgNum + 1
 
print('imgNum:'+str(imgNum))# ファイル数の表示

imgParameterList = []
imgParameterListHedder = []
imgParameterListHedder.append('img_name')
imgParameterListHedder.append('face_num')
imgParameterListHedder.append('age_low')
imgParameterListHedder.append('age_high')
imgParameterListHedder.append('smile')
imgParameterListHedder.append('eyeglasses')
imgParameterListHedder.append('sunglasses')
imgParameterListHedder.append('gender')
imgParameterListHedder.append('beard')
imgParameterListHedder.append('mustache')
imgParameterListHedder.append('eyeopen')
imgParameterListHedder.append('mouthopen')
imgParameterListHedder.append('calm')
imgParameterListHedder.append('happy')
imgParameterListHedder.append('sad')
imgParameterList.append(imgParameterListHedder)

for i in range(1,imgNum+1):
    imageName = str(i) + '.png'
    importImagePath = os.path.join('..', 'img', imageName)
    im = Image.open(importImagePath)
    draw = ImageDraw.Draw(im)
    fontPath = os.path.join('..', 'font', 'meiryob.ttc')
    font = ImageFont.truetype(fontPath, 10)

    faceList = getFaceParameterList(imageName)
    faceNum = len(faceList)
    print(importImagePath)
    print('検出された顔の数'+str(faceNum))
    print('--------------------')
    for face in faceList:
        face.print()
        x1 = int(im.width * face.x)
        x2 = int(im.width * face.x + im.width * face.w)
        y1 = int(im.height * face.y)
        y2 = int(im.height * face.y + im.height * face.h)
        age = (face.age_high + face.age_low)/2
        drawStr = 'gen:' + str(face.gender) + '\nage:' + str(age) + '\nsmi:' + str(face.smile) + '\nemo:' + face.getEmotion()
        draw.rectangle((x1, y1, x2, y2), outline=(255,0,255))
        draw.rectangle((x1 - 1, y1 - 1, x2 + 1, y2 + 1), outline=(255,0,255))
        draw.rectangle((x1 - 3, y2 + 3, x1 + 65, y2 + 60), outline=(255,128,255), fill=(255,0,255))
        draw.line(((x1 + 4 + 10, y1 + 4), (x1 + 4, y1 + 4), (x1 + 4, y1 + 4 + 10)), fill=(255, 0, 255))
        draw.line(((x2 - 4 - 10, y1 + 4), (x2 - 4, y1 + 4), (x2 - 4, y1 + 4 + 10)), fill=(255, 0, 255))
        draw.line(((x1 + 4 + 10, y2 - 4), (x1 + 4, y2 - 4), (x1 + 4, y2 - 4 - 10)), fill=(255, 0, 255))
        draw.line(((x2 - 4 - 10, y2 - 4), (x2 - 4, y2 - 4), (x2 - 4, y2 - 4 - 10)), fill=(255, 0, 255))
        draw.text((x1, y2 + 2), drawStr, fill=(255, 255, 255), font=font)
        print('--------------------')

    exportImagePath = os.path.join('export', 'img', imageName)
    im.save(exportImagePath)

    if faceNum >= 1 :
        jsonName = str(i) + '.json'
        exportJsonPath = os.path.join('export', 'json', jsonName)
        f = open(exportJsonPath, 'w') # 書き込みモードで開く
        json.dump(faceList[0].json, f, indent=4)
        f.close()
        for face in faceList:
            imgParameterListRow = []
            imgParameterListRow.append(importImagePath)
            imgParameterListRow.append(faceNum)
            imgParameterListRow.append(face.age_low)
            imgParameterListRow.append(face.age_high)
            imgParameterListRow.append(face.smile)
            imgParameterListRow.append(face.eyeglasses)
            imgParameterListRow.append(face.sunglasses)
            imgParameterListRow.append(face.gender)
            imgParameterListRow.append(face.beard)
            imgParameterListRow.append(face.mustache)
            imgParameterListRow.append(face.eyeopen)
            imgParameterListRow.append(face.mouthopen)
            imgParameterListRow.append(face.calm)
            imgParameterListRow.append(face.happy)
            imgParameterListRow.append(face.sad)
            imgParameterList.append(imgParameterListRow)
    else :
        imgParameterListRow = []
        imgParameterListRow.append(importImagePath)
        imgParameterListRow.append(faceNum)
        imgParameterList.append(imgParameterListRow)



np.csvList = []
for row in imgParameterList:
    np.colList = []
    for col in row:
        np.colList.append(col)
    np.csvList.append(row)
f = open(os.path.join('export', 'csv', 'result.csv'), 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(np.csvList)
f.close()
    