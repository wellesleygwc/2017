import sqlite3

database_file = "static/web-site.db"

def create_db():
    # All your initialization code
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Create and populate your database tables. Here's an example to get you started.
    # cursor.execute("drop table if exists table1")
    # cursor.execute("create table if not exists table1("+
    #                "column1 text primary key not null" +
    #                ", column2 text not null" +
    #                ", column3 int not null default 0)")
    # cursor.execute("insert or ignore into table1 values ('value1', 'value2', 123)")

    #
    # Users
    #
    cursor.execute("drop table if exists users")
    cursor.execute("create table if not exists users("+
                   "username text primary key not null" +
                   ", role text not null" +
                   ", password text not null" +
                   ", firstname text not null" +
                   ", lastname text not null" +
                   ", email text not null" +
                   ", phone text not null)")
    cursor.execute("insert or ignore into users values ('admin', 'Administrator', '1010', 'Joe', 'Jones', 'admin@example.com', '1234567890')")
    cursor.execute("insert or ignore into users values ('test', 'EventC', 'test', 'Roger', 'Rogers', 'roger@roger.net', '1234567890')")
    cursor.execute("insert or ignore into users values ('volunteerBeth', 'Volunteer', 'badPassword', 'Beth', 'Rogers', 'beth@rogers.net', '1234567890')")


    #
    # events
    #
    cursor.execute("drop table if exists events")
    cursor.execute("create table if not exists events("+
                   "title text not null" +
                   ", description text not null" +
                   ", date text not null"+
                   ", id integer primary key autoincrement"+
                   ", time text not null"+
                   ", credits int not null default 1"+
                   ", numvolunteers int not null default 1"+
                   ", creator text not null)")
    #cursor.execute("insert or ignore into events values ('Presentation 1', 'Give presentation to the rest of the club on a CS topic', '11/2/2017', null, 2, 20, 'admin')")
    #cursor.execute("insert or ignore into events values ('Presentation 2', 'Give presentation', '11/9/2017', null, 3, 20, 'admin')")

    #
    # signups
    #
    cursor.execute("drop table if exists signups")
    cursor.execute(
        """create table if not exists signups(
             event_id integer,
             username text not null,
             unique(event_id,username))""")
    cursor.execute("insert or ignore into signups values (1, 'admin')")

    cursor.execute("insert or ignore into events (title,description,date,time,credits,numvolunteers,creator) values ('Presentation 2', 'Give presentation', '11/9/2017', '2:00 PM', null, 3, 'admin')")


    # Save (commit) the changes
    connection.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def adduser(username, role, password, firstname, lastname, email, phone):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    sql = "insert or ignore into users values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (username, role, password, firstname, lastname, email, phone)
    cursor.execute(sql)
    connection.commit()
    connection.close()

def userexists(username):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("select * from users where username='%s'" % (username))
    rows = cursor.fetchall()

    connection.close()

    if len(rows)>0:
        return True
    else:
        return False


def checkuser(username, password):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("select password from users where username = '%s'" % username)
    row = cursor.fetchone()
    if not row:
        return ("There is not a user with that name")
    if str(row[0]) == password:
        return ("Congratulations")
    else:
        return("Incorrect password")

    connection.close()
    return (str(row[0]), ())

def getprofile (username):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("select username, firstname, lastname, email, phone, role from users where username= '%s'" % username)
    row = cursor.fetchone()
    return row


def change_password(username, old_password, new_password):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Try to retrieve a record from the users table that matches the username and password
    cursor.execute("select * from users where username='%s' and password='%s'" % (username, old_password))
    rows = cursor.fetchall()

    if len(rows) == 0:
        return "bad password"
    sql = "update users SET  password='%s' WHERE username='%s'" % (new_password, username)
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return "password changed"

def list_events():
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Retrieve all the events
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    connection.close()
    return rows

def volunteer(id, username):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("insert or ignore into signups (event_id, username) values ('%s', '%s')" % (id, username) )
    connection.commit()
    connection.close()

def get_event_availability(id):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT numvolunteers
                   FROM events 
                   WHERE id='%s' """ % (id) )
    needed = cursor.fetchone()

    cursor.execute("""SELECT count(*)
                   FROM signups 
                   WHERE event_id='%s' """ % (id) )
    filled = cursor.fetchone()
    connection.close()

    return needed[0]-filled[0]


def list_signups(event_id):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Retrieve all the events
    cursor.execute("SELECT username FROM signups WHERE event_id = %d" % (event_id))
    rows = cursor.fetchall()
    connection.close()

    return rows


def add_event (Title, description, date, time, credits, numvolunteers, creator) :
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("insert or ignore into events (title, description, date, time, credits, numvolunteers, creator) values ('%s', '%s', '%s', '%s', %d, %d, '%s')" % (Title, description, date, time, credits, numvolunteers, creator) )
    connection.commit()
    connection.close()


def delete_account(username):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE username = '%s'" % (username))

    connection.commit()
    connection.close()

#def change_credentials(username, new_email, ):
   # connection = sqlite3.connect(database_file)
    # cursor = connection.cursor()

    # Try to retrieve a record from the users table that matches the username and password
    # cursor.execute("select * from users where username='%s' and password='%s'" % (username, old_password))
    # rows = cursor.fetchall()


    # print (' username:%s, old_password:%s, new_password:%s' % (username, old_password, new_password))
    # if len(rows) == 0:
    #     return "bad password"
    # sql = "update users SET  password='%s' WHERE username='%s'" % (new_password, username)
    # print (sql)
    # cursor.execute(sql)
    # connection.commit()
    # connection.close()
    # return "password changed"

    #
    # volunteerhoursummary
    #
    # cursor.execute("drop table if exists volunteerhoursummary")
    # cursor.execute("create table if not exists volunteerhoursummary("+
    #                "column1 text primary key not null" +
    #                ", column2 text not null" +
    #                ", column3 int not null default 0)")
    # cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    # cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    # cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    # cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    # cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")


#
# Example of reading a table.
# To retrieve the information stored in a database, we use a "SELECT" statement:
#
# def read_table1(column1_value):
#     connection = sqlite3.connect(database_file)
#     cursor = connection.cursor()
#
#     # Retrieve a record from table1 whose column1 value matches the value passed to this function
#     cursor.execute("select * from table where column='%s'" % (column1_value))
#     row = cursor.fetchone()
#
#     connection.close()
#
#     return row[0]

#
# Example of updating a table.
# To edit and save the information stored in a database, we use an "UPDATE" statement:
#
# def update_table1(column1_value, column2_new_value):
#     connection = sqlite3.connect(database_file)
#     cursor = connection.cursor()
#
#     # Update the column2 value in table1 whose column1 value matches the value passed to this function
#     cursor.execute("UPDATE table1 SET colum2='%s' WHERE column1='%s'" % (column2_new_value, column1_value))
#     connection.commit()
#     connection.close()
