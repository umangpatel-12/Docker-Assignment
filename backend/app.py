from flask import Flask, request, jsonify ,render_template
from business import getData

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
    data = getData()

    data = {
        "data": data
    }

    return jsonify(data)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000,debug=True)