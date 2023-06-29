# Projeto de Busca Distribuída

Este é um projeto de busca distribuída utilizando Flask e MongoDB. O objetivo é permitir a busca de registros em um conjunto de servidores, onde cada servidor instanciado possui seu próprio banco de dados MongoDB. Os servidores são conectados em uma topologia de vizinhança, realizando uma busca em largura, permitindo que a busca seja encaminhada aos vizinhos em caso de não encontrar o registro localmente.

## Configuração

Certifique-se de ter o Python 3.x instalado no seu sistema. Em seguida, instale as dependências do projeto:

```sh
    python -m pip install flask
    python -m pip install pymongo
    python -m pip install requests
```



## Uso
1. Clone o repositório para sua máquina local:



1. Execute os arquivos `server.py` para iniciar a API Flask.
```sh
python server.py
```

## API

Certifique-se de que cada servidor esteja sendo executado em uma porta diferente, conforme especificado no arquivo vizinhos.json.

Agora, você pode acessar as seguintes URLs para obter informações dos servidores de vizinhança.

Substitua <id> pelo ID desejado e <neighbor_id> pelo ID do vizinho para obter as informações correspondentes.

Exemplo de uso:

#### http://localhost:8000/get_data?_id=<id>&neighbor_id=<neighbor_id>
#### http://localhost:8001/get_data?_id=<id>&neighbor_id=<neighbor_id>
#### http://localhost:8002/get_data?_id=<id>&neighbor_id=<neighbor_id>
#### http://localhost:8003/get_data?_id=<id>&neighbor_id=<neighbor_id>


#### Resposta:

```json
{
  "database": "ID encontrado na database: airbnb2",
  "resultado": {
    "_id": "11945972",
    ...
  }
}
```

#### Caso o ID não seja fornecido:

```json
{
  "error": "ID nao fornecido"
}
```

#### Caso o ID não seja encontrado:

```json
{
  "error": "ID nao encontrado"
}
```

## Arquivo de configuração

- Certifique-se de que os servidores estejam configurados corretamente no arquivo vizinhos.json.
- Deve estar dentro de colchetes, pois o nosso algoritmo de busca acessa a posição na variável servidores.

#### Exemplo:

```json
[
  {
    "id": "server1",
    "port": 5000,
    "mongo_uri": "mongodb://localhost:27017",
    "database": "airbnb1",
    "neighbors": [
      {
        "id": "server2",
        "port": 5001,
        "mongo_uri": "mongodb://localhost:27017",
        "database": "airbnb2"
      },
      {
        "id": "server3",
        "port": 5002,
        "mongo_uri": "mongodb://localhost:27017",
        "database": "airbnb3"
      }
    ]
  }
]
```
