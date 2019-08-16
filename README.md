# 画像表情認識API調査
  * Google Cloud Vision API
  * Face++

## Google Cloud Vision APIについて(https://cloud.google.com/vision/)
いわずもがなGCPのAPI  
コンソールでAPIを有効にしAPIKeyを取ってきてつかう  
感情認識だけでなく物体検知機能もある  
月1000問い合わせまでは無料  

### 機能
API内にもいくつかの機能に分かれる
#### 物体検知 (LABEL_DETECTION)
画像に写っている物体などを検知し、ラベルとして情報を返す
  * description(ラベルの名称)
  * mid(Google Knowledge Graphなどで使われるラベルのID)
  * score(ラベルの確度)

#### ランドマーク検知 (LANDMARK_DETECTION)
写真に含まれた建造物や地形などから、撮影を行った観光地や名所の検知
  * boundingPoly(対象の画像内での位置)
  * description(ランドマークの名称)
  * location(位置情報)
  * mid(Google Knowledge Graphなどで使われるラベルのID)
  * score(ランドマークの確度)
  
#### 顔認識(FACE_DETECTION)
画像に含まれている人物の顔を検知し、その位置や表情、帽子をかぶっているかなどの情報を返す
  * boundingPoly(検出された顔のおおまかな位置情報)
  * fdBoundingPoly(boundingPolyよりも厳密な範囲での顔の位置情報)
  * landmarks[](顔の特徴点(目や口など)の情報)
  * rollAngle(顔の傾き(ロール角))
  * panAngle(顔の傾き(ヨー角))
  * tiltAngle(顔の傾き(ピッチ角))
  * detectionConfidence(検知された顔の確度)
  * landmarkingConfidence(顔の特徴点についての確度)
  * joyLikelihood(楽しい表情であるか)
  * sorrowLikelihood(悲しい表情であるか)
  * angerLikelihood(怒りの表情であるか)
  * surpriseLikelihood(驚きの表情であるか)
  * underExposedLikelihood(露光不足であるか)
  * blurredLikelihood(ぼやけているか)
  * headwearLikelihood(帽子をかぶっているか)


## Face++について(https://www.faceplusplus.com/)
中国の顔認識API  
開発元企業はメグビィー(Megvii)  
中国では多くの企業でも採用実績があるらしい(アリババ等)  
こちらもコンソールからAPIKeyとAPISecretをとってくる必要あり  
機能制限版が無料で使える(ライセンスがどうなっているかは不明)  
SDKもあるが有料(一年間 4000USD)  

### 機能
画像をAPIに送信し各種パラメータを分析して返答してくれる  
APIのためリアルタイム処理には向いていない  
  * face_rectangle(画像上の顔の範囲)
  * 顔の点を最大106点取得
  * gender(性別)
  * age(年齢)
  * ethnicity(人種)
    - WHITE,BLACK,ASEA,INDIA
  * smile(笑顔度)
  * emotion(感情)
    -  sadness,neutral,disgust,anger,surprise,fear,happiness
  * beauty(美しさ)
    - female_score,male_score
  * skinstatus(肌の状態)
    - dark_circle,stain,acne,health
  * mouthstatus(口の状態)
    -  close,surgical_mask_or_respirator,open,other_occlusion
  * headpose(頭の角度)
    - yaw_angle,pitch_angle,roll_angle
  * facequality
  * eyegaze
  * blur
    - blurness,motionblur,gaussianblur


## 参考
https://qiita.com/LyricalMaestro0/items/e6c418443c1f35770773  
https://dev.classmethod.jp/cloud/gcp/google-cloud-vision-api-get-start/  
http://famirror.hateblo.jp/entry/2015/12/14/180000  

