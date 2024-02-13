from flask import Flask, render_template, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/')
def index():
    data_from_script = get_data_from_script()
    return render_template('index.html', data=data_from_script)

@app.route('/api/data', methods=['GET'])
def api_data():
    data_from_script = get_data_from_script()
    color = color_from_script()

    return jsonify({"data": data_from_script, "color": color})

def get_data_from_script():
    target = '192.168.1.200'
    try:
        subprocess.run(['ping', '-c', '1', target], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return f"{target} is up"
    except subprocess.CalledProcessError:
        return f"{target} is down"

def color_from_script():
    target = '192.168.1.200'
    try:
        subprocess.run(['ping', '-c', '1', target], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "green"
    except subprocess.CalledProcessError:
        return "red"

if __name__ == '__main__':
    app.run(debug=True)