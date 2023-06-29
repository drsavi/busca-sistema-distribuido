# Projeto de Busca Distribuída

Este é um projeto de busca distribuída utilizando Flask e MongoDB. O objetivo é permitir a busca de registros em um conjunto de servidores, onde cada servidor instanciado possui seu próprio banco de dados MongoDB. Os servidores são conectados em uma topologia de vizinhança, realizando uma busca em largura, permitindo que a busca seja encaminhada aos vizinhos em caso de não encontrar o registro localmente.

## Pré-requisitos

```sh
    Python 3.x
    MongoDB
```

## Configuração do Projeto
Em seguida, instale as dependências do projeto:

```sh
    python -m pip install flask
    python -m pip install pymongo
    python -m pip install requests
```

Certifique-se de ter um servidor MongoDB rodando na sua máquina

## Configuração do MongoDB
1. Instale o MongoDB em sua máquina de acordo com as instruções específicas para o seu sistema operacional. Você pode encontrar mais informações em: 
[MongoDB - Documentação Oficial](https://www.mongodb.com/docs/manual/installation/)

2. Inicie o servidor MongoDB localmente.

3. Crie quatro bancos de dados no MongoDB chamados: 
```sh
    airbnb10
    airbnb11
    airbnb12
    airbnb13
```
4. Crie uma coleção chamada listingsAndReviews em cada um dos bancos de dados recém-criados.

5. Inserir registros em cada coleção listingsAndReviews. Segue abaixo o link de uma base de dados de registros do Airbnb: 

[Airbnb - Registros](https://github.com/neelabalan/mongodb-sample-dataset/blob/main/sample_airbnb/listingsAndReviews.json)

## Uso

1. Clone o repositório para sua máquina local:
```sh
    https://github.com/drsavi/busca-sistema-distribuido
```

2. Navegue até o diretório do projeto:
```sh
    cd busca-sistema-distribuido
```

2. Execute os arquivos `server.py` para iniciar a API Flask.

```sh
python server10.py
python server11.py
python server12.py
python server13.py
```

## API

Certifique-se de que cada servidor esteja sendo executado em uma porta diferente, conforme especificado no arquivo vizinhos.json.

Agora, você pode acessar as seguintes URLs para obter informações dos servidores de vizinhança.

Substitua <id> pelo ID desejado e <neighbor_id> pelo ID do vizinho para obter as informações correspondentes.

Exemplo de uso:


```sh
http://localhost:8000/get_data?_id=<id>&neighbor_id=<neighbor_id>
http://localhost:8001/get_data?_id=<id>&neighbor_id=<neighbor_id>
http://localhost:8002/get_data?_id=<id>&neighbor_id=<neighbor_id>
http://localhost:8003/get_data?_id=<id>&neighbor_id=<neighbor_id>

http://localhost:8000/get_data?_id=11945972&neighbor_id=10
```


#### Resposta:


```json
{
    "_id":"11945972",
    "etc":"etc"
}
```