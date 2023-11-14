# Extraction of data from Phonepe github by using git clone in terminal

import json
import pandas as pd
import mysql.connector

# creating connection and cursor
conn = mysql.connector.connect(host = 'localhost', password = 'Saravanan123', user = 'root', port = 3307, database = 'phonepe')
if conn.is_connected():
    print('connected')
cursor = conn.cursor()
try:
    cursor.execute('create table phonepe.agg_tran(SL_No int auto_increment primary key, State varchar(255) not null, Year YEAR not null, Quarter varchar(2) not null, Transaction_Type varchar(250) not null, Transaction_Count int not null, Transaction_Amount bigint(20) UNSIGNED not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")
# except:
#     pass

# to drop the table
# cursor.execute('drop table agg_tran')
# cursor.execute('drop table agg_user')
# cursor.execute('drop table map_tran')
# cursor.execute('drop table map_user')
# cursor.execute('drop table top_tran_district')
# cursor.execute('drop table top_user_district')
# cursor.execute('drop table top_tran_pincode')
# cursor.execute('drop table top_user_pincode')
# conn.commit()
# conn.close()

state = ['andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar','chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya-pradesh','maharashtra','manipur','meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal']
def Agg_Transaction_Qua1():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['transactionData']:
                Amount = int(k['paymentInstruments'][0]['amount'])
                insert_query = 'insert into agg_tran(State, Year, Quarter, Transaction_Type, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q1',k['name'],k['paymentInstruments'][0]['count'],Amount)
                cursor.execute(insert_query,value)
                conn.commit()
   
def Agg_Transaction_Qua2():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['transactionData']:
                Amount = int(k['paymentInstruments'][0]['amount'])
                insert_query = 'insert into agg_tran(State, Year, Quarter, Transaction_Type, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q2',k['name'],k['paymentInstruments'][0]['count'],Amount)
                cursor.execute(insert_query,value)
                conn.commit()


def Agg_Transaction_Qua3():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['transactionData']:
                Amount = int(k['paymentInstruments'][0]['amount'])
                insert_query = 'insert into agg_tran(State, Year, Quarter, Transaction_Type, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q3',k['name'],k['paymentInstruments'][0]['count'],Amount)
                cursor.execute(insert_query,value)
                conn.commit()


def Agg_Transaction_Qua4():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['transactionData']:
                Amount = int(k['paymentInstruments'][0]['amount'])
                insert_query = 'insert into agg_tran(State, Year, Quarter, Transaction_Type, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q4',k['name'],k['paymentInstruments'][0]['count'],Amount)
                cursor.execute(insert_query,value)
                conn.commit()
                        
def aggregate_transactions():
    Agg_Transaction_Qua1()
    Agg_Transaction_Qua2()
    Agg_Transaction_Qua3()
    Agg_Transaction_Qua4()
# aggregate_transactions()

try:
    cursor.execute('create table phonepe.agg_user(SL_No int auto_increment primary key, State varchar(255) not null, Year YEAR not null, Quarter varchar(2) not null, User_Brand varchar(250) not null, User_Count int not null, User_Percentage int not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def Agg_user_Qua1():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\user\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['usersByDevice']:
                insert_query = 'insert into agg_user(State, Year, Quarter, User_Brand, User_Count, User_Percentage) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q1',k['brand'],k['count'],int(k['percentage']*100))
                cursor.execute(insert_query,value)
                conn.commit()

def Agg_user_Qua2():
    year = [2018,2019,2020,2021]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\user\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['usersByDevice']:
                insert_query = 'insert into agg_user(State, Year, Quarter, User_Brand, User_Count, User_Percentage) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q2',k['brand'],k['count'],int(k['percentage']*100))
                cursor.execute(insert_query,value)
                conn.commit()


def Agg_user_Qua3():
    year = [2018,2019,2020,2021]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\user\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['usersByDevice']:
                insert_query = 'insert into agg_user(State, Year, Quarter, User_Brand, User_Count, User_Percentage) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q3',k['brand'],k['count'],int(k['percentage']*100))
                cursor.execute(insert_query,value)
                conn.commit()


def Agg_user_Qua4():
    year = [2018,2019,2020,2021]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\aggregated\\user\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['usersByDevice']:
                insert_query = 'insert into agg_user(State, Year, Quarter, User_Brand, User_Count, User_Percentage) values(%s,%s,%s,%s,%s,%s)'
                value = (i,j,'Q4',k['brand'],k['count'],int(k['percentage']*100))
                cursor.execute(insert_query,value)
                conn.commit()


def aggregate_users():
    Agg_user_Qua1()
    Agg_user_Qua2()
    Agg_user_Qua3()
    Agg_user_Qua4()
# aggregate_users()

