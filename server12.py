from flask import Flask, request, jsonify
from pymongo import MongoClient
import requests
import json

app = Flask(__name__)

# Carregar as configurações do servidor e vizinhos
with open('server_config12.json') as config_file:
    config = json.load(config_file)
    server_id = config['id']
    port = config['port']
    mongo_uri = config['mongo_uri']
    database = config['database']
    neighbors = config['vizinhos']

# Conexão com o MongoDB
client = MongoClient(mongo_uri)
db = client[database]
collection = db['listingsAndReviews']

# Rota para receber as requisições
@app.route('/get_data', methods=['GET'])
def get_data():
    document_id = request.args.get('_id')
    neighbor_id = request.args.get('neighbor_id')
    
    data = collection.find_one({'_id': document_id})

    if data:
        return jsonify(data)

    # Utilizar busca em largura para encaminhar a requisição aos vizinhos
    max_forwarding = 3  # Limite máximo de encaminhamentos consecutivos
    forwarding_count = 0  # Contador de encaminhamentos

    queue = [(neighbor, forwarding_count + 1) for neighbor in neighbors]

    while queue:
        neighbor, level = queue.pop(0)
        neighbor_id = neighbor['id']
        neighbor_port = neighbor['port']
        neighbor_url = f"http://localhost:{neighbor_port}/get_data?_id={document_id}&neighbor_id={neighbor_id}"
        response = requests.get(neighbor_url)

        if response.status_code == 200:
            return response.json()

        if level < max_forwarding:
            forwarding_count += 1
            for n in neighbors:
                if n['id'] == neighbor_id:
                    queue.append((n, level + 1))

    return jsonify({'message': 'Registro não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=port)
