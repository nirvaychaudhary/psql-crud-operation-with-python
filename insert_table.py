import psycopg2

try:
    con = psycopg2.connect(
        user = "admin",
        password = "admin1234",
        host = "127.0.0.1",
        port = "5432",
        database = "climate_db" 
    )
    cur = con.cursor()
    # cur.execute("select * from tbl_climate ");
    cur.execute("INSERT INTO tbl_climate (temperature, rainfall, humidity) \
          VALUES (39, 65, 70)");
    con.commit()
    print("Record inserted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error occured", error)

finally:
    #closing database connection.
    if(con):
        cur.close()
        con.close()
        print("PostgreSQL connection is closed")