import json
import os.path
import datetime
import conn
import log
from datetime import datetime
import boto3


def s3list():
    client = boto3.client('s3')
    response = client.list_objects(
        Bucket='data-funcional-teste',
        Prefix='data/data-sample',
    )
    return response


def copy(connection):
    logger = log.log()
    cursor = connection.cursor()
    response = s3list()
    for x in response["Contents"]:
        print(x["Key"])
        sql = """copy funcional.trips from 's3://data-funcional-teste/{}' 
                iam_role 'arn:aws:iam::819120498720:role/RedshiftAccessS3'
                format as json 'auto'
                timeformat 'YYYY-MM-DDTHH:MI:SS';""".format(x["Key"])
        cursor.execute(sql)
        logger.debug('funcional schema created')
        connection.commit()
        logger.debug('schema creation commited')



    sql = """copy funcional.vendor
            from 's3://data-funcional-teste/data/data-vendor_lookup-csv.csv' 
            iam_role 'arn:aws:iam::819120498720:role/RedshiftAccessS3' 
            IGNOREHEADER 1 
            csv;"""
    cursor.execute(sql)
    logger.debug('funcional schema created')
    connection.commit()
    #except:
    #    logger.error('problem on create schema process')

def lambda_handler(event, context):
    logger = log.log()
    logger.debug('starting')
    connection = conn.db_createConnection()
    copy(connection)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



lambda_handler("a", "b")
