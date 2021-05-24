from datetime import date, timedelta

#những queries để lấy ra toàn bộ column
rawsql_followers = """ SELECT
            #CAST( CreatedAt AS date ),
            count( FollowerUUID ) 
        FROM
            v4.sg_followers 
        WHERE
            CreatedAt > '2020-09-14'
            and CreatedAt < '{}'
        GROUP BY
            CAST( CreatedAt AS date ) ASC """

rawsql_blockers = """WITH t1 AS (
            SELECT DISTINCT
                CAST( b.CreatedAt AS date ) AS date,
                count( b.BlockerUUID ) AS blockers 
            FROM
                original_social_graph.sg_blocking b
                JOIN v4.users u ON u.UUID = b.BlockerUUID 
            WHERE
                b.CreatedAt >= '2020-11-30 13:06:41' 
                AND b.CreatedAt < '{}' 
            GROUP BY
                CAST( b.CreatedAt AS date ) 
            ) SELECT
            blockers 
        FROM
            t1 
        ORDER BY
            t1.date ASC"""

rawsql_videocollect = """WITH t1 AS ( SELECT DISTINCT UserUUID FROM original_social_graph.sg_djsessions dj ) 
        SELECT 
        #CAST( cd.CreatedAt AS date ),
        #count(DISTINCT cd.DataSourceId ),
        count(cd.DataSourceId)
        FROM
            t1
            JOIN v4.users u ON u.UUID = t1.UserUUID
            JOIN v4.collections c ON c.UserId = u.id
            JOIN v4.collection_datasource cd ON cd.CollectionId = c.UUID 
        WHERE
            cd.CreatedAt > '2020-09-14' 
            AND cd.CreatedAt < '{}' 
        GROUP BY
            CAST( cd.CreatedAt AS date ) ASC"""

rawsql_artistcollect = """with t1 as (select DISTINCT UserUUID from original_social_graph.sg_djsessions dj)
        select 
        #DISTINCT CAST(c.CreatedAt as date), 
        count (c.EntityUUID) from t1
        join v4.sg_likes c on c.UserUUID = t1.UserUUID
        where c.CreatedAt > '2020-09-14' 
        and c.CreatedAt < '{}'
        and c.EntityType = 'Ar'
        GROUP BY  CAST(c.CreatedAt as date) ASC"""

rawsql_albumcollect = """with t1 as (select DISTINCT UserUUID from original_social_graph.sg_djsessions dj)
        select 
        #DISTINCT CAST(c.CreatedAt as date), 
        count (c.EntityUUID) from t1
        join v4.sg_likes c on c.UserUUID = t1.UserUUID
        where c.CreatedAt > '2020-09-14' 
        and c.CreatedAt < '{}' 
        and c.EntityType = 'Al'
        GROUP BY  CAST(c.CreatedAt as date) ASC"""