try:
    cursor.execute('create table phonepe.map_tran(SL_No int auto_increment primary key, State varchar(255) not null, District varchar(250) not null, Year YEAR not null, Quarter varchar(2) not null, Transaction_Count int not null, Transaction_Amount bigint(20) UNSIGNED not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def map_tran_Qua1():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['hoverDataList']:
                amount = int(k['metric'][0]['amount'])
                dt = k['name'].split('district')[0]
                insert_query = 'insert into map_tran(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q1',k['metric'][0]['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()

def map_tran_Qua2():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['hoverDataList']:
                amount = int(k['metric'][0]['amount'])
                dt = k['name'].split('district')[0]
                insert_query = 'insert into map_tran(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q2',k['metric'][0]['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()

def map_tran_Qua3():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['hoverDataList']:
                amount = int(k['metric'][0]['amount'])
                dt = k['name'].split('district')[0]
                insert_query = 'insert into map_tran(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q3',k['metric'][0]['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()


def map_tran_Qua4():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['hoverDataList']:
                amount = int(k['metric'][0]['amount'])
                dt = k['name'].split('district')[0]
                insert_query = 'insert into map_tran(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q4',k['metric'][0]['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()

def map_transactions():
    map_tran_Qua1()
    map_tran_Qua2()
    map_tran_Qua3()
    map_tran_Qua4()
# map_transactions()

try:
    cursor.execute('create table phonepe.map_user(SL_No int auto_increment primary key, State varchar(255) not null, District varchar(250) not null, Year YEAR not null, Quarter varchar(2) not null, Registered_Users int not null, App_Opens int not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def map_user_Qua1():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\user\\hover\\country\\india\\state\\{i}\\{j}\\1.json')
            for district,Data in data['data']['hoverData'].items():
                dt = district.split('district')[0]
                insert_query = 'insert into map_user(State, District, Year, Quarter, Registered_Users, App_Opens) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q1',Data['registeredUsers'],Data['appOpens'])
                cursor.execute(insert_query,value)
                conn.commit()


def map_user_Qua2():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\user\\hover\\country\\india\\state\\{i}\\{j}\\2.json')
            for district,Data in data['data']['hoverData'].items():
                dt = district.split('district')[0]
                insert_query = 'insert into map_user(State, District, Year, Quarter, Registered_Users, App_Opens) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q2',Data['registeredUsers'],Data['appOpens'])
                cursor.execute(insert_query,value)
                conn.commit()


def map_user_Qua3():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\user\\hover\\country\\india\\state\\{i}\\{j}\\3.json')
            for district,Data in data['data']['hoverData'].items():
                dt = district.split('district')[0]
                insert_query = 'insert into map_user(State, District, Year, Quarter, Registered_Users, App_Opens) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q3',Data['registeredUsers'],Data['appOpens'])
                cursor.execute(insert_query,value)
                conn.commit()


def map_user_Qua4():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\map\\user\\hover\\country\\india\\state\\{i}\\{j}\\4.json')
            for district,Data in data['data']['hoverData'].items():
                dt = district.split('district')[0]
                insert_query = 'insert into map_user(State, District, Year, Quarter, Registered_Users, App_Opens) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q4',Data['registeredUsers'],Data['appOpens'])
                cursor.execute(insert_query,value)
                conn.commit()

def map_users():
    map_user_Qua1()
    map_user_Qua2()
    map_user_Qua3()
    map_user_Qua4()
# map_users()

try:        
    cursor.execute('create table phonepe.top_tran_district(SL_No int auto_increment primary key, State varchar(255) not null, District varchar(250) not null, Year YEAR not null, Quarter varchar(2) not null, Transaction_Count int not null, Transaction_Amount bigint(20) UNSIGNED not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def top_tran_Qua1_dt():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['districts']:
                amount = int(k['metric']['amount'])
                dt = k['entityName'].split('district')[0]
                insert_query = 'insert into top_tran_district(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q1',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()


def top_tran_Qua2_dt():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['districts']:
                amount = int(k['metric']['amount'])
                dt = k['entityName'].split('district')[0]
                insert_query = 'insert into top_tran_district(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q2',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()


def top_tran_Qua3_dt():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['districts']:
                amount = int(k['metric']['amount'])
                dt = k['entityName'].split('district')[0]
                insert_query = 'insert into top_tran_district(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q3',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()


def top_tran_Qua4_dt():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['districts']:
                amount = int(k['metric']['amount'])
                dt = k['entityName'].split('district')[0]
                insert_query = 'insert into top_tran_district(State, District, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q4',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()


def top_transaction_district():
    top_tran_Qua1_dt()
    top_tran_Qua2_dt()
    top_tran_Qua3_dt()
    top_tran_Qua4_dt()
    conn.close()
# top_transaction_district()


try:  
    cursor.execute('create table phonepe.top_tran_pincode(SL_No int auto_increment primary key, State varchar(255) not null, Pincode int not null, Year YEAR not null, Quarter varchar(2) not null, Transaction_Count int not null, Transaction_Amount bigint(20) UNSIGNED not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def top_tran_Qua1_pc():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['pincodes']:
                amount = int(k['metric']['amount'])
                insert_query = 'insert into top_tran_pincode(State, Pincode, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,k['entityName'],j,'Q1',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()

def top_tran_Qua2_pc():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['pincodes']:
                amount = int(k['metric']['amount'])
                insert_query = 'insert into top_tran_pincode(State, Pincode, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,k['entityName'],j,'Q2',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()

def top_tran_Qua3_pc():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['pincodes']:
                amount = int(k['metric']['amount'])
                insert_query = 'insert into top_tran_pincode(State, Pincode, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                value = (i,k['entityName'],j,'Q3',k['metric']['count'],amount)
                cursor.execute(insert_query,value)
                conn.commit()

def top_tran_Qua4_pc():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\transaction\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['pincodes']:
                try:
                    amount = int(k['metric']['amount'])
                    insert_query = 'insert into top_tran_pincode(State, Pincode, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                    value = (i,k['entityName'],j,'Q4',k['metric']['count'],amount)
                    cursor.execute(insert_query,value)
                    conn.commit()
                except:
                    amount = int(k['metric']['amount'])
                    insert_query = 'insert into top_tran_pincode(State, Pincode, Year, Quarter, Transaction_Count, Transaction_Amount) values(%s,%s,%s,%s,%s,%s)'
                    value = (i,0,j,'Q4',k['metric']['count'],amount)
                    cursor.execute(insert_query,value)
                    conn.commit()

def top_transaction_pincode():
    top_tran_Qua1_pc()
    top_tran_Qua2_pc()
    top_tran_Qua3_pc()
    top_tran_Qua4_pc()
    conn.close()
# top_transaction_pincode()

try:       
    cursor.execute('create table phonepe.top_user_district(SL_No int auto_increment primary key, State varchar(255) not null, district varchar(250) not null, Year YEAR not null, Quarter varchar(2) not null, Registered_Users int not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def top_user_Qua1_dt():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['districts']:
                dt = k['name'].split('district')[0]
                insert_query = 'insert into top_user_district(State, District, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q1',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_Qua2_dt():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['districts']:
                dt = k['name'].split('district')[0]
                insert_query = 'insert into top_user_district(State, District, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q2',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_Qua3_dt():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['districts']:
                dt = k['name'].split('district')[0]
                insert_query = 'insert into top_user_district(State, District, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q3',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_Qua4_dt():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['districts']:
                dt = k['name'].split('district')[0]
                insert_query = 'insert into top_user_district(State, District, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,dt,j,'Q4',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_district():
    top_user_Qua1_dt()
    top_user_Qua2_dt()
    top_user_Qua3_dt()
    top_user_Qua4_dt()
    conn.close()
# top_user_district()

try:      
    cursor.execute('create table phonepe.top_user_pincode(SL_No int auto_increment primary key, State varchar(255) not null, Pincode int not null, Year YEAR not null, Quarter varchar(2) not null, Registered_Users int not null)')
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def top_user_Qua1_pc():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\1.json')
            for k in data['data']['pincodes']:
                insert_query = 'insert into top_user_pincode(State, Pincode, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,k['name'],j,'Q1',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_Qua2_pc():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\2.json')
            for k in data['data']['pincodes']:
                insert_query = 'insert into top_user_pincode(State, Pincode, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,k['name'],j,'Q2',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_Qua3_pc():
    year = [2018,2019,2020,2021,2022,2023]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\3.json')
            for k in data['data']['pincodes']:
                insert_query = 'insert into top_user_pincode(State, Pincode, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,k['name'],j,'Q3',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_Qua4_pc():
    year = [2018,2019,2020,2021,2022]
    for i in state:
        for j in year:
            data = pd.read_json(f'C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\pulse\\data\\top\\user\\country\\india\\state\\{i}\\{j}\\4.json')
            for k in data['data']['pincodes']:
                insert_query = 'insert into top_user_pincode(State, Pincode, Year, Quarter, Registered_Users) values(%s,%s,%s,%s,%s)'
                value = (i,k['name'],j,'Q4',k['registeredUsers'])
                cursor.execute(insert_query,value)
                conn.commit()

def top_user_pincode():
    top_user_Qua1_pc()
    top_user_Qua2_pc()
    top_user_Qua3_pc()
    top_user_Qua4_pc()
    conn.close()
# top_user_pincode()
