from flask import Flask, render_template, request, jsonify  # Importing the Flask module from the flask package  
from app import app
 
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
        # Zde byste měli uložit uživatelské údaje do databáze
        return redirect(url_for('loginPage'))
    return render_template('register.html')

    # if request.method == 'POST':
    #     # Handle form submission here
    #     name = request.form['name']

    #     # Serialize the form data to JSON
    #     user_data = {
    #         'name': name,
    #         'email': email,
    #         'dob': dob,
    #         'password': password,
    #         'password_confirm': password_confirm
    #     }

    #     if not name or not email or not password:
    #         return "All fields are required", 400

    #     if password != password_confirm:
    #         return "Passwords do not match", 400

    #     # Assuming the registration is successful, you can redirect or render a success message
    #     return "Registration successful"
    #     # return jsonify(user_data)  # Return JSON response
        
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])  # View function for endpoint '/login'
def loginPage():  
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Zde byste měli ověřit přihlašovací údaje a nastavit session
        return redirect(url_for('dashboardPage'))
    return render_template("login.html")

@app.route('/dashboard')
def dashboardPage():   
    username = "User" 
    return render_template("dashboard.html", last_temp=last_temp, last_timestamp=last_timestamp, temperature_data=temperature_data, username=username)

@app.route('/delete', methods=['POST'])
def deleteRecords():
    num_to_delete = int(request.form['numToDelete'])
    del temperature_data[:num_to_delete]
    return render_template("dashboard.html", last_temp=last_temp, last_timestamp=last_timestamp, temperature_data=temperature_data)


# Starting a web application at 0.0.0.0.0:5000 with debug mode enabled  
