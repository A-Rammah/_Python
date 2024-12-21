from flask import Flask, request, jsonify, abort, render_template

app = Flask(__name__)

# conn ===> connection to DB

def get_user_from_db(user_id):
   pass

@app.route('/')
def home_page():
   return "Welcome to the Flask Lab!"

@app.route('/greet/<name>', methods=['GET', 'POST'])
def greet(name):
    if request.method == 'POST':
        return f"Hello {name}! Welcome to the Flask Lab."
    return f"Please add your name in the URL /greet/YourName." 

@app.route('/submit', methods=['POST'])
def submit_data():
 name = request.json.get('name')
 return f'Hello, {name}! Your form has been submitted.'

@app.route('/api/data')
def get_data():
   data = {
        "age": 28,
        "title": "Flask API data retrieved",
   }
   return jsonify(data)

@app.route('/search')
def search():
   query = request.args.get('query')
   return f'Search results for: {query}'

@app.route('/form/<name>')
def welcome(name):
   return render_template('welcome.html', name=name)

# @app.route('/user/<user_id>')
# def get_user_by_id():
#    user = get_user_from_db(user_id)
#    if user.isdigit():
    #   abort(404, description="User not found!")
    # return jsonify(user)

@app.errorhandler(404)
def page_not_found(error):
   return "This page does not exist. Please check the URL.", 404

if __name__ == '__main__':
    app.run(debug=True, port=8082)