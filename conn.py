import pymysql.cursors

def db_createConnection():
    try:
        # Connect to the database
        connection = pymysql.connect(host='funcionaldb.cf0vlrdfbqsd.us-east-1.rds.amazonaws.com',
                                    user='admin',
                                    password='12345678',
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
    except:
        print("error")
        pass
    db_createSchema(connection)
    db_createTables(connection)
    return connection

def db_createTables(connection):
    try:
        with connection.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS trips(
                cod INT NOT NULL AUTO_INCREMENT,
                vendor_id VARCHAR(5),
                DATE DATE,
                pickup_datetime TIMESTAMP(6),
                dropoff_datetime TIMESTAMP(6),
                passenger_count TINYINT,
                trip_distance DECIMAL(5, 2),
                pickup_longitude DECIMAL(10, 10),
                pickup_latitude DECIMAL(10, 10),
                rate_code VARCHAR(100),
                store_and_fwd_flag VARCHAR(100),
                dropoff_longitude DECIMAL(10, 10),
                dropoff_latitude DECIMAL(10, 10),
                payment_type VARCHAR(20),
                fare_amount DECIMAL(5, 2),
                surcharge DECIMAL(5, 2),
                tip_amount DECIMAL(5, 2),
                tolls_amount DECIMAL(5, 2),
                total_amount DECIMAL(5, 2),
                UNIQUE KEY `trip_key`(`cod`, `date`)
            ) PARTITION BY RANGE(YEAR(DATE))(
                PARTITION p0
            VALUES LESS THAN(2010),
            PARTITION p1
            VALUES LESS THAN(2011),
            PARTITION p2
            VALUES LESS THAN(2012),
            PARTITION p3
            VALUES LESS THAN MAXVALUE
            )"""
            cursor.execute(sql)
    finally:
        #connection.close()
        return True


def db_createSchema(connection):
    try:
        with connection.cursor() as cursor:
            sql = "CREATE DATABASE IF NOT EXISTS dbfuncional"
            cursor.execute(sql) #, ('webmaster@python.org', 'very-secret'))

#        # connection is not autocommit by default. So you must commit to save
#        # your changes.
#        connection.commit()
#
#        with connection.cursor() as cursor:
#            # Read a single record
#            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#            cursor.execute(sql, ('webmaster@python.org',))
#            result = cursor.fetchone()
#            print(result)
    finally:
        return True
