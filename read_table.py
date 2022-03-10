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
    cur.execute("SELECT temperature, rainfall, humidity from tbl_climate")
    records = cur.fetchall()
    print("     CLIMATE INFORMATION       ")
    print("-----------------------------------")
    for row in records:
        print("     Temperature = ", row[0])
 
        print("     Rainfall = ", row[1])
 
        print("     Humidity = ", row[2])
 
        "\n"
 
    con.commit()
except (Exception, psycopg2.Error) as error:
    print("Error occured", error)

finally:
    #closing database connection.
    if(con):
        cur.close()
        con.close()
        print("PostgreSQL connection is closed")