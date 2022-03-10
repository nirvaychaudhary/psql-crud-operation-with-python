import psycopg2

try:
     # connecting to database
    con = psycopg2.connect(user = "admin",
                                  password = "admin1234",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "climate_db")
    cur = con.cursor()
 
    # Print PostgreSQL version
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("\nYou are connected to - ", record,"\n")
 
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
 
finally:
    #closing database connection.
    if(con):
        cur.close()
        con.close()
        print("PostgreSQL connection is closed")
 