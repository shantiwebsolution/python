import psycopg2

def table():
    connecion = psycopg2.connect(dbname="company", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = connecion.cursor()
    cursor.execute("CREATE TABLE employee (Name text, ID int, Age int);")
    print("Table created successfully")
    connecion.commit()
    connecion.close()
def data():
    connecion = psycopg2.connect(dbname="company", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = connecion.cursor()
    Name  = input("Enter Name: ")
    ID    = int(input("Enter ID: "))
    Age   = int(input("Enter Age: "))
    sql = "INSERT INTO employee (Name, ID, Age) VALUES (%s, %s, %s);"
    cursor.execute(sql, (Name, ID, Age))
    print("Data inserted successfully")
    connecion.commit()
    connecion.close()
def extract():
    connecion = psycopg2.connect(dbname="company", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = connecion.cursor()
    cursor.execute("SELECT * FROM employee;")
    row = cursor.fetchone()
    print(row)
    print(f"Name: {row[0]}, ID: {row[1]}, Age: {row[2]}")
    connecion.close()
data()
