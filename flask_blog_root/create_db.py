import sqlite3

with sqlite3.connect("fblog.db") as connection:
	conn = connection.cursor()

	#conn.execute("""CREATE TABLE key_info_posts
	#				(title TEXT, posts TEXT, views INT)
	#			""")

	conn.execute('INSERT INTO key_info_posts VALUES("First Dummy", "blahblahblah", 17)')
	conn.execute('INSERT INTO key_info_posts VALUES("Second Dummy", "blahblahblah", 12)')
	conn.execute('INSERT INTO key_info_posts VALUES("Third Dummy", "blahblahblah", 13)')
	conn.execute('INSERT INTO key_info_posts VALUES("Fourth Dummy", "blahblahblah", 11)')
