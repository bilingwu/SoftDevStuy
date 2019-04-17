import sqlite3  # Database
import time
import os
import sys

from hashlib import sha512  # Hashing for Passwords
from uuid import uuid4  # Salting for Passwords

from re import search

database = os.path.dirname(os.path.realpath(__file__)) + "/backend"

# Student Database -------------------------------------------------------------------------------------------------------------------------------------------
"""
Student Database - Stores student's login information
+------------+-----------+----------+------+-------+-------+------------------+
| First Name | Last Name | Password | Salt | Grade | Email | Number of Logins |
+------------+-----------+----------+------+-------+-------+------------------+
| TEXT       | TEXT      | INT      | INT  | TEXT  | TEXT  | INT              |
+------------+-----------+----------+------+-------+-------+------------------+
"""

# Adds a student to the database
# Returns a list [Boolean, String]
# True if successful, False if unsuccessful
# String is a status message
def valid_create_student(first_name, last_name, password, repeat_password, grade, email):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS student_database (first_name TEXT, last_name TEXT, password INT, salt INT, grade TEXT, email TEXT, num_logins INT)'
    c.execute(q)
    q = 'SELECT email FROM student_database'
    users = c.execute(q)
    is_valid = valid_data(email, password, repeat_password, users)
    if not is_valid[0]:
        conn.close()
        return is_valid
    else:
        salt = uuid4().hex
        hash_password = sha512((password + salt) * 10000).hexdigest()
        q = 'INSERT INTO student_database (first_name, last_name, password, salt, grade, email, num_logins) VALUES (?, ?, ?, ?, ?, ?, ?)'
        c.execute(q, (first_name, last_name, hash_password, salt, grade, email, 0))
        q = 'SELECT * FROM student_database WHERE email = ?'
        # info = c.execute((email,)).fetchone()
        conn.commit()
        conn.close()
        return [True, ""]

def valid_data(email, password, repeat_password, users):
    emails = []
    for user in users:
        emails.append(user[0])
    if not email.endswith("@stuy.edu"):
        return [False, "Please use a stuy.edu email"]
    if email in emails:
        return [False, "Email is already used."]
    if password != repeat_password:
        return [False, "Passwords do not match."]
    if len(password) < 8:
        return [False, "Your password must be at least 8 characters long."]
    if not (search(r'\d', password) and search('[a-z]', password) and search('[A-Z]', password) and search(r'[!@#$%^*]', password)):
        return [False, "Your password must include a lowercase letter, an uppercase letter, a number, and at least one of the following symbols: '!@#$%^*'."]
    return [True, "Successfully logged in."]

# Validates a student logging in
# Returns a list [Boolean, String]
# True if successful, False if unsuccessful
# "Invalid info" if failed, First name if successful
def valid_login_student(email, password):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "student_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return [False, "-1"]
    q = 'SELECT password, salt FROM student_database WHERE email = ?'
    pepper_and_salt = c.execute(q, (email,)).fetchone()
    if pepper_and_salt and sha512((password + pepper_and_salt[1]) * 10000).hexdigest() == pepper_and_salt[0]:
        q = "UPDATE student_database SET num_logins=num_logins + 1 WHERE email = ?"
        c.execute(q, (email,))
        q = "SELECT * FROM student_database WHERE email = ?"
        info = c.execute(q, (email,)).fetchone()
        conn.close()
        return [True, '', info]
    conn.close()
    return [False, 'Invalid information! Please try again.', ()]
 
# Resets a student's password
# Returns a list [Boolean, String]
# True if successful, False if unsuccessful
# String is a status message
def valid_reset_password(email, password, repeat_password, new_password):
    if password != repeat_password:
        return [False, "Passwords don't match!"]
    if len(repeat_password) < 8:
        return [False, "Your password must be at least 8 characters long."]
    if not (search(r'\d', repeat_password) and search('[a-z]', repeat_password) and search('[A-Z]', repeat_password) and search(r'[!@#$%^*]', repeat_password)):
        return [False, "Your password must include a lowercase letter, an uppercase letter, a number, and at least one of the following symbols: '!@#$%^*'."]
    conn = sqlite3.connect(database)
    c = conn.cursor()
    is_valid = valid_login_student(email, password)
    if not is_valid[0]:
        conn.close()
        return [False, "Invalid Information! Please try again."]
    else:
        salt = uuid4().hex
        hash_password = sha512((new_password + salt) * 10000).hexdigest()
        q = 'UPDATE student_database SET salt = ? WHERE email = ?'
        c.execute(q, (salt, email,))
        q = 'UPDATE student_database SET password = ? WHERE email = ?'
        c.execute(q, (hash_password, email,))
        conn.commit()
        conn.close()
        return [True, ""]
        
