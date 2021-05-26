from flask import Flask, request, Response, json, jsonify

app = Flask("json")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)

@app.route('/add1', methods=['POST'])
def add1():
    result = {'sum': request.json['a'] + request.json['b']}
    res= Response(json.dumps(result),  mimetype='application/json')
    res.headers.add('Server', 'python flask')
    return  res


@app.route('/add2', methods=['POST'])
def jsonif():
    result = {'sum': request.json['a'] + request.json['b']}

    return  jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)