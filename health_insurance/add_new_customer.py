from core.db.db import db
from datetime import date
from get_customer_id import get_customer_id
prevID =db('select max(C_id) from Customers;')[0][0];
prevID = int(prevID)
def add_new_customer(list_of_data):
    ssn = list_of_data[0]
    name = list_of_data[1]
    birth_date = list_of_data[2]
    gender = list_of_data[3]
    income = list_of_data[4]
    address = list_of_data[5]
    phone = list_of_data[6]
    has_chronic_dis = list_of_data[7]
    tall = list_of_data[8]
    weight = list_of_data[9]
    email = list_of_data[10]
    plane = list_of_data[11]
    price = db(f"select Price from plane where P_id = {plane}")[0][0]
    today = date.today()
    db(f'''INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
    ("{ssn}","{name}", "{birth_date}", "{gender}", {income}, "{address}", "{phone}", {has_chronic_dis}, {tall}, {weight}, "{email}", {plane});''',
    f'''INSERT INTO Payments (amount, date, Customer) VALUES ({price},"{today}", {prevID +1});'''
    )
    
   
    return "successfuly"

