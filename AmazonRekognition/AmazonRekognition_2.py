from json import JSONDecoder
import boto3

bucket = 'bucketname' # into bucket name
name = 'image/1.png' # into pic path in bucket
attributes = ['ALL']
region = 'region'

rekognition = boto3.client('rekognition', region)
response = rekognition.detect_faces(
    Image = {
        "S3Object": {
            "Bucket": bucket,
            "Name": name,
        }
    },
    Attributes = attributes,
)

print(response)