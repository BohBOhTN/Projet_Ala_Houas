from flask import Flask, render_template, jsonify
from scrape_data import get_finance_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/finance/<choice>')
def finance_choice(choice):
    message = f"You are interested in {choice}."
    finance_info = get_finance_info(choice)  # Assuming you have a function to fetch finance info
    return jsonify({'message': message, 'finance_info': finance_info})

if __name__ == '__main__':
    app.run(debug=True)
