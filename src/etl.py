import duckdb

duckdb.sql("""select column0 as station,
           min(column1) as temp_min,
           max(column1) as temp_max,
           avg(column1) as temp_med
           from read_csv("../data/measurements.txt", sep=";")
           group by station 
           order by station
            """).show()