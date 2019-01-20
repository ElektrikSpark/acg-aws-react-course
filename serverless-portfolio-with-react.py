import boto3
import zipfile

s3 = boto3.resource('s3')

build_bucket = s3.Bucket('build.portfolio.spark.info')
portfolio_bucket = s3.Bucket('portfolio.spark.info')

build_bucket.download_file('buildPortfolio.zip', '/tmp/portfolio.zip')

with zipfile.ZipFile('/tmp/portfolio.zip') as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
