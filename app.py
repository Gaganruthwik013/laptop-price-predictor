from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("laptop_data.csv")

@app.route('/')
def index():
    companies = sorted(df['Company'].dropna().unique())
    return render_template('index.html', companies=companies)

@app.route('/get_cpus', methods=['POST'])
def get_cpus():
    company = request.json['company']
    cpus = sorted(df[df['Company'] == company]['Cpu'].dropna().unique())
    return jsonify(cpus)

@app.route('/get_rams', methods=['POST'])
def get_rams():
    company = request.json['company']
    cpu = request.json['cpu']
    rams = sorted(df[(df['Company'] == company) & (df['Cpu'] == cpu)]['Ram'].dropna().unique())
    return jsonify(rams)

@app.route('/get_price', methods=['POST'])
def get_price():
    data = request.json
    company = data['company']
    cpu = data['cpu']
    ram = data['ram']

    filtered_df = df[(df['Company'] == company) & (df['Cpu'] == cpu) & (df['Ram'] == ram)]

    if not filtered_df.empty:
        price = round(filtered_df['Price'].mean(), 2)
    else:
        price = "No match found."

    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
