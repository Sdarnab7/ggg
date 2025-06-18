from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/factorial')
def factorial():
    try:
        number = int(request.args.get('number', 0))
        if number < 0:
            return jsonify({'error': 'Negative number not allowed'}), 400
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return jsonify({'number': number, 'factorial': fact})
    except:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/')
def home():
    return 'Factorial API is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
