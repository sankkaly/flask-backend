from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(
        {"message":"This is Home Page"}
        )

@app.route('/settings')
def settings():
    return jsonify(
        {"message":"This is settings page"}
    )

@app.route('/login')
def login():
    return jsonify(
        {"message":"This is login page"}
    )

@app.route('/dashboard')
def dashboard():
    return jsonify(
        {"Message":"This are the dashboards"}
    )

if __name__ == "__main__" :
    app.run(debug=True)