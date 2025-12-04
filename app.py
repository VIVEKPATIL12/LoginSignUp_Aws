from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Temporary in-memory "database"
users = {}

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        # Save user (in real apps, use a database + hashing)
        users[username] = password

        # Redirect to login page after signup
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        # Check credentials
        if username in users and users[username] == password:
            return f"Welcome, {username}! You are logged in."
        else:
            return "Invalid credentials. Try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
