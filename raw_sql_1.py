from datetime import date, timedelta

#những queries để lấy ra 2 giá trị
rawsql_djtotalhour = """ WITH t1 AS (
                        SELECT DISTINCT
                                UUID 
                        FROM
                                original_social_graph.sg_djsessions 
                        WHERE
                                CreatedAt > '2020-09-07'
                                
                                AND EXTRACT( HOUR FROM cast( TIMEDIFF( EndedAt, BroadcastAt ) AS TIME ) ) > 24 
                        ) SELECT
                        #CAST(CreatedAt as date),
                        round(
                                sum( EXTRACT( HOUR FROM ( cast( TIMEDIFF( EndedAt, CreatedAt ) AS time ) ) ) ) + sum( EXTRACT( MINUTE FROM ( cast( TIMEDIFF( EndedAt, CreatedAt ) AS time ) ) ) ) / 60 + sum( EXTRACT( SECOND FROM ( cast( TIMEDIFF( EndedAt, CreatedAt ) AS time ) ) ) / 60 / 60 ),
                                2 
                        ) AS hours 
                FROM
                        original_social_graph.sg_djsessions 
                WHERE
                        CreatedAt > '2020-09-07'
                        AND CreatedAt < '{}'
                        AND sg_djsessions.uuid NOT IN ( SELECT t1.uuid FROM t1 ) 
                GROUP BY
                        CAST( CreatedAt AS date ) ASC"""

rawsql_uniquedj = """SELECT
                        #CAST( CreatedAt AS date ),
                        count( DISTINCT UserUUID ) 
                FROM
                        original_social_graph.sg_djsessions 
                WHERE
                        CreatedAt > '2020-09-07'
                        AND CreatedAt < '{}'
                GROUP BY
                        CAST( CreatedAt AS date ) ASC"""

rawsql_newdj = """ WITH t1 AS (
                        SELECT
                            min( CAST( CreatedAt AS date ) ) AS date,
                            UserUUID 
                        FROM
                            original_social_graph.sg_djsessions 
                        WHERE
                            CreatedAt > '2020-09-07' 
                            AND CreatedAt < '{}' 
                        GROUP BY
                            UserUUID 
                        ORDER BY
                            date ASC 
                        ) SELECT
                        #t1.date,
                        count( t1.UserUUID ) 
                    FROM
                        t1 
                    GROUP BY
                        t1.date 
                    ORDER BY
                        t1.date ASC"""

rawsql_djandlistening = """WITH t3 AS (
                        WITH t2 AS (
                                WITH t1 AS (
                                        SELECT DISTINCT
                                                CAST( sga.CreatedAt AS date ) AS date,
                                                sga.UserUUID AS useruuid 
                                        FROM
                                                original_social_graph.sg_djsessionaudience sga
                                                JOIN original_social_graph.sg_djsessions sgd ON sgd.UUID = sga.DJSessionUUID 
                                        WHERE
                                                sga.CreatedAt > '2020-09-07' 
                                                AND sga.CreatedAt < '{}' 
                                                AND sga.UserUUID != sgd.UserUUID 
                                        GROUP BY
                                                CAST( sga.CreatedAt AS date ) DESC,
                                                sga.UserUUID 
                                        ORDER BY
                                                CAST( sga.CreatedAt AS date ) ASC 
                                        ) SELECT DISTINCT
                                        t1.date,
                                        t1.useruuid 
                                FROM
                                        t1 
                                ORDER BY
                                        t1.date ASC 
                                ) SELECT DISTINCT
                                CAST( sg_djsessions.CreatedAt AS date ) AS date,
                                sg_djsessions.UserUUID 
                        FROM
                                original_social_graph.sg_djsessions
                                INNER JOIN t2 ON CAST( sg_djsessions.CreatedAt AS date ) = t2.date 
                                AND sg_djsessions.UserUUID = t2.useruuid
                                
                        ORDER BY
                                CAST( sg_djsessions.CreatedAt AS date ) ASC 
                        ) SELECT
                        #t3.date,
                        count( t3.UserUUID ) 
                FROM
                        t3 
                GROUP BY
                        t3.date 
                ORDER BY
                        t3.date ASC"""

