import psycopg2

def connect():
    return psycopg2.connect(host= "localhost", database= "pipe", user= "postgres",password= "apple_ball",port= 5432)


def extract(filePath):
    connection = connect()
    cursor = connection.cursor()

    with open(filePath,'r') as file:
        i=0
        for line in file:
            if i ==0:
                i +=1
                continue
            
            row = line.split(",")
            sql = """INSERT INTO raw_employee_timesheet(employee_id, cost_center, punch_in_time, punch_out_time, punch_apply_date, hours_worked, paycode)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql, row)
            connection.commit() 
            i +=1
    cursor.close()
    connection.close()

if __name__ ==  "__main__":
    extract("../../data/timesheet_2021_05_23-Sheet1.csv")
    extract("../../data/timesheet_2021_06_23-Sheet1.csv")
    extract("../../data/timesheet_2021_07_23-Sheet1.csv")

