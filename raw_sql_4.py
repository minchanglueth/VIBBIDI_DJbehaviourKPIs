from datetime import date, timedelta

#những queries liên quan đến djreturn
rawsql_djreturn7 = """WITH t2 AS (
                WITH t1 AS (
                        SELECT DISTINCT
                                CAST( CreatedAt AS date ) AS date,
                                UserUUID 
                        FROM
                                original_social_graph.sg_djsessions 
                        WHERE
                                CAST( CreatedAt AS date ) <= '{}' 
                        ORDER BY
                                CreatedAt ASC 
                        ) SELECT
                        sg_djsessions.CreatedAt,
                        t1.UserUUID,
                        count( DISTINCT t1.date ) 
                FROM
                        t1
                        JOIN original_social_graph.sg_djsessions ON sg_djsessions.UserUUID = t1.UserUUID 
                WHERE
                        sg_djsessions.CreatedAt LIKE '{}%' -- and t1.UserUUID = 'D5D1A58FA4EC4948A86C04D9E2EE21E7'
                        
                GROUP BY
                        t1.UserUUID 
                HAVING
                        count( DISTINCT t1.date ) >= 7
                ) SELECT
                count( t2.UserUUID ) 
        FROM
                t2"""

rawsql_djreturn14 = """WITH t2 AS (
                WITH t1 AS (
                        SELECT DISTINCT
                                CAST( CreatedAt AS date ) AS date,
                                UserUUID 
                        FROM
                                original_social_graph.sg_djsessions 
                        WHERE
                                CAST( CreatedAt AS date ) <= '{}' 
                        ORDER BY
                                CreatedAt ASC 
                        ) SELECT
                        sg_djsessions.CreatedAt,
                        t1.UserUUID,
                        count( DISTINCT t1.date ) 
                FROM
                        t1
                        JOIN original_social_graph.sg_djsessions ON sg_djsessions.UserUUID = t1.UserUUID 
                WHERE
                        sg_djsessions.CreatedAt LIKE '{}%' -- and t1.UserUUID = 'D5D1A58FA4EC4948A86C04D9E2EE21E7'
                        
                GROUP BY
                        t1.UserUUID 
                HAVING
                        count( DISTINCT t1.date ) >= 14
                ) SELECT
                count( t2.UserUUID ) 
        FROM
                t2"""

rawsql_djreturn30 = """WITH t2 AS (
                WITH t1 AS (
                        SELECT DISTINCT
                                CAST( CreatedAt AS date ) AS date,
                                UserUUID 
                        FROM
                                original_social_graph.sg_djsessions 
                        WHERE
                                CAST( CreatedAt AS date ) <= '{}' 
                        ORDER BY
                                CreatedAt ASC 
                        ) SELECT
                        sg_djsessions.CreatedAt,
                        t1.UserUUID,
                        count( DISTINCT t1.date ) 
                FROM
                        t1
                        JOIN original_social_graph.sg_djsessions ON sg_djsessions.UserUUID = t1.UserUUID 
                WHERE
                        sg_djsessions.CreatedAt LIKE '{}%' -- and t1.UserUUID = 'D5D1A58FA4EC4948A86C04D9E2EE21E7'
                        
                GROUP BY
                        t1.UserUUID 
                HAVING
                        count( DISTINCT t1.date ) >= 30
                ) SELECT
                count( t2.UserUUID ) 
        FROM
                t2"""

today = date.today()
yesterday = date.today() - timedelta(1)
yesterday_2 = date.today() - timedelta(2)

value_1 = (rawsql_djreturn7.format(yesterday,today))
value_2 = (rawsql_djreturn14.format(yesterday,today))
value_3 = (rawsql_djreturn30.format(yesterday,today))

# print(value_1)
# print(value_2)
# print(value_3)