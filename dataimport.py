import json
import os.path
import datetime
import conn

def lambda_handler(event, context):
    for path, dirnames, filenames in os.walk('data/'):
        if path == "data/":
            filenames = ["teste.json"]
            for x in filenames:
                with open(path+x) as json_file:
                    for p in json_file:
                        data = json.loads(p)

                        for key, value in data.items() :
                            print (key, type(value))
                        print("---------")

        if path == "data/lookups":
            print(path)
            print(filenames)
#
    return {
        'statusCode': 200,
        
        'body': json.dumps('Hello from Lambda!')
    }



lambda_handler("a", "b")
db_createSchema()