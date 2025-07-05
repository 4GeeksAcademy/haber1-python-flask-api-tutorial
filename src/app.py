from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/todos', methods=['GET', 'POST'])
def todos():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = 'Lista de todos'
        response_body['results'] = todos
        return response_body, 200
    if request.method == 'POST':
        data = request.json
        todos.append(data)
        response_body['message'] ='Todo agregado correctamente'
        response_body['results'] = todos
        return response_body, 201


@app.route('/todos/<int:position>', methods=['GET', 'PUT', 'DELETE'])
def todo(position):
    response_body = {}
    if position > len(todos):
        response_body['message'] = 'Posición fuera de rango'
        return response_body, 400
    if request.method == 'DELETE':
        del todos[position]
        response_body['message'] = f'This is the position to delete {position}'
        return response_body, 200
    response_body['message'] = 'El GET Y el PUT no esrtan defenidos aún'
    return response_body, 200
 

todos = [{'label': 'My firt task', 'done': False},
        {'label': 'My second task', 'done': False}]
same_data = {'name': 'Bobby',
              'lastname': 'Rixer'}


if __name__== '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
