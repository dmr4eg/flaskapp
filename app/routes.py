from flask import Flask, render_template, request, redirect, url_for, session
from app import app
from .data_manager import TemperatureDataManager

app.secret_key = 'mysecretkey'
data_manager = TemperatureDataManager()

@app.route('/')  # View function for endpoint '/'
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
        # Save user details and if successful:
        session['username'] = username
        return redirect(url_for('dashboardPage'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate credentials and if valid:
        session['username'] = username
        return redirect(url_for('dashboardPage'))
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
    count = int(request.form['numToDelete'])
    deleted_count = data_manager.delete_records(count)
    return redirect(url_for('dashboardPage'))

@app.route('/logout')
def logout():
    session.clear()  # This will remove all items in the session
    return redirect(url_for('loginPage'))