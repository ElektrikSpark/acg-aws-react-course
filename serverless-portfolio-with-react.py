import json
import boto3
import zipfile

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    build_bucket = s3.Bucket('build.portfolio.spark.info')
    portfolio_bucket = s3.Bucket('portfolio.spark.info')

    build_bucket.download_file('buildPortfolio', '/tmp/portfolio.zip')

    with zipfile.ZipFile('/tmp/portfolio.zip') as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm)
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
