from connection import connect
import json
import psycopg2

def connect():
    return psycopg2.connect(host= "localhost", database= "pipe", user= "postgres",password= "apple_ball",port= 5432)

def extract_employee__raw_data(filePath):
    connection = connect()
    cursor = connection.cursor()
    f = open(filePath)
    data = json.load(f)
    
    
 

    with open(filePath, 'r') as file:
        i = 0
        for line in file:
           if i == 0:
               i += 1
                continue

           row = line.values().split(",")
           sql= """INSERT INTO raw_employee(employee_id,first_name,last_name,department_id,department_name,manager_employee_id,employee_role,salary,hire_date,terminated_date,terminated_reason,dob,fte,location)
            VALUES(%s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"""
            
            cursor.execute(sql, row)
            connection.commit()
            i +=1 
    cursor.close()
    connection.close()


if __name__ == "__main__":
    extract_employee_data("../../data/employee_2021_08_01.json")
