import psycopg2

def connect():
    return psycopg2.connect(
        host = "localhost", 
        database = "extraction_database", 
        user ="postgres", 
        password ="password", 
        port =5432
        )

def extract_timesheet_data(cur,con):
    delete="DELETE FROM raw_timesheet"
    cur.execute(delete)
    con.commit()
    with open('../schema/timesheet.sql') as file:
        sql = " ".join(file.readlines())
        cur.execute(sql)
        con.commit()
