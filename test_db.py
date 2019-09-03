import psycopg2

try:
	conn = psycopg2.connect(host = "localhost",
							port = "5432",
							database = "aidooit_login",
							user = "postgres",
							password = "postgres")

	print('Connection success!!!')
	# Print PostgreSQL version
	cursor = conn.cursor()
	cursor.execute("SELECT version();")
	record = cursor.fetchone()
	print("You are connected to - ", record,"\n")

	#Create table query
#	create_table_query = '''CREATE TABLE login_data
#			(id SERIAL PRIMARY KEY,
#			name TEXT NOT NULL,
#			mobile TEXT NOT NULL,
#			code TEXT NOT NULL);'''
#	cursor.execute(create_table_query)
#	conn.commit()
#	print('Table login_data created successfully!')

	#Insert in table
	insert_query = '''INSERT INTO login_data (name, mobile, code) VALUES (%s,%s,%s)'''
	values = ('Reinaldo J.', '+5353278865', 'ADr56*3S')
	cursor.execute(insert_query, values)
	conn.commit()
	count = cursor.rowcount
	print(count, "Record inserted to login_data table.")

except (Exception, psycopg2.Error) as error :
	print ("Error while connecting to PostgreSQL", error)

finally:
	#closing database connection.
	if(conn):
		cursor.close()
		conn.close()
		print("PostgreSQL connection is closed")
