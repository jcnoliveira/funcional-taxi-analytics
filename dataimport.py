import json
import os.path
import datetime
import conn
import log
from datetime import datetime



def lambda_handler(event, context):
    logger = log.log()
    logger.debug('starting')


    connection = conn.db_createConnection()
    conn.db_query(connection, "START TRANSACTION;")
    logger.debug('starting transaction')


    for path, dirnames, filenames in os.walk('data/'):
        if path == "data/":
            filenames = ["data-sample_data-nyctaxi-trips-2009-json_corrigido.json"]
            for x in filenames:
                logger.debug('sending ' + x)

                with open(path+x) as json_file:
                    for p in json_file:
                        data = json.loads(p)
                        
                        data["pickup_datetime"] = datetime.strptime(data["pickup_datetime"], '%Y-%m-%dT%H:%M:%S.%f+00:00')
                        data["dropoff_datetime"] = datetime.strptime(data["dropoff_datetime"], '%Y-%m-%dT%H:%M:%S.%f+00:00')
                        data["date"] = data["pickup_datetime"].strftime('%Y-%m-%d')
                        sql = """INSERT INTO dbfuncional.trips (vendor_id, date, pickup_datetime, dropoff_datetime, passenger_count, trip_distance,
                                                    pickup_longitude, pickup_latitude, rate_code, store_and_fwd_flag, dropoff_longitude, 
                                                    dropoff_latitude, payment_type, fare_amount, surcharge, tip_amount, tolls_amount, total_amount)
                                 VALUES 
                                    ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');
                                    """.format(str(data["vendor_id"]), data["date"], data["pickup_datetime"], data["dropoff_datetime"], data["passenger_count"], data["trip_distance"],
                                               data["pickup_longitude"], data["pickup_latitude"], str(data["rate_code"]), str(data["store_and_fwd_flag"]), data["dropoff_longitude"], 
                                               data["dropoff_latitude"], str(data["payment_type"]), data["fare_amount"], data["surcharge"], data["tip_amount"], data["tolls_amount"], data["total_amount"])
                        print(sql.strip())
                        conn.db_query(connection, sql)
        if path == "data/lookups":
            print(path)
            print(filenames)
    connection.commit()
    #conn.db_query(connection, "COMMIT")
    logger.debug('commited')
#
    return {
        'statusCode': 200,
        
        'body': json.dumps('Hello from Lambda!')
    }



lambda_handler("a", "b")
