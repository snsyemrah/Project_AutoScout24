import psycopg2

conn = psycopg2.connect(
    host= 'localhost',
    database = 'autoscout24',
    user = 'postgres',
    password = '1234')

cur = conn.cursor()

creat_script = '''CREATE TABLE IF NOT EXISTS autos (
	"id" serial NOT NULL,
	"model" varchar(255),
	"kilometer" varchar(255),
	"city" varchar(255),
	"year" varchar(255),
	"price" varchar(255),
	"plate" varchar(255),
	CONSTRAINT "main_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
'''
cur.execute(creat_script)
conn.commit()