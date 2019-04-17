from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import csv
from database_stuff import *

app = Flask(__name__)
app.secret_key = '8Z5T#4ChdZu"488jRBs/)hI5BO=O/L'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():    
    if 'is_logged_in' not in session or not session['is_logged_in']:
        return render_template('landing.html')
    else:
        posts = get_posts(session['grade'])
        print session['grade']
        if session['is_admin']:
            posts = get_posts()
        return render_template('home.html', posts=posts, is_logged_in=session['is_logged_in'], first_name=session['first_name'])

@app.route('/post/<int:post_ID>', methods=['GET', 'POST'])
def post(post_ID=None, comment_body=None):
    post = get_post_by_ID(post_ID)
    comments = retrieve_comments(post_ID)
    if request.method == 'POST':
        make_comment(post_ID, request.form['comment_body'], session['first_name'], session['last_name'])
    return render_template('post.html', post=post, comments=comments, is_logged_in=session['is_logged_in'], first_name=session['first_name'], is_admin=session['is_admin'], post_ID=post_ID)

@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    is_logged_in = message = first_name = last_name = password = repeat_password = grade_level = email_address = ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        grade_level = request.form['grade_level']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        email_address = request.form['email_address']
        validate = valid_create_student(first_name, last_name,
                                        password, repeat_password,
                                        grade_level, email_address)
        is_logged_in = validate[0]
        message = validate[1]
    if 'is_logged_in' in session and session['is_logged_in']:
        return redirect(url_for('home'))
    if is_logged_in:
        return redirect(url_for('login'))
    return render_template('sign_up.html', message=message,
                           first_name=first_name, last_name=last_name,
                           password=password, repeat_password=repeat_password,
                           grade_level=grade_level, email_address=email_address,
                           is_logged_in=is_logged_in)

@app.route('/reset_pass', methods=['POST', 'GET'])
def reset_pass():
    message = ''
    if 'is_logged_in' not in session or not session['is_logged_in']:
        return redirect(url_for('home'))
    if request.method=='POST':
        validate = valid_reset_password(session['email_address'], 
                                        request.form['password'], 
                                        request.form['repeat_password'],
                                        request.form['new_password'])
        if validate[0]:
            return redirect(url_for('home'))
        message=validate[1]
    return render_template('reset_pass.html', message=message)

@app.route('/login', methods=['POST', 'GET'])
def login():
    message = email_address = password = ''
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']
        validate = valid_login_student(email_address, password)
        session['is_logged_in'] = validate[0]
        message = validate[1]
        if validate[0]:
            session['first_name'] = validate[2][0]
            session['last_name'] = validate[2][1]
            session['grade'] = validate[2][4]
            session['email_address'] = validate[2][5]
        session['is_admin'] = (validate[0] and email_address == 'kcastanos@stuy.edu')
    if 'is_logged_in' in session and session['is_logged_in']:
        print session['grade']
        return redirect(url_for('home'))
    return render_template('login.html', message=message,
                           email_address=email_address,
                           password=password)

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if ('is_logged_in' not in session or
       'is_admin' not in session or session['is_admin'] != True):
        return redirect(url_for('home'))
    delete_post_ID = request.args.get('delete_post_ID', -1)
    if delete_post_ID >= 0:
        delete_post(delete_post_ID)
    rollover = request.args.get('rollover', False)
    if rollover:
        student_rollover()
    if request.method == 'POST':
        grade_level = request.form['grade_level']
        grade_level = grade_level[:1].upper() + grade_level[1:]
        make_post(request.form['post_title'], 
           request.form['post_body'], session['first_name'], session['last_name'],
           grade_level)         
    posts = get_posts()
    return render_template('admin.html', posts=posts, is_logged_in=session['is_logged_in'], first_name=session['first_name'])

if __name__== '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
