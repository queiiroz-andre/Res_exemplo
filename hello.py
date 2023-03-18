from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
user_id = 1

@app.route('/users', methods=['POST'])
def create_user():
    global user_id
    user_data = request.get_json()
    name = user_data['name']
    cpf = user_data['cpf']
    phone = user_data['phone']

    user = {
        'id': user_id,
        'name': name,
        'cpf': cpf,
        'phone': phone
    }
    users.append(user)
    user_id += 1

    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'Usuário deletado!'})
    return jsonify({'message': 'Usuário não encontrado!'})

if __name__ == '__main__':
    app.run(debug=True)
