from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route - renders the frontend page
@app.route('/')
def home():
    return render_template('index.html')

# Example API route - handles data sent from frontend
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    bid = data.get('bid')
    
    # You can process/store this data (e.g., save to DB)
    print(f"Received bid: {name} - ₹{bid}")
    
    return jsonify({'message': f'Bid received from {name} for ₹{bid}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
