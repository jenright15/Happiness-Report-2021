import mysql.connector

## Creating the connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="johne",
  password="jognrocks1",
  database= "Happiness"
)

mycursor = mydb.cursor()

#mycursor.execute('CREATE DATABASE Happiness')

create_db = "CREATE DATABASE Happiness"
create_countries_table_sql = "CREATE TABLE Countries (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255))"

mycursor.execute("SHOW TABLES")


