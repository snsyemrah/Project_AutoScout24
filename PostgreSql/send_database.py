import psycopg2


conn = psycopg2.connect(host= 'localhost',database = 'autoscout24',user = 'postgres',password = '1234')
cur = conn.cursor()


cur.execute("copy autos (model,kilometer,city,year,price,plate,image) from 'C:\\Users\\ANKA\Desktop\\Project_AutoScout24\\Auto_Scrapy\\auto\\auto\\new.csv' delimiter ',' csv header")

conn.commit()

