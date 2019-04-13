import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

emp = int

emp = (input("Enter something: "))
print (emp)




try:
        connection = mysql.connector.connect(host='localhost',
                                            database='project',
                                            user='root',
                                            password='password')
        
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO time (emp_id) VALUES (%s)""" %(emp)

        
        
        result = cursor.execute(sql_insert_query)
        connection.commit()
        print ("Success")

except mysql.connector.Error as error :
        connection.rollback()
        print("Failed".format(error))
finally:
        if(connection.is_connected()):
                cursor.close()
                connection.close()
                print ("Connection closed.")
        
