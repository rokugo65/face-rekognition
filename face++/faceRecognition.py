import os
import re
import csv
import numpy as np
import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont

import facePlusPlus
from facePlusPlus import getFaceParameterList

files = os.listdir('../img/')# ファイルのリストを取得
count = 0# カウンタの初期化
for file in files:# ファイルの数だけループ
    index = re.search('.png', file)# 拡張子がjpgのものを検出
    if index:# jpgの時だけ（今回の場合は）カウンタをカウントアップ
        count = count + 1
 
print('imgNum:'+str(count))# ファイル数の表示

imgNum = count

imgParameterList = []
imgParameterListHedder = []
imgParameterListHedder.append('img_name')
imgParameterListHedder.append('face_num')
imgParameterListHedder.append('ID')
imgParameterListHedder.append('gender')
imgParameterListHedder.append('age')
imgParameterListHedder.append('ethnicity')
imgParameterListHedder.append('smile')
imgParameterListHedder.append('emo_sadness')
imgParameterListHedder.append('emo_neutral')
imgParameterListHedder.append('emo_disgust')
imgParameterListHedder.append('emo_anger')
imgParameterListHedder.append('emo_surprise')
imgParameterListHedder.append('emo_fear')
imgParameterListHedder.append('emo_happiness')
imgParameterListHedder.append('beauty_f')
imgParameterListHedder.append('beauty_m')
imgParameterListHedder.append('facestate_dark_circle')
imgParameterListHedder.append('facestate_stain')
imgParameterListHedder.append('facestate_acne')
imgParameterListHedder.append('facestate_health')

imgParameterList.append(imgParameterListHedder)

for i in range(1,imgNum+1):
    importImgName = '../img/' + str(i) + '.png'
    im = Image.open(importImgName)
    #im.show()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("C:\Windows\Fonts\meiryob.ttc", 10)

    faceList = getFaceParameterList(importImgName)
    faceNum = len(faceList)
    print(importImgName)
    print('検出された顔の数'+str(faceNum))
    print('--------------------')
    for face in faceList:
        face.print()
        drawStr = 'ID :' + str(face.token[0:6]) + '\ngen:' + str(face.gender) + '\nage:' + str(face.age) + '\neth:' + str(face.ethnicity) + '\nemo:' + face.getEmotion()
        x1 = face.x
        x2 = face.x + face.w
        y1 = face.y
        y2 = face.y + face.h
        draw.rectangle((x1, y1, x2, y2), outline=(255,0,255))
        draw.rectangle((x1 - 1, y1 - 1, x2 + 1, y2 + 1), outline=(255,0,255))
        draw.rectangle((x1 - 3, y2 + 3, x1 + 85, y2 + 75), outline=(255,128,255), fill=(255,0,255))
        draw.line(((x1 + 4 + 10, y1 + 4), (x1 + 4, y1 + 4), (x1 + 4, y1 + 4 + 10)), fill=(255, 0, 255))
        draw.line(((x2 - 4 - 10, y1 + 4), (x2 - 4, y1 + 4), (x2 - 4, y1 + 4 + 10)), fill=(255, 0, 255))
        draw.line(((x1 + 4 + 10, y2 - 4), (x1 + 4, y2 - 4), (x1 + 4, y2 - 4 - 10)), fill=(255, 0, 255))
        draw.line(((x2 - 4 - 10, y2 - 4), (x2 - 4, y2 - 4), (x2 - 4, y2 - 4 - 10)), fill=(255, 0, 255))
        draw.text((x1, y2 + 2), drawStr, fill=(255, 255, 255), font=font)
        print('--------------------')
    #im.show()
    exportImgName = 'export/img/' + str(i) + '.png'
    im.save(exportImgName)

    if faceNum >= 1 :
        f = open('export/json/'+ str(i) +'.json', 'w') # 書き込みモードで開く
        json.dump(faceList[0].json, f, indent=4)
        #f.write(faceList[0].json) # 引数の文字列をファイルに書き込む
        f.close() # ファイルを閉じる
        for face in faceList:
            imgParameterListRow = []
            imgParameterListRow.append(importImgName)
            imgParameterListRow.append(faceNum)
            imgParameterListRow.append('fid'+str(face.token[0:6]))
            imgParameterListRow.append(face.gender)
            imgParameterListRow.append(face.age)
            imgParameterListRow.append(face.ethnicity)
            imgParameterListRow.append(face.smile)
            imgParameterListRow.append(face.sadness)
            imgParameterListRow.append(face.neutral)
            imgParameterListRow.append(face.disgust)
            imgParameterListRow.append(face.anger)
            imgParameterListRow.append(face.surprise)
            imgParameterListRow.append(face.fear)
            imgParameterListRow.append(face.happiness)
            imgParameterListRow.append(face.beauty_f)
            imgParameterListRow.append(face.beauty_m)
            imgParameterListRow.append(face.dark_circle)
            imgParameterListRow.append(face.stain)
            imgParameterListRow.append(face.acne)
            imgParameterListRow.append(face.health)
            imgParameterList.append(imgParameterListRow)
    else :
        imgParameterListRow = []
        imgParameterListRow.append(importImgName)
        imgParameterListRow.append(faceNum)
        imgParameterList.append(imgParameterListRow)

np.csvList = []
for row in imgParameterList:
    np.colList = []
    for col in row:
        np.colList.append(col)
    np.csvList.append(row)
f = open('export/csv/result.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(np.csvList)
f.close()