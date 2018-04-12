import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db="laravel_shop")

myCurr = conn.cursor()

myCurr.execute(
	"""CREATE TABLE names
	(
		id int primary key,
		name varchar(20)
	)
	"""
)

conn.commit()

conn.close()