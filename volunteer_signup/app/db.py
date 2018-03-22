import sqlite3

database_file = "static/web-site.db"

def create_db():
    # All your initialization code
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Create and populate your database tables. Here's an example to get you started.
    cursor.execute("drop table if exists table1")
    cursor.execute("create table if not exists table1("+
                   "column1 text primary key not null" +
                   ", column2 text not null" +
                   ", column3 int not null default 0)")
    cursor.execute("insert or ignore into table1 values ('value1', 'value2', 123)")

    # Create and populate your database tables. Here's an example to get you started.
    cursor.execute("drop table if exists users")
    cursor.execute("create table if not exists users("+
                   "username text primary key not null" +
                   ", password text not null" +
                   ", firstname text not null" +
                   ", lastname text not null" +
                   ", email text not null" +
                   ", phone text not null)")
    cursor.execute("insert or ignore into users values ('admin', '1010', 'Joe', 'Jones', 'admin@example.com', '1234567890')")

# Create and populate your database tables. Here's an example to get you started.
    cursor.execute("drop table if exists volunteerhoursummary")
    cursor.execute("create table if not exists volunteerhoursummary("+
                   "column1 text primary key not null" +
                   ", column2 text not null" +
                   ", column3 int not null default 0)")
    cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")
    cursor.execute("insert or ignore into volunteerhoursummary values ('leiblingfach', 'scholade', 123)")

    cursor.execute("drop table if exists events")
    cursor.execute("create table if not exists events("+
                   "title text not null" +
                   ", description text not null" +
                   ", date text not null"+
                   ", id integer primary key autoincrement"+
                   ", credits int not null default 1)")
    cursor.execute("insert or ignore into events values ('Presentation 1', 'Give presentation to the rest of the club on a CS topic', '11/2/2017', null, 2)")

    cursor.execute("insert or ignore into events values ('Presentation 2', 'Give presentation', '11/9/2017', null, 3)")


    # Save (commit) the changes
    connection.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def read_table1(column1_value):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Retrieve a record from table1 whose column1 value matches the value passed to this function
    cursor.execute("select * from table where column='%s'" % (column1_value))
    row = cursor.fetchone()

    connection.close()

    return row[0]

def adduser(username, password, firstname, lastname, email, phone):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    sql = "insert or ignore into users values ('%s', '%s', '%s', '%s', '%s', '%s')" % (username, password, firstname, lastname, email, phone)
    cursor.execute(sql)
    connection.commit()
    connection.close()

def userexists(username):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("select * from users where username='%s'" % (username))
    rows = cursor.fetchall()
    print(rows)

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
    print(row)
    return (str(row[0]), ())

def update_table1(column1_value, column2_new_value):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Update the column2 value in table1 whose column1 value matches the value passed to this function
    cursor.execute("UPDATE table1 SET colum2='%s' WHERE column1='%s'" % (column2_new_value, column1_value))

    connection.close()

def change_password(username, old_password, new_password):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Try to retrieve a record from the users table that matches the username and password
    cursor.execute("select * from users where username='%s' and password='%s'" % (username, old_password))
    rows = cursor.fetchall()


    print (' username:%s, old_password:%s, new_password:%s' % (username, old_password, new_password))
    if len(rows) == 0:
        return "bad password"
    sql = "update users SET  password='%s' WHERE username='%s'" % (new_password, username)
    print (sql)
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

    print (rows)

    connection.close()

    return rows



def add_event (Title, description, date, credits) :
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("insert or ignore into events (title, description, date, credits) values ('%s', '%s', '%s', %d)" % (Title, description, date, credits) )
    connection.commit()
    connection.close()
