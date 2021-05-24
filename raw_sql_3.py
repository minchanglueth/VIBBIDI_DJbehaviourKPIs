from datetime import date, timedelta

#những queries có thể 1 số ngày không có giá trị
rawsql_videocontribute = """WITH t1 AS ( SELECT DISTINCT UserUUID FROM original_social_graph.sg_djsessions dj ) SELECT DISTINCT
        CAST( pl.CreatedAt AS date ),
        count( pl.id ) 
        FROM
            v4.pointlogs pl
            JOIN t1 ON t1.UserUUID = pl.Userid 
        WHERE
            pl.CreatedAt > '2020-09-14' 
            AND pl.CreatedAt < '{}' 
            AND t1.UserUUID IS NOT NULL 
        GROUP BY
            CAST( pl.CreatedAt AS date ) ASC"""

rawsql_artistcontribute = """WITH t1 AS ( SELECT DISTINCT UserUUID FROM original_social_graph.sg_djsessions dj ) SELECT DISTINCT
        CAST( pl.CreatedAt AS date ),
        count( pl.id ) 
        FROM
            v4.pointlogs pl
            JOIN v4.users u ON u.Email = pl.info ->> '$.email'
            JOIN t1 ON t1.UserUUID = u.UUID 
        WHERE
            pl.CreatedAt > '2020-09-14' 
            AND pl.CreatedAt < '{}'
            AND t1.UserUUID IS NOT NULL 
            AND pl.ActionType = 'MA' 
        GROUP BY
            CAST( pl.CreatedAt AS date ) ASC"""

rawsql_albumcontribute = """WITH t1 AS ( SELECT DISTINCT UserUUID FROM original_social_graph.sg_djsessions dj ) SELECT DISTINCT
        CAST( pl.CreatedAt AS date ),
        count( pl.id ) 
        FROM
            v4.pointlogs pl
            JOIN v4.users u ON u.Email = pl.info ->> '$.email'
            JOIN t1 ON t1.UserUUID = u.UUID 
        WHERE
            pl.CreatedAt > '2020-09-14' 
            AND pl.CreatedAt < '{}'
            AND t1.UserUUID IS NOT NULL 
            AND pl.ActionType = 'MAA' 
        GROUP BY
            CAST( pl.CreatedAt AS date ) ASC"""