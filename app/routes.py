from flask import Flask, render_template, request, redirect, url_for, session
from app import app

app.secret_key = 'mysecretkey'
 
temperature_data = [
    {"timestamp": "2024-03-01 12:00:00", "temp": 20},
    {"timestamp": "2024-03-02 12:00:00", "temp": 22},
    {"timestamp": "2024-03-03 12:00:00", "temp": 18},
    {"timestamp": "2024-03-04 12:00:00", "temp": 21},
    {"timestamp": "2024-03-05 12:00:00", "temp": 19},
]
last_data = temperature_data[-1]
last_temp = last_data['temp']
last_timestamp = last_data['timestamp']

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
    username = session.get('username', 'Guest')  # Default to 'Guest' if not found in session
    return render_template("dashboard.html", username=username, last_temp=last_temp, last_timestamp=last_timestamp, temperature_data=temperature_data)

@app.route('/delete', methods=['POST'])
def deleteRecords():
    num_to_delete = int(request.form['numToDelete'])
    del temperature_data[:num_to_delete]
    return render_template("dashboard.html", last_temp=last_temp, last_timestamp=last_timestamp, temperature_data=temperature_data)

@app.route('/logout')
def logout():
    session.clear()  # This will remove all items in the session
    return redirect(url_for('loginPage'))