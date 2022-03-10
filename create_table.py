import psycopg2

try:
    con = psycopg2.connect(
        user='admin',
        password='admin1234',
        host = '127.0.0.1',
        port='5432',
        database='climate_db'
    )
    cur = con.cursor()
    cur.execute('''create table tbl_climate
          (temperature float not null,
          rainfall float not null,
          humidity float not null);
          ''')
 
    
    con.commit()
    
    print("Table created successfully")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
 
finally:
    #closing database connection.
        if(con):
            cur.close()
            con.close()
            print("PostgreSQL connection is closed")