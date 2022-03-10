import psycopg2

try:
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", 
    user='admin', 
    password='admin1234', 
    host='127.0.0.1', 
    port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database climate_db''';

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    conn.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)