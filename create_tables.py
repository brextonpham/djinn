import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("INSERT INTO VILLAGES (ID,VILLAGE,COUNTRY,POPULATION,SALARY) VALUES (1,'Atlanta', 'U.S.', 20000.0, 1234 )");

conn.execute("INSERT INTO VILLAGES (ID,VILLAGE,COUNTRY,POPULATION,SALARY) VALUES (2,'San Francisco', 'U.S.', 15000.0, 12345 )");

conn.execute("INSERT INTO VILLAGES (ID,VILLAGE,COUNTRY,POPULATION,SALARY) VALUES (3,'Orlando', 'U.S.', 20000.0, 2384 )");

conn.execute("INSERT INTO VILLAGES (ID,VILLAGE,COUNTRY,POPULATION,SALARY) VALUES (4,'Los Angeles', 'U.S.', 65000.0, 18245 )");

conn.commit()
print "Records created successfully";
conn.close()