rawsql_dailydjcomment = """SELECT
                        #CAST( CreatedAt AS date ),
                        count( UserUUID ) 
                FROM
                        original_social_graph.sg_usercomments 
                WHERE
                        CreatedAt > '2020-09-07'
                        and CreatedAt < '{}'
                GROUP BY
                        CAST( CreatedAt AS date ) ASC"""

rawsql_userdjcomment = """SELECT
                        #CAST( CreatedAt AS date ),
                        count( DISTINCT UserUUID ) 
                FROM
                        original_social_graph.sg_usercomments 
                WHERE
                        CreatedAt > '2020-09-07' 
                        and createdat < '{}' 
                GROUP BY
                        CAST( CreatedAt AS date ) ASC"""

rawsql_dailydmcomment = """SELECT
                        #StartTime,
                        messagecount 
                FROM
                        v4.dm_statistics 
                WHERE
                        Type = 'daily' 
                        AND StartTime < '{}'
                        """

rawsql_userdmcomment = """SELECT
                        #StartTime,
                        usercount 
                FROM
                        v4.dm_statistics 
                WHERE
                        Type = 'daily' 
                        AND StartTime < '{}'
                        """

rawsql_chatroomnewjoiner = """SELECT
                        #CAST ( CreatedAt AS date ),
                        count( DISTINCT sg_map_conversation_user.UserUUID ) 
                FROM
                        original_social_graph.sg_map_conversation_user 
                WHERE
                        UserRole = 1 
                        AND MessageReadCount > 0 
                        AND createdat < '{}' 
                GROUP BY
                        CAST(CreatedAt AS date)"""

rawsql_uniquelistener = """WITH t1 AS (
                        SELECT DISTINCT
                                CAST( sga.CreatedAt AS date ) AS date,
                                count( DISTINCT sga.UserUUID ) AS useruuid 
                        FROM
                                original_social_graph.sg_djsessionaudience sga
                                JOIN original_social_graph.sg_djsessions sgd ON sgd.UUID = sga.DJSessionUUID 
                        WHERE
                                CAST( sga.CreatedAt AS date ) > '2020-09-13' 
                                AND sga.UserUUID != sgd.UserUUID 
                        GROUP BY
                                date 
                        ORDER BY
                                date 
                        ) SELECT
                        t1.useruuid 
                FROM
                        t1 
                WHERE
                        t1.date < '{}' 
                ORDER BY
                        t1.date"""

rawsql_newlistener = """WITH t3 AS (
                        SELECT
                                min( CAST( sga.CreatedAt AS date ) ) AS date,
                                sga.UserUUID AS useruuid 
                        FROM
                                original_social_graph.sg_djsessionaudience sga
                                JOIN original_social_graph.sg_djsessions sgd ON sgd.UUID = sga.DJSessionUUID 
                        WHERE
                                sga.CreatedAt > '2020-09-07' 
                                AND sga.CreatedAt < '{}'
                                AND sga.UserUUID != sgd.UserUUID 
                        GROUP BY
                                sga.UserUUID 
                        ORDER BY
                                date 
                        ) SELECT
                        #t3.date,
                        count( t3.UserUUID ) 
                FROM
                        t3 
                GROUP BY
                        t3.date 
                ORDER BY
                        t3.date"""



today = date.today()
yesterday = date.today() - timedelta(1)
yesterday_2 = date.today() - timedelta(2)
# value = (sql.format(yesterday_2,today))
value_1 = (rawsql_djtotalhour.format(today))
value_2 = (rawsql_uniquedj.format(today))
value_3 = (rawsql_newdj.format(today))
value_4 = (rawsql_djandlistening.format(today))
value_5 = (rawsql_dailydjcomment.format(today))
# print(value_1)
# print(value_2)
# print(value_3)
# print(value_4)
# print(value_5)
