from flask import Flask, render_template  # Importing the Flask module from the flask package  
 
app = Flask(__name__)  # Creating an instance of the Flask class  
 
@app.route('/')  # View function for endpoint '/'
def basePage():  
    return render_template("base.html")

@app.route('/r')  # View function for endpoint '/'
def registerPage():  
    return render_template("register.html")


# Starting a web application at 0.0.0.0.0:5000 with debug mode enabled  
if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)