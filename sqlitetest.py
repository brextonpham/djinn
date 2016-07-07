# #!/usr/bin/python

# import sqlite3

# conn = sqlite3.connect('djinn_tables_v0.db')
# print "Opened database successfully";

# conn.execute('''CREATE TABLE USERS
#        (ID INT PRIMARY KEY     NOT NULL,
#        FIRST_NAME     TEXT    NOT NULL,
#        LAST_NAME      TEXT    NOT NULL,
#        EMAIL		  TEXT    NOT NULL,
#        NO_TEAMS       INT     NOT NULL);''')


# print "Table created successfully";

# conn.close()

import sqlite3

conn = sqlite3.connect('djinn_tables_v0.db')
print "Opened database successfully";

conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (1, 'Jake', 'Byman', 'jbyman@slack-corp.com', 2 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (2, 'Ananya', 'Chandra', 'ananyac@slack-corp.com', 3 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (3, 'Marc', 'Nolan', 'mnolan@slack-corp.com', 1 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (4, 'Meghana', 'Rao', 'mrao@slack-corp.com', 2 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (5, 'Eni', 'Asebiomo', 'easebiomo@slack-corp.com', 3 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (6, 'Jackie', 'Wibowo', 'jwibowo@slack-corp.com', 4 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (7, 'Divya', 'Saini', 'dsaini@slack-corp.com', 2 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (8, 'Jenny', 'Lu', 'jlu@slack-corp.com', 1 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (9, 'Brexton', 'Pham', 'bpha,@slack-corp.com', 3 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (10, 'Josh', 'Wills', 'jwills@slack-corp.com', 2 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (11, 'Stewart', 'Butterfield', 'sbutterfield@slack-corp.com', 2 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (12, 'Cal', 'Henderson', 'chendersonslack-corp.com', 1 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (13, 'Erica', 'Engle', 'eengle@slack-corp.com', 2 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (14, 'Anthony', 'Williams', 'awilliams@slack-corp.com', 3 )");
conn.execute("INSERT INTO USERS (ID,FIRST_NAME,LAST_NAME,EMAIL,NO_TEAMS) VALUES (15, 'Shashank', 'Bhargava', 'sbhargava@slack-corp.com', 2 )");

conn.commit()
print "Records created successfully";
conn.close()