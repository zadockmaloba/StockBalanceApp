
#Main file of the Stock Balance app

import os
import sys
import sqlite3
import pandas as pd
import numpy as np
import matplotlib
import csv

class soft_drinks(object):
    global sd_items
    global sd_amounts
    global sd_stats

    sd_items=[]
    sd_amounts=[]
    sd_stats=[]
    def create_table():
        global sd_DF
        sd_DF=pd.DataFrame({"Item Name": sd_items,
                            "Quantity": sd_amounts,
                            "Status": sd_stats})
        #stock_database.append_dataframe(sd_DF, "Soft Drinks")
        sd_DF.to_sql(name="Soft Drinks", con=dbs, if_exists='append')
        sd_DF.to_csv('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/Stockbalance(softdrinks).csv')
        dbs.commit()
        soft_drinks.load_table()

        #print(sd_DF)
        #pass
    def create_column(clmnName):
        sd_DF.insert(clmnName)
        #pass
    def add_item(itemName, itemQnty, itemStat):
        sd_items.append(itemName)
        sd_amounts.append(itemQnty)
        sd_stats.append(itemStat)
        soft_drinks.create_table()

        #pass
    def subtract_item():
        pass
    def check_balance():
        pass
    def remove_item():
        pass
    def show_table():
        print(sd_DF)
    def load_table():
        pd.read_csv('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/Stockbalance(softdrinks).csv')
        print("CSV table loaded successfully")


class spices(object):
    global sp_items
    global sp_amounts
    global sp_stats

    sp_items=[]
    sp_amounts=[]
    sp_stats=[]
    def create_table():
        global sp_DF
        sp_DF=pd.DataFrame({"ItemName": sp_items,
                            "Quantity": sp_amounts,
                            "Status": sp_stats})

    def create_column(clmnName):
        sp_DF.insert(clmnName)
        pass
    def add_item(itemName, itemQnty, itemStat):
        sp_items.append(itemName)
        sp_amounts.append(itemQnty)
        sp_stats.append(itemStat)
        spices.create_table()

    def subtract_item():
        pass
    def check_balance():
        pass
    def remove_item():
        pass

class dry_goods(object):
    global dg_items
    global dg_amounts
    global dg_stats

    dg_items=[]
    dg_amounts=[]
    dg_stats=[]
    def create_table():
        global dg_DF
        dg_DF=pd.DataFrame({"Item Name": dg_items,
                            "Quantity": dg_amounts,
                            "Status": dg_stats})

    def create_column(clmnName):
        dg_DF.insert(clmnName)

    def add_item(itemName, itemQnty, itemStat):
        dg_items.append(itemName)
        dg_amounts.append(itemQnty)
        dg_stats.append(itemStat)
        dry_goods.create_table()
    def subtract_item():
        pass
    def check_balance():
        pass
    def remove_item():
        pass

class alcoholic_drinks(object):
    global sd_items
    global sd_amounts
    global sd_stats

    sd_items=[]
    sd_amounts=[]
    sd_stats=[]
    def create_table():
        global sd_DF
        sd_DF=pd.DataFrame({"Item Name": sd_items,
                            "Quantity": sd_amounts,
                            "Status": sd_stats})

        #print(sd_DF)
        #pass
    def create_column(clmnName):
        sd_DF.insert(clmnName)
        #pass
    def add_item(itemName, itemQnty, itemStat):
        sd_items.append(itemName)
        sd_amounts.append(itemQnty)
        sd_stats.append(itemStat)
        soft_drinks.create_table()
    def subtract_item():
        pass
    def check_balance():
        pass
    def remove_item():
        pass

class stock_database(object):
    global dbs
    global fdb
    if os.path.isfile('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/StockbalanceDB.db'):
        print('Database loaded')
        dbs = sqlite3.connect('C:/Users/HP/Documents/codingnprogramming/projects/pyprojects/School Database/StockbalanceDB.db')
        #fdb=open('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/StockbalanceDB.db', "w+")
    else:
        #fdb=open('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/StockbalanceDB.db', "w+")
        print('Creating database')
        dbs = sqlite3.connect('C:/Users/HP/Documents/codingnprogramming/projects/pyprojects/School Database/StockbalanceDB.db')
        #dbs.execute("create table company(Name, text);")


    def append_dataframe(dfName, tableName):

        #pd.DataFrame.to_sql(dfName, name=tableName, con=db, if_exists='append')
        dbs.commit()
        print("saved successfully")
        #pass
class stock_csv(object):
    def append_toCSV(self):
        pass

soft_drinks.add_item("sprite", 30, "good")
dry_goods.add_item("EXE flour", 20, "good")
#soft_drinks.show_table()
