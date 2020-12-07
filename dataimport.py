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

    for path, dirnames, filenames in os.walk('data/'):
        if path == "data/":
            filenames = ["teste.json"]
            for x in filenames:
                with open(path+x) as json_file:
                    for p in json_file:
                        data = json.loads(p)
                        data["date"] = "10/10/2020"
                        data["pickup_datetime"] = datetime.strptime(data["pickup_datetime"], '%Y-%m-%dT%H:%M:%S.%f+00:00')
                        data["dropoff_datetime"] = datetime.strptime(data["dropoff_datetime"], '%Y-%m-%dT%H:%M:%S.%f+00:00')
                        sql = """INSERT INTO trips (vendor_id, date, pickup_datetime, dropoff_datetime, passenger_count, trip_distance,
                                                    pickup_longitude, pickup_latitude, rate_code, store_and_fwd_flag, dropoff_longitude, 
                                                    dropoff_latitude, payment_type, fare_amount, surcharge, tip_amount, tolls_amount, total_amount)
                                 VALUES 
                                    ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})
                                    """.format(data["vendor_id"], data["date"], data["pickup_datetime"], data["dropoff_datetime"], data["passenger_count"], data["trip_distance"],
                                               data["pickup_longitude"], data["pickup_latitude"], data["rate_code"], data["store_and_fwd_flag"], data["dropoff_longitude"], 
                                               data["dropoff_latitude"], data["payment_type"], data["fare_amount"], data["surcharge"], data["tip_amount"], data["tolls_amount"], data["total_amount"])
                        print(sql.strip())


                        #for key, value in data.items() :
                        #    print (key, type(value))
                        #print("---------")

        if path == "data/lookups":
            print(path)
            print(filenames)
    conn.db_query(connection, "COMMIT")

#
    return {
        'statusCode': 200,
        
        'body': json.dumps('Hello from Lambda!')
    }



lambda_handler("a", "b")
