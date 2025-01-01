import sqlite3
import ctypes
from typing import List
import os
from escpos.printer import Serial
from datetime import datetime

printer = 'COM5'

p = Serial(devfile=printer,
           baudrate=115200,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=True)


db_name= os.path.join(os.getcwd(), "database", "restaurant.db")

def get_conn():
    conn=sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn

def dict_factory(cursor,row):
    d={}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def update_order_data(param):
    try:
        sql = 'UPDATE FoodOrder SET qty=:qty , total_price=:total_price WHERE customer_name=:customer_name AND item_name=:item_name'
        conn = get_conn()
        curssor = conn.cursor()
        curssor.execute(sql,param)
        conn.commit()
        return True
    except Exception as e:
        print("failed INSERT db ERROR : ", e)
    
def insert_order_data(param):
    try:
        sql = 'INSERT INTO FoodOrder (item_name, qty, price, total_price, customer_name) VALUES (:item_name, :qty, :price, :total_price, :customer_name)'
        conn = get_conn()
        curssor = conn.cursor()
        curssor.execute(sql,param)
        conn.commit()
        return True
    except Exception as e:
        print("failed INSERT db ERROR : ", e)
        
def handle_order_data(param):
    try:
        data_exist = get_order_data_by_name_and_item(param)
        
        #data already exist, we wiil update it
        if len(data_exist) > 0:
            update_order_data(param)
        else:
            insert_order_data(param)
    except Exception as e:
        print("failed INSERT db ERROR : ", e)
        
def get_order_data_by_name_and_item(param):
    try:
        sql = 'SELECT * FROM FoodOrder WHERE customer_name=:customer_name AND item_name=:item_name'
        conn = get_conn()
        curssor = conn.cursor()
        curssor.execute(sql,param)
        result = curssor.fetchall()
        return result
    except Exception as e:
        print("FAILED get parking by id => " + str(e))
        return False
    
def get_order_data_by_name(param):
    try:
        sql = 'SELECT * FROM FoodOrder WHERE customer_name=:customer_name'
        conn = get_conn()
        curssor = conn.cursor()
        curssor.execute(sql,param)
        result = curssor.fetchall()
        return result
    except Exception as e:
        print("FAILED get parking by id => " + str(e))
        return False
    
def delete_data_order():
    try:
        sql = 'DELETE FROM FoodOrder'
        conn = get_conn()
        curssor = conn.cursor()
        curssor.execute(sql,{})
        conn.commit()
        return True
    except Exception as e:
        print("FAILED get parking by id => " + str(e))
        return False


# DISPALY RESOLUTION
def get_screen_resolution() -> List[int]:
    # return width, height of screen
    user32 = ctypes.windll.user32
    screensize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    # print(screensize)
    return screensize


#Printer function

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_receip(data):
    try:
        p.set(align='center')
        p.text("E-Kiosk System\n")
        p.text("Prayogo's Kitchen\n")
        p.text(str(get_datetime()))
        p.text("\n")
        p.text("-------------------------------\n")
        p.text("-------------------------------\n")
        p.close()    
    except Exception as e:
        print(f"error print {e}")
    
