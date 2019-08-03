from task_lister import app,db,mail
from flask import render_template, redirect, url_for, flash, request, json
from task_lister.forms import RegistrationForm, LoginForm , TaskForm , ChangePass
from flask_login import current_user, login_user , logout_user, login_required, user_logged_in
from flask_mail import Message
from task_lister.models import User,Task
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash
from twilio.rest import Client

account_sid = "ACa6323d4f06e9409df6cfa4887ade3584"

auth_token  = "f1fbf972cb28c78908f58f8892f5fbe3"

client = Client(account_sid,auth_token)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Home")




@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid Username or Password")
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title = 'Login', form = form)          



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/register", methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, mob = form.mobile.data )
        user.set_password(form.password.data)
        msg = Message(subject = 'Welcome to Task Lister',recipients = [form.email.data], body = 'Welcome to Daily Task Lister '+form.username.data+'.\n This mail is to inform that you are successfully registered on Task Lister.\n Thank You!!!!',sender = 'developernil98@gmail.com')
        mail.send(msg)
        message = client.messages.create(to="+91"+form.mobile.data ,from_="+12509002936",body="Thank You for registering with Daily Task Lister!")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))        
    return render_template('register.html',title="Register", form=form)



@app.route('/user/<username>', methods = ['GET','POST'])
@login_required
def user(username):
    user = User.query.filter_by(username = username).first_or_404()
    task = Task.query.filter_by(user_id = user.id).all()
    return render_template('user.html',title = 'Welcome', tasks = task)



@app.route('/user/<username>/newtask',methods = ['GET','POST'])
def newtask(username):
    user = User.query.filter_by(username = username).first_or_404()
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(t_name = form.t_head.data, t_desc = form.t_body.data, user_id = user.id, ddate = form.ddate.data)
        db.session.add(task)
        db.session.commit()
        flash("Congrats!!!! Task Added !!!")
        return redirect(url_for('user', username = current_user.username))
    return render_template('newtask.html',title = 'New Task', form = form)   



@app.route("/deltask/<t_id>", methods = ['POST', 'GET'])
def deltask(t_id):
    task = Task.query.filter_by(id = t_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash("Task Deleted Succesfully")
    return redirect(url_for('user', username = current_user.username))


@app.route('/user/<username>/task/<t_id>')
def desc_task(username,t_id):
    task = Task.query.filter_by(id = t_id).first_or_404()
    return render_template('taskdetails.html',title = 'Details',task = task)


@app.route('/user/<username>/profile', methods = ['GET','POST'])
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = ChangePass()
    if form.validate_on_submit():
        old_pass = form.old_pass.data
        new_pass = form.new_pass.data
        if user.check_password(old_pass):
            user.password_hash = generate_password_hash(new_pass)
            db.session.commit()
            flash("Password Changed Successfully!!!")
            return redirect(url_for('user',username = username))
        else:
            flash("Old Password not Matching")
            return redirect(url_for('profile', username = username))      
    return render_template( 'profilesetting.html' ,title = 'Profile',form = form)


@app.route("/create_list")
@login_required
def create_list():
    return redirect(url_for('user', username = current_user.username))


@app.route("/about")
def about():
    return render_template('underconst.html',title = 'About')

@app.route("/feedback")
def feedback():
    return render_template('underconst.html',title = 'Feedback')
