import json
import os.path
import datetime
#import conn
import log
from datetime import datetime
import boto3

#def copy(connection):
def copy():
    logger = log.log()
    try:
        #cursor = connection.cursor()
        client = boto3.client('s3')
        response = client.list_objects(
            Bucket='data-funcional-teste',
            Prefix='data/data-sample',
       )
        for x in response["Contents"]:

            sql = """copy funcional.trips from 's3://data-funcional-teste/data/{}' 
                    iam_role 'arn:aws:iam::819120498720:role/RedshiftAccessS3'
                    format as json 'auto'
                    timeformat 'YYYY-MM-DDTHH:MI:SS';""".format(x["Key"])

            #cursor.execute(sql)
            print(sql)
            logger.debug('funcional schema created')
            #connection.commit()
            logger.debug('schema creation commited')
    except:
        logger.error('problem on create schema process')

def lambda_handler(event, context):
    logger = log.log()
    logger.debug('starting')

    copy()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



lambda_handler("a", "b")
