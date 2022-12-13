import sqlite3

dbname = input("\nEnter name for database (This is necessary to create a database or connect to an existing one. Enter without .db)\n\n>>> ")
db = sqlite3.connect(f"{dbname}.db")
cur = db.cursor()

def create_table(NameTable, One, Two, Three):
	cur.execute(f""" CREATE TABLE {NameTable} (
		{One} text,
		{Two} text,
		{Three} text
	)""")

def insert_table(entities):
	cur.execute(f"INSERT INTO {tablename} VALUES (?, ?, ?)", entities)

def delete_user(rowid):
	cur.execute(f"DELETE FROM {tablename} WHERE rowid = {rowid}")

def update_table(tablename, columnname, value, rowid):
	cur.execute(f"UPDATE {tablename} SET {columnname} = '{value}' where rowid = {rowid}")

def delete_table(tablename):
	cur.execute(f"DROP TABLE {tablename}")

def watch_table(tablename):
	cur.execute(f"SELECT * FROM {tablename}")
	all_results = cur.fetchall()
	print(all_results)

menu = input("\n1) Create table\n2) Insert table\n3) Delete line\n4) Update table\n5) Delete table\n6) Watch table\n\n>>> ")
	
if menu == "2":
	tablename = input("\nEnter table name: ")
	onecol = input("First column: ")
	twocol = input("Second column: ")
	threecol = input("Third column: ")
	entities = (onecol, twocol, threecol)
	insert_table(entities)

elif menu == "3":
	tablename = input("\nEnter table name: ")
	rowid = input("Enter id: ")
	delete_user(rowid)

elif menu == "1":
	NameTable = input("\nEnter table name: ")
	One = input("Enter name first column: ")
	Two = input("Enter name second column: ")
	Three = input("Enter name third column: ")
	create_table(NameTable, One, Two, Three)

elif menu == "4":
	tablename = input("\nEnter table name: ")
	columnname = input("Enter column name: ")
	value = input("Enter value: ")
	rowid = input("Enter id: ")
	update_table(tablename, columnname, value, rowid)

elif menu == "5":
	tablename = input("\nEnter table name: ")
	warning = input("\nRight?\n1) Yes\n2) No\n\n>>> ")
	if warning == "1":
		delete_table(tablename)
	elif warning == "2":
		exit()
elif menu == "6":
	tablename = input("\nEnter table name: ")
	watch_table(tablename)

db.commit()
db.close()
