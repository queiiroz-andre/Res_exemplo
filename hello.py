from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    name = user_data['name']
    cpf = user_data['cpf']
    phone = user_data['phone']

    user = {
        'name': name,
        'cpf': cpf,
        'phone': phone
    }

    users.append(user)

    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<string:cpf>', methods=['DELETE'])
def delete_user(cpf):
    for user in users:
        if user['cpf'] == cpf:
            users.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)