def get_top_student_login():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'SELECT * FROM student_database ORDER BY num_logins DESC LIMIT 4;'
    c.execute(q)
    result = c.fetchall()
    return result[::-1]

# Rolls over student grades
# Returns nothing
def student_rollover():
    print "it happened"
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'SELECT * FROM student_database'
    c.execute(q)
    q = 'UPDATE student_database SET grade="alumni" WHERE grade="senior";'
    c.execute(q)
    q = 'UPDATE student_database SET grade="senior" WHERE grade="junior";'
    c.execute(q)
    q = 'UPDATE student_database SET grade="junior" WHERE grade="sophomore";'
    c.execute(q)
    q = 'UPDATE student_database SET grade="sophomore" WHERE grade="freshman";'
    c.execute(q)
    conn.commit()
    conn.close()


# Post Database -------------------------------------------------------------------------------------------------------------------------------------------
"""
Post Database - Stores Post information
+-------+------+-----+-----------+------------+-----------+---------+
| Title | Body | ID  | Timestamp | First Name | Last Name | Section |
+-------+------+-----+-----------+------------+-----------+---------+
| TEXT  | TEXT | INT | TEXT      | TEXT       | TEXT      | TEXT    |
+-------+------+-----+-----------+------------+-----------+---------+
"""

# Adds a post to the database
# Returns nothing
def make_post(title, body, first_name, last_name, section):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS posts (title TEXT, body TEXT, ID INT, timestamp TEXT, first_name TEXT, last_name TEXT, section TEXT)'
    c.execute(q)
    new_ID = get_next_post_ID()
    timestamp = time.strftime("%x %X")
    q = 'INSERT INTO posts (title, body, ID, timestamp, first_name, last_name, section) VALUES (?, ?, ?, ?, ?, ?, ?)'
    c.execute(q, (title, body, new_ID, timestamp, first_name, last_name, section))
    conn.commit()
    conn.close()

# Gets the posts from the database
# that satisfy the given criteria
# Note: start >= ID > end
#       posts are displayed FILO (first-in, last-out)
# Returns a list of the selected posts
def get_posts(section=None):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'SELECT * FROM posts'
    if section:
        q += ' WHERE section = ?'
        c.execute(q, (section,))
    else:
        c.execute(q)
    posts = c.fetchall()[::-1]
    return posts

def get_post_by_ID(ID):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c. execute('SELECT * FROM posts WHERE ID = ?', (ID,))
    post = c.fetchall()[0]
    return post

# Gets the next post ID
# Returns a non-negative integer
def get_next_post_ID():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'SELECT COUNT(*) FROM posts'
    num_rows = c.execute(q).fetchone()[0]
    return num_rows + 1

# Deletes the post with the given ID
# Returns nothing
def delete_post(ID):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'DELETE FROM posts WHERE ID = ?'
    c.execute(q, (ID,))
    conn.commit()
    conn.close()

# Comment Database -------------------------------------------------------------------------------------------------------------------------------------------
"""
Comment Database - Stores Comment information
+-----+------+------+------------+-----------+
| ID  | Body | Time | First Name | Last Name |
+-----+------+------+------------+-----------+
| INT | TEXT | TEXT | TEXT       | TEXT      |
+-----+------+------+------------+-----------+
"""

# Adds a post to the database
# Returns nothing
def make_comment(ID, body, first_name, last_name):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS comments (ID INT, body TEXT, time TEXT, first_name TEXT, last_name TEXT)'
    c.execute(q)
    comment_time = time.strftime("%x %X")
    q = 'INSERT INTO comments (ID, body, time, first_name, last_name) VALUES (?, ?, ?, ?, ?)'
    c.execute(q, (ID, body, comment_time, first_name, last_name))
    conn.commit()
    conn.close()

# Retrieves all comments from the database
# that are on the post with the given ID
# Returns a list of all the comments
def retrieve_comments(ID):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'SELECT * FROM comments WHERE ID = ?'
    c.execute(q, (ID,))
    return c.fetchall()

# Deletes all the comments from the database
# that are on the post with the given ID
# Returns nothing
def delete_comments(ID):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    q = 'DELETE FROM comments WHERE ID = ?'
    c.execute(q, (ID,))
    conn.commit()
    conn.close()
