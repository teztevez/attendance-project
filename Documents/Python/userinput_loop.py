import mysql.connector
import datetime
from mysql.connector import Error
from mysql.connector import errorcode

emp = int #variable to act as emp_id

#using the sentinal 
while(emp != -1): 
    
    emp = (input("Ready for input. Please swipe in: "))
    print (emp) #display what user has entered

    try:
            connection = mysql.connector.connect(host='localhost',
                                                database='project',
                                                user='root',
                                                password='password')
        
            cursor = connection.cursor()
            
            now_str = datetime.datetime.now().strftime("%H:%M") #formats datetime to string to be in 24 hr format with hrs and mins (eg 18:00)
            now = datetime.datetime.strptime(now_str, "%H:%M") #formats string to datetime variable with format 10:00
            arrive_min = "07:00" #ealiest recognised arrival time
            arrive_max = "11:00" #latest recognised arrival time
            arrive_time1 = datetime.datetime.strptime(arrive_min, "%H:%M") #convert cutoff time to actual datetime variable
            arrive_time2 = datetime.datetime.strptime(arrive_max, "%H:%M") #convert cutoff time to actual datetime variable
            
            late_str = "09:00" #cutoff point for being on tne
            late = datetime.datetime.strptime(late_str, "%H:%M") 
            leave_min = "13:00"
            leave_max = "19:00"
            leave_time1 = datetime.datetime.strptime(leave_min, "%H:%M") #convert cutoff time to actual datetime variable
            leave_time2 = datetime.datetime.strptime(leave_max, "%H:%M")
            early_str = "17:00"
            early = datetime.datetime.strptime(early_str, "%H:%M") 
            
            if(now >= arrive_time1 and now <= arrive_time2): #if current time falls between 07:00 and 11:00
                if(now <= late):
                    sql_insert_query = """ INSERT INTO clockings (emp_id, direction, punctual) VALUES ((%s), "in", "acceptable")""" %(emp)
                else:
                    sql_insert_query = """ INSERT INTO clockings (emp_id, direction, punctual) VALUES ((%s), "in", "unacceptable")""" %(emp)
            elif(now >= leave_time1 and now <= leave_time2):
                if(now >= early):
                    sql_insert_query = """ INSERT INTO clockings (emp_id, direction, punctual) VALUES ((%s), "out", "acceptable")""" %(emp)
                else:
                    sql_insert_query = """ INSERT INTO clockings (emp_id, direction, punctual) VALUES ((%s), "out", "unacceptable")""" %(emp)
            else:
                sql_insert_query = """ INSERT INTO clockings (emp_id) VALUES (%s)""" %(emp)
            

        
        
            result = cursor.execute(sql_insert_query)
            connection.commit()
            print ("Thank you for punching the clock!")
            
            sql_select_query = "Select * from employee WHERE emp_id =(%s)" %(emp)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            
            for row in records:
                print("Hello " + row[1])
                print (now_str)

    except mysql.connector.Error as error :
            connection.rollback()
            print("Failed".format(error))  
    finally:
            if(connection.is_connected()):
                    cursor.close()
                    connection.close()