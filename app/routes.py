from flask import render_template, request, redirect, url_for, session
from app import app, db
from .data_manager import TemperatureDataManager
from .models import Users
from werkzeug.security import check_password_hash

data_manager = TemperatureDataManager()

@app.route('/')
def basePage():
    return render_template("base.html")

@app.route('/register', methods=['GET', 'POST'])
def registerPage():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        dob = request.form['dob']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        if password != password_confirm:
            return "Passwords do not match", 400

        user = Users(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        session['username'] = username
        return redirect(url_for('dashboardPage'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            return redirect(url_for('dashboardPage'))
        return "Invalid username or password", 400
    return render_template("login.html")

@app.route('/dashboard')
def dashboardPage():
    last_record = data_manager.get_last_record()
    last_temp = last_record['temp'] if last_record else None
    last_timestamp = last_record['timestamp'] if last_record else None
    username = session.get('username', 'Guest')  # Default to 'Guest' if not found in session
    temperature_data = data_manager.get_data()  # Make sure this retrieves the latest data
    return render_template("dashboard.html", username=username, temperature_data=temperature_data, last_temp=last_temp, last_timestamp=last_timestamp)

@app.route('/delete', methods=['POST'])
def deleteRecords():
    try:
        num_to_delete = request.form.get('numToDelete', 0)
        if not num_to_delete:
            return "No number provided for deletion.", 400

        count = int(num_to_delete)
        if count <= 0:
            return "Number of records to delete must be positive.", 400

        manager = TemperatureDataManager()
        deleted_count = manager.delete_records(count)

        return redirect(url_for('dashboardPage'))
    except ValueError:
        return "Invalid input. Please enter a valid number.", 400

@app.route('/logout')
def logout():
    session.clear()  # This will remove all items in the session
    return redirect(url_for('loginPage'))
