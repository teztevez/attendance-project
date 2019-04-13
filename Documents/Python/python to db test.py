{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Record inserted successfully into admin table\n",
      "MySQL connection is closed\n"
     ]
    }
   ],
   "source": [
    "import mysql.connector #allows python to connect to database\n",
    "from mysql.connector import Error\n",
    "from mysql.connector import errorcode\n",
    "try:\n",
    "   connection = mysql.connector.connect(host='localhost', \n",
    "                             database='project',\n",
    "                             user='root',\n",
    "                             password='password')\n",
    "   sql_insert_query = \"\"\" INSERT INTO `admin`\n",
    "                          (`username`, `password`) VALUES ('Terry','1234')\"\"\"\n",
    "   cursor = connection.cursor() #creates a new mysqlcursor object\n",
    "   result  = cursor.execute(sql_insert_query) #executes the prepared statement\n",
    "   connection.commit()\n",
    "   print (\"Record inserted successfully into admin table\")\n",
    "except mysql.connector.Error as error :\n",
    "    connection.rollback() #rollback if any exception occured\n",
    "    print(\"Failed inserting record into python_users table {}\".format(error))\n",
    "finally:\n",
    "    #closing database connection.\n",
    "    if(connection.is_connected()):\n",
    "        cursor.close()\n",
    "        connection.close()\n",
    "        print(\"MySQL connection is closed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
