import pymysql.cursors
import datetime
import log
import psycopg2
import os
import json
import boto3


def db_createConnection():
    logger = log.log()
    #try:
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='RedshiftSecret')
    response = json.loads(response["SecretString"])                  
    #if os.environ['DB_HOST'] == "":
    if "DB_HOST" in os.environ:
        DB_HOST = os.environ['HOME']
    else:
        DB_HOST = "funcionalcf-redshiftcluster-hg42toiuq7v2.cym24i1ilzer.us-east-1.redshift.amazonaws.com"
        
    DB_NAME='dev'
    DB_PORT='5439'
    DB_USER= response["username"]
    DB_PWD= response["password"]
    conn_string = "dbname='{}' port='{}' host='{}' user='{}' password='{}'".format(DB_NAME, DB_PORT, DB_HOST, DB_USER, DB_PWD)
    connection = psycopg2.connect(conn_string)
    logger.debug('connection created')
    #except:
     #   logger.error('problem on connection')

    db_createSchema(connection)
    db_createTables(connection)
    return connection

def db_createTables(connection):
    logger = log.log()
    try:
        logger.debug('creating tables')
        cursor = connection.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS funcional.trips(
            cod INT IDENTITY(1,1),
            vendor_id VARCHAR(5),
            pickup_datetime TIMESTAMPTZ,
            dropoff_datetime TIMESTAMPTZ,
            passenger_count INT,
            trip_distance NUMERIC(5, 2),
            pickup_longitude NUMERIC(9, 6),
            pickup_latitude NUMERIC(9, 6),
            rate_code VARCHAR(100),
            store_and_fwd_flag VARCHAR(100),
            dropoff_longitude NUMERIC(9, 6),
            dropoff_latitude NUMERIC(9, 6),
            payment_type VARCHAR(20),
            fare_amount NUMERIC(5, 2),
            surcharge NUMERIC(5, 2),
            tip_amount NUMERIC(5, 2),
            tolls_amount NUMERIC(5, 2),
            total_amount NUMERIC(5, 2)
        );
        """
        cursor.execute(sql)
        logger.debug('trips table created')

        sql = """
        CREATE TABLE IF NOT EXISTS funcional.vendor(
            vendor_id VARCHAR(5),
            name VARCHAR(60),
            address VARCHAR(60),
            city VARCHAR(20),
            state VARCHAR(20),
            zip VARCHAR(6),
            country VARCHAR(20),
            contact VARCHAR(60),
            current VARCHAR(5)
        )"""
        cursor.execute(sql)
        logger.debug('trips table created')
        connection.commit()
        logger.debug('table creation commited')

    except:
        logger.error('problem on create table process')

    finally:
        return True


def db_createSchema(connection):
    logger = log.log()
    #try:
    cursor = connection.cursor()
    sql = "CREATE SCHEMA IF NOT EXISTS funcional;"
    cursor.execute(sql)
    logger.debug('funcional schema created')
    connection.commit()
    logger.debug('schema creation commited')

    #except:
    #   logger.error('problem on create schema process')

    #finally:
    #    return True
