#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import matplotlib.pyplot as plt
import numpy as np

con = pymysql.connect(host='localhost',
        user='dbuser',
        password='dbuserdbuser',
        db='lead_exposure',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

with con:


    cur = con.cursor()
    cur.execute("SELECT * FROM under_6_bll_cleaned where geo_area_name='Bronx'")
    bronx_rows = cur.fetchall()
    cur.execute("SELECT * FROM under_6_bll_cleaned where geo_area_name='Brooklyn'")
    brooklyn_rows = cur.fetchall()
    cur.execute("SELECT * FROM under_6_bll_cleaned where geo_area_name='Manhattan'")
    manhattan_rows = cur.fetchall()
    cur.execute("SELECT * FROM under_6_bll_cleaned where geo_area_name='Queens'")
    queens_rows = cur.fetchall()
    cur.execute("SELECT * FROM under_6_bll_cleaned where geo_area_name='Staten Island'")
    staten_rows = cur.fetchall()
    #cur = con.cursor()
    cur.execute("SELECT * FROM under_6_bll_cleaned where geo_type='Neighborhood (UHF 42)'")
    neighborhood_rows = cur.fetchall()

    #desc = cur.description
    #print("{0:>3} {1:>10} {2:>15}".format(desc[1][0], desc[2][0], desc[5][0]))
    '''
    Notes: 
    Need to not include SELECT * FROM fratt_lead_cooper where Lead_First_Draw_mg_L<Lead_1_to_2_Minute_Flush_mg_L
     - Seems there are 4 instances where the 1-2 min flush has an enter of 1, which seems like som inaccuracy 
     SELECT * FROM fratt_lead_cooper where Lead_First_Draw_mg_L<Lead_5_Minute_Flush_mg_L
     - 16 instances where there was an increase after 5 min flush
    '''

print()
time = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
plt.plot(time, [r['rate_greater_5'] for r in bronx_rows], label='Bronx')
plt.plot(time, [r['rate_greater_5'] for r in brooklyn_rows], label='Brooklyn')
plt.plot(time, [r['rate_greater_5'] for r in manhattan_rows], label='Manhattan')
plt.plot(time, [r['rate_greater_5'] for r in queens_rows], label='Queens')
plt.plot(time, [r['rate_greater_5'] for r in staten_rows], label='Staten Island')
plt.legend()
plt.show()


