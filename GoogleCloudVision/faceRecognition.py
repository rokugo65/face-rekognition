import os
import re
import csv
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont

import GoogleCloudVision
from GoogleCloudVision import getFaceParameterList

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
imgParameterListHedder.append('joy')
imgParameterListHedder.append('sorrow')
imgParameterListHedder.append('anger')
imgParameterListHedder.append('surprise')
imgParameterListHedder.append('underExposed')
imgParameterListHedder.append('blurred')
imgParameterListHedder.append('headwear')
imgParameterList.append(imgParameterListHedder)

for i in range(1,imgNum+1):
    importImgName = '../img/' + str(i) + '.png'
    im = Image.open(importImgName)
    #im.show()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("C:\Windows\Fonts\meiryob.ttc", 10)

    faceList = getFaceParameterList(importImgName)
    faceNum = len(faceList)
    id = 0
    print(importImgName)
    print('検出された顔の数'+str(faceNum))
    print('--------------------')
    for face in faceList:
        id += 1
        face.print()
        print('--------------------')

        drawStr = 'joy :' + str(face.joy) + '\nsorrow:' + str(face.sorrow) + '\nanger:' + str(face.anger) + '\nsurprise:' + str(face.surprise) + '\nheadwear:' + face.headwear
        x1 = face.x1
        x2 = face.x2
        y1 = face.y1
        y2 = face.y2

        draw.rectangle((x1, y1, x2, y2), outline=(255,0,255))
        draw.rectangle((x1 - 1, y1 - 1, x2 + 1, y2 + 1), outline=(255,0,255))
        draw.rectangle((x1 - 3, y2 + 3, x1 + 149, y2 + 76), outline=(255,128,255), fill=(255,0,255))
        draw.line(((x1 + 4 + 10, y1 + 4), (x1 + 4, y1 + 4), (x1 + 4, y1 + 4 + 10)), fill=(255, 0, 255))
        draw.line(((x2 - 4 - 10, y1 + 4), (x2 - 4, y1 + 4), (x2 - 4, y1 + 4 + 10)), fill=(255, 0, 255))
        draw.line(((x1 + 4 + 10, y2 - 4), (x1 + 4, y2 - 4), (x1 + 4, y2 - 4 - 10)), fill=(255, 0, 255))
        draw.line(((x2 - 4 - 10, y2 - 4), (x2 - 4, y2 - 4), (x2 - 4, y2 - 4 - 10)), fill=(255, 0, 255))
        draw.text((x1, y2 + 2), drawStr, fill=(255, 255, 255), font=font)

    exportImgName = 'export/img/' + str(i) + '.png'
    im.save(exportImgName)

    if faceNum >= 1:
        f = open('export/json/'+ str(i) +'.json', 'w') # 書き込みモードで開く
        f.write(faceList[0].json) # 引数の文字列をファイルに書き込む
        f.close() # ファイルを閉じる
        for face in faceList:
            imgParameterListRow = []
            imgParameterListRow.append(importImgName)
            imgParameterListRow.append(faceNum)
            imgParameterListRow.append('fid' + str(i) + '-' + str(id))
            imgParameterListRow.append(face.joy)
            imgParameterListRow.append(face.sorrow)
            imgParameterListRow.append(face.anger)
            imgParameterListRow.append(face.surprise)
            imgParameterListRow.append(face.underExposed)
            imgParameterListRow.append(face.blurred)
            imgParameterListRow.append(face.headwear)
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