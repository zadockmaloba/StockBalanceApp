
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
        stock_database.append_dataframe(sd_DF, "Soft Drinks")
        #sd_DF.to_sql(name="Soft Drinks", con=dbs, if_exists='append')     This line is repetitive of the above
        sd_DF.to_csv('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/Stockbalance(softdrinks).csv')
        dbs.commit()
        #soft_drinks.load_table()

    def create_column(clmnName):
        sd_DF.insert(clmnName)

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
    def show_table():
        print(sd_DF)
    def load_table():
        readCSV=pd.read_csv('C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/Stockbalance(softdrinks).csv')
        print("CSV table loaded successfully")
        print(readCSV)
        itm = readCSV.at[0,'Item Name']
        qntty=readCSV.at[0,'Quantity']
        for items in itm:
            sd_items.append(items)
        for items in qntty:
            sd_amounts.append(items)
        print(sd_items)
        print(sd_amounts)



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
    global ad_items
    global ad_amounts
    global ad_stats

    ad_items=[]
    ad_amounts=[]
    ad_stats=[]
    def create_table():
        global ad_DF
        ad_DF=pd.DataFrame({"Item Name": ad_items,
                            "Quantity": ad_amounts,
                            "Status": ad_stats})
    def create_column(clmnName):
        ad_DF.insert(clmnName)
        #pass
    def add_item(itemName, itemQnty, itemStat):
        ad_items.append(itemName)
        ad_amounts.append(itemQnty)
        ad_stats.append(itemStat)
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
    dbpath='C:/Users/HP/Documents/codingnprogramming/projects/stockbalance_app/StockbalanceDB.db'
    if os.path.isfile(dbpath):
        print('Database loaded')
        dbs = sqlite3.connect(dbpath)
    else:
        print('Creating database')
        dbs = sqlite3.connect(dbpath)
    def append_dataframe(dfName, tableName):
        pd.DataFrame.to_sql(dfName, name=tableName, con=dbs, if_exists='append')
        dbs.commit()
        print("saved successfully")

class stock_csv(object):
    def append_toCSV(self):
        pass

soft_drinks.add_item("coke", 30, "good")
dry_goods.add_item("EXE flour", 20, "good")
#soft_drinks.show_table()
