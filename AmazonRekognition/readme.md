## アクセスキーの発行
シークレットキーはアクセスキー発行時にしか確認できないので  
シークレットキーを知らない場合は新しくアクセスキーを発行する必要がある(発行にはAdmin権限が必要)  
IAMのページから自分のユーザーを選択  
認証情報タブからアクセスキーの作成を押す  
キーが表示されるのでメモしておく  

## ユーザーamazonrekognitionのポリシー追加
ユーザーのアクセス権限タブでアクセス権限の追加を押す  
既存のポリシーを直接アタッチを押す  
ポリシーのフィルタにAmazonRekognitionを入れて  
表示されたAmazonRekognitionFullAccessにチェックを入れ確認に進み権限を追加する  

## aws-cliセットアップ
コマンドプロンプト起動
aws-cliをインストール

```
pip install awscli
```

aws configureにkeyとかを設定する

```
aws configure
```

```
AWS Access Key:発行したやつ
AWS Secret Access Key:発行したやつ
Default region name:ap-northeast-1
Default output format:json
```

## S３セットアップ
どうやらamazon rekoginitionは  
AWSのストレージにある画像を解析するものらしいので  
S3のセットアップを行う  
Amazon S3のコンソールからバケットを作成  
ここではバケット名をaws-rekognition-ap-northeast-1とする  
s3のregionはAPIのregionと同じにする必要があるのでアジアパシフィック(東京)を選択  
アクセス権限のユーザーを良い感じに追加する  
バケット作成時によく分からない警告が出たりするが無視しても動いた  
バケットが作成されたら作成したバケット名をクリックし  
適当な画像をアップロードするここではphoto.jpgをアップロードした  

## SDKインストール
コード動かすのに必要なので入れておく

```
pip install boto3
```

## テストコード

```
import boto3

def detect_faces(bucket, name, attributes=['ALL'], region="ap-northeast-1"):
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
	return response['FaceDetails']

if __name__ == '__main__':
	BUCKET = "aws-rekognition-ap-northeast-1" #S3に作成したバケット名を入れる
	NAME = "photo.jpg" #作成したバケットに保存したファイルパスを入れる

	for label in detect_faces(BUCKET, NAME):
		print(label)
```

## 実行

```
python test.py
```
