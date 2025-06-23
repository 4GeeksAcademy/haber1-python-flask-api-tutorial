from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/todos',methods=['GET'])
def hello_world():
    return jsonify(todos)

todos = [{'label': 'My firt task', 'done': False},
        {'label': 'My second task', 'done': False}]
same_data = {'name': 'Bobby',
              'lastname': 'Rixer'}


if __name__== '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
