import pymysql
import pandas as pd
import pymysql.cursors
from sshtunnel import SSHTunnelForwarder
import time
from datetime import date, timedelta

import _locate_
import sys
sys.path.insert(1,_locate_.BASE_DIR)
from connect_confidential.connect_db_final import cursor

import raw_sql_1
import raw_sql_2
import raw_sql_4
import raw_sql_3

# start1 = time.time()
today = date.today()
yesterday = today - timedelta(1)
yesterday_2 = yesterday - timedelta(1)
yesterday_3 = yesterday_2 - timedelta(1)
yesterday_4 = yesterday_3 - timedelta(1)

value_uniquedj = raw_sql_1.rawsql_uniquedj.format(today)
value_newdj = raw_sql_1.rawsql_newdj.format(today)
value_uniquelistener = raw_sql_1.rawsql_uniquelistener.format(today)
value_newlistener = raw_sql_1.rawsql_newlistener.format(today)
value_djandlistening = raw_sql_1.rawsql_djandlistening.format(today)
value_userdjcomment = raw_sql_1.rawsql_userdjcomment.format(today)     
value_dailydjcomment = raw_sql_1.rawsql_dailydjcomment.format(today)
value_chatroomnewjoiner = raw_sql_1.rawsql_chatroomnewjoiner.format(today)
value_userdmcomment = raw_sql_1.rawsql_userdmcomment.format(today)
value_dailydmcomment = raw_sql_1.rawsql_dailydmcomment.format(today)
value_djtotalhour = raw_sql_1.rawsql_djtotalhour.format(today)

operation = [
        value_uniquedj,
        value_newdj,
        value_uniquelistener,
        value_newlistener,
        value_djandlistening,
        value_userdjcomment,
        value_dailydjcomment,
        value_chatroomnewjoiner,
        value_userdmcomment,
        value_dailydmcomment,
        value_djtotalhour
        ]
# print(operation)
l = []
for result in operation:
        cursor.execute(result)
        result = cursor.fetchall()
        sql1 = pd.DataFrame(result).astype(str)
        sql2 = sql1.values.tolist()
        a = [float(str(sql2[len(sql2)-4]).strip('[]').strip("'")),
        float(str(sql2[len(sql2)-3]).strip('[]').strip("'")),
        float(str(sql2[len(sql2)-2]).strip('[]').strip("'")),
        float(str(sql2[len(sql2)-1]).strip('[]').strip("'"))]
        l.append(a)

uniquedj = l[0]
newdj = l[1]
uniquelistener = l[2]
newlistener = l[3]
djandlistening = l[4]
userdjcomment = l[5]
dailydjcomment = l[6]
chatroomnewjoiner = l[7]
userdmcomment = l[8]
dailydmcomment = l[9]
djtotalhour = l[10]

value_followers = raw_sql_2.rawsql_followers.format(today)
value_videocollect = raw_sql_2.rawsql_videocollect.format(today)
value_albumcollect = raw_sql_2.rawsql_albumcollect.format(today)
value_artistcollect = raw_sql_2.rawsql_artistcollect.format(today)
value_blockers = raw_sql_2.rawsql_blockers.format(today)

operation2 = [
        value_followers,
        value_videocollect,
        value_albumcollect,
        value_artistcollect,
        value_blockers]

l3 = []
for result2 in operation2:
        cursor.execute(result2)
        result2 = cursor.fetchall()
        sql1 = pd.DataFrame(result2).astype(str)
        sql2 = sql1.values.tolist()
        l2 = []
        for i in sql2:
                x = int(str(i).strip('[]').strip("'"))
                l2.append(x)
        l3.append(l2)

followers = l3[0]
videocollect = l3[1]
albumcollect = l3[2]
artistcollect = l3[3]
blockers = l3[4]
# print(blockers)

value_djreturn7 = raw_sql_4.rawsql_djreturn7.format(yesterday_2,yesterday)
value_djreturn14 = raw_sql_4.rawsql_djreturn14.format(yesterday_2,yesterday)
value_djreturn30 = raw_sql_4.rawsql_djreturn30.format(yesterday_2,yesterday)
value_djreturn7_2 = raw_sql_4.rawsql_djreturn7.format(yesterday_3,yesterday_2)
value_djreturn14_2 = raw_sql_4.rawsql_djreturn14.format(yesterday_3,yesterday_2)
value_djreturn30_2 = raw_sql_4.rawsql_djreturn30.format(yesterday_3,yesterday_2)
value_djreturn7_3 = raw_sql_4.rawsql_djreturn7.format(yesterday_4,yesterday_3)
value_djreturn14_3 = raw_sql_4.rawsql_djreturn14.format(yesterday_4,yesterday_3)
value_djreturn30_3 = raw_sql_4.rawsql_djreturn30.format(yesterday_4,yesterday_3)

operation3 = [
        [
        value_djreturn7_3,
        value_djreturn7_2,
        value_djreturn7
        ],
        [
        value_djreturn14_3,
        value_djreturn14_2,
        value_djreturn14
        ],
        [
        value_djreturn30_3,
        value_djreturn30_2,
        value_djreturn30
        ]
]

djreturn = []
for i in operation3:
        l = []
        for result3 in i:
                cursor.execute(result3)
                result3 = cursor.fetchall()
                sql1 = pd.DataFrame(result3).astype(str)
                sql2 = sql1.values.tolist()
                l.append(int(str(sql2).strip('[]').strip("'")))
        djreturn.append(l)
# print(djreturn)

value_videocontribute = raw_sql_3.rawsql_videocontribute
value_albumcontribute = raw_sql_3.rawsql_albumcontribute
value_artistcontribute = raw_sql_3.rawsql_artistcontribute

operation4 = [
        value_videocontribute,
        value_albumcontribute,
        value_artistcontribute
]

contribute = []
for result in operation4:
        # try:
        cursor.execute(result)
        result = cursor.fetchall()
        sql1 = pd.DataFrame(result).astype(str)
        sql4 = pd.Series(sql1[1].values, index = sql1[0])
        try:
                result1 = int(sql4[str(yesterday_3)])
        except KeyError:
                result1 = 0
        try:
                result2 = int(sql4[str(yesterday_2)])
        except KeyError:
                result2 = 0
        try:
                result3 = int(sql4[str(yesterday)])
        except KeyError:
                result3 = 0
        l = [result1, result2, result3]
        contribute.append(l)
# print(contribute)
# print(contribute[0])
# print(contribute[1])
# print(contribute[2])
# end1 = time.time()
# print('finished running queries in', end1 - start1,'seconds')