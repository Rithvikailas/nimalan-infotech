from flask import Flask, render_template, request
from image_generator import generate_coin_with_details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        company_name = request.form['company_name']
        coin_value = request.form['coin_value']
        # Generate the coin image based on form data
        generate_coin_with_details(radius=100, company_name=company_name, coin_value=coin_value)
        return "NFT generated successfully"

if __name__ == '__main__':
    app.run(debug=True)
