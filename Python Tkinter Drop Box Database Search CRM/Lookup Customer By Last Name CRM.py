# Python Tkinter Drop Box Database Search CRM
# CRM de búsqueda de base de datos de cuadro desplegable de Python Tkinter
# CRM de búsqueda de base de datos de cuadro desplegable


from tkinter import *
from PIL import ImageTk, Image
#import mysql.connector
import mysql.connector as mariadb
import csv # Archicos excell
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Drop Box Database Search CRM!')
root.iconbitmap('Python Tkinter Drop Box Database Search CRM/db.ico')
root.geometry("400x600") 

# Connect DATABASE
mydb = mariadb.connect(
#mydb = mysql.connector.connect(
    host="127.0.0.1",
    port = 3307,
    user="briandb",
    password="briandb",
    database = "cmd",
)

#Check to see if connection to MYSQL was created
print(mydb)

#create a cursor and initialize it
my_cursor = mydb.cursor()

# Create Database
#my_cursor.execute("CREATE DATABASE cmd")

# Test to seee if database was created 
#my_cursor.execute("SHOW DATABASES")
#print(my_cursor)
#for db in my_cursor:
#    print(db)

# Drop Table
#my_cursor.execute("DROP TABLE customers")

# Create Table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255),\
    last_name VARCHAR(255), \
    zipcade INT(10), \
    price_paid DECIMAL(10, 2),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Alter Table
'''my_cursor.execute("ALTER TABLE customers ADD (\
    email VARCHAR(255),\
    address_1 VARCHAR(255), \
    address_2  VARCHAR(255), \
    city VARCHAR(50),\
    state VARCHAR(50),\
    country VARCHAR(255),\
    phone VARCHAR(255),\
    payment_method VARCHAR(255),\
    dicount_code VARCHAR(255))")
'''

# Show table
#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)

#for thing in my_cursor.description:
#    print(thing)


# Create Function Clear_fileds / clear text fileds
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address_1_box.delete(0, END)
    address_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcade_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    dicount_cod_box.delete(0, END)
    price_paid_box.delete(0, END)

# create Main to Enter customer Data
first_name_label = Label(root, text="First Name").grid(row=1, column=0)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0)
address_1_label = Label(root, text="Address 1").grid(row=3, column=0)
address_2_label = Label(root, text="Address 2").grid(row=4, column=0)
city_label = Label(root, text="City").grid(row=5, column=0)
state_label = Label(root, text="State").grid(row=6, column=0)
zipcade_label = Label(root, text="Zipcode").grid(row=7, column=0)
country_label = Label(root, text="Country").grid(row=8, column=0)
phone_label = Label(root, text="Phone Number").grid(row=9, column=0)
email_label = Label(root, text="Email Address").grid(row=10, column=0)
#username_label = Label(root, text="Username").grid(row=11, column=0)
payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0)
dicount_code_label = Label(root, text="Discount Code").grid(row=12, column=0)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0)

# Submit customer To Database
def add_customer():
    sql_command = "INSERT INTO customers(first_name, last_name, address_1, address_2, city, state, zipcade, country, phone, email, payment_method, dicount_code, price_paid) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), address_1_box.get() ,address_2_box.get(), city_box.get(), state_box.get(), zipcade_box.get(), country_box.get(), phone_box.get(), email_box.get(), payment_method_box.get(), dicount_cod_box.get(), price_paid_box.get())
    my_cursor.execute(sql_command, values)

    mydb.commit()
    clear_fields()

# Write to CSV Excel Function
def write_to_csv(result):
    with open('Python Tkinter Drop Box Database Search CRM/customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)

# List Customers
def search_customer():
    search_customers=Tk()
    search_customers.title("Search All Customers")
    search_customers.iconbitmap('Python Tkinter Drop Box Database Search CRM/db.ico')
    search_customers.geometry("800x600") 

    def seach_now():

        selected = drop.get()
        sql=""
        if selected == "Search By...":
            test = Label(search_customers, text="Hey! You Forgot to pick a drop")
            test.grid(row=3, column=0)
        if selected == "Last name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
            #test = Label(search_customers, text="You picked Last Name")
            #test.grid(row=2, column=0)
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
            #test = Label(search_customers, text="You picked Last Email Address")
            #test.grid(row=2, column=0)
        if selected == "Customers ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"
            #test = Label(search_customers, text="You picked Customers Id")
            #test.grid(row=2, column=0)


        searched = search_box.get()
        #sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result="Record not found..."
        
        searched_label = Label(search_customers, text=result)
        searched_label.grid(row=2, column=0, padx=10, columnspan=2)
          
    #Entry box search for customers
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    # Entry box label search for costumers
    search_box_label = Label(search_customers, text="Search ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    # Entry box Label Button search for costumers.
    search_button = Button(search_customers, text="Search Customers", command=seach_now)
    search_button.grid(row=1, column=0, padx=10, pady=10)

    # Drop down Box
    drop= ttk.Combobox(search_customers, values=["Search By...","Last name", "Email Address", "Customers ID"])
    drop.current(0)
    drop.grid(row=0, column=2)


# List Customers
def list_customer():
    list_customer_query =Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.iconbitmap('Python Tkinter Drop Box Database Search CRM/db.ico')
    list_customer_query.geometry("800x600") 

    # Query the Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num)
            num +=1

    csv_button = Button(list_customer_query, text="Save to Excel", command = lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)

#create label
title_label = Label (root, text="MariaDb customer database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady="10")

# Create Entry Boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address_1_box = Entry(root)
address_1_box.grid(row=3, column=1, pady=5)

address_2_box = Entry(root)
address_2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcade_box = Entry(root)
zipcade_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

dicount_cod_box = Entry(root)
dicount_cod_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Create Buttons

add_customers_button = Button(root, text= "Add customer To Database", command=add_customer)
add_customers_button.grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text= "Cler Fileds", command=clear_fields)
clear_fields_button.grid(row=14, column=1)

# list_customer_button
list_customer_button = Button(root, text="List Customer", command= list_customer)
list_customer_button.grid(row=15, column=0, sticky=W, padx=10)

# Search Customers
search_customers_button = Button(root, text="Save Customers", command = search_customer)
search_customers_button.grid(row=15, column=1, sticky=W, padx=10)

root.mainloop()
