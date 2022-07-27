from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

#сохраняем данные в переменную jdata
jdata = {
    'first': {'Russia': 'Moscow'}
}

#время записи сохраняем в переменную jdata_time
jdata_time = {'first': 'by default'}


#обрабатываем get запрос
@app.route('/show/<string:key>', methods=['GET'])
def get_key(key):
    if key in jdata:
        return jsonify({'value': jdata[key], 'timestamp': jdata_time[key]})
    else:
        return jsonify({'value': None})

#обрабатываем post запрос
@app.route('/save/<string:key>', methods=['POST'])
def post_key(key):
    if not request.json:
        return jsonify({'error': 'json not found'})
    else:
        jdata[key] = request.get_json()
        jdata_time[key] = datetime.timestamp(datetime.now())
        return jsonify(jdata)

#обрабатываем del запрос
@app.route('/del/<string:key>', methods =['DELETE'])
def del_key(key):
    if key in jdata:
        del jdata[key]
        return jsonify(jdata)
    else:
        return jsonify({'error': 'key not found'})

if __name__ == '__main__':
    app.run(debug=True, port = 5000, host = '127.0.0.1')