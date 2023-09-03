# Documentação de código

## Room Service (room_service.py)
O módulo room_service.py contém a implementação dos serviços relacionados às salas.

### Classe RoomService
A classe RoomService fornece métodos para gerenciar as salas.

Método get_all_rooms()
Este método retorna todas as salas disponíveis.

* Retorno: Uma lista de objetos Room representando as salas.
Método create_room(name, room_type)
Este método cria uma nova sala com um nome e um tipo especificado.

* Parâmetros:
* - name (str): O nome da sala.
* - room_type (str): O tipo da sala.
* Retorno: Um objeto Room representando a sala recém-criada.

Método reserve_room(room_id)
Este método reserva uma sala com base em seu ID.

* Parâmetros:
* - room_id (str): O ID da sala a ser reservada.
* Retorno: Um objeto JSON contendo detalhes da sala reservada.

Método get_room_details(room_id)
Este método retorna os detalhes de uma sala com base em seu ID.

* Parâmetros:
* - room_id (str): O ID da sala cujos detalhes estão sendo solicitados.
* Retorno: Um objeto JSON contendo os detalhes da sala.

Método delete_room(room_id)
Este método exclui uma sala com base em seu ID.

* Parâmetros*:
* - room_id (str): O ID da sala a ser excluída.
* Retorno: Um valor booleano indicando se a sala foi excluída com sucesso.

Método get_available_rooms()
Este método retorna todas as salas disponíveis que não estão ocupadas.

Retorno: Uma lista de objetos Room representando as salas disponíveis.
Método update_room_name(room_id, new_name)
Este método atualiza o nome de uma sala com base em seu ID.

* Parâmetros*:
* - room_id (str): O ID da sala cujo nome deve ser atualizado.
* - new_name (str): O novo nome da sala.
* Retorno: Um objeto Room representando a sala com o nome atualizado.

Método get_rooms_by_type(room_type)
Este método retorna todas as salas de um tipo específico.

* Parâmetros*:
* - room_type (str): O tipo de sala a ser filtrado.
* Retorno: Uma lista de objetos Room representando as salas do tipo especificado.

## Room (room.py)
O módulo room.py define a classe Room, que representa uma sala.

### Classe Room
A classe Room representa uma sala com os seguintes atributos:

* id (str): O ID da sala.
* name (str): O nome da sala.
* room_type (str): O tipo da sala.
* is_occupied (bool): Indica se a sala está ocupada.
* reservations (list): Uma lista de reservas na sala.
* Método to_json()
* Este método converte um objeto Room em um dicionário JSON para facilitar a serialização.

Retorno: Um dicionário JSON contendo os atributos da sala.

## Room Repository (room_repository.py)
O módulo room_repository.py define o repositório de salas.

### Classe RoomRepository
A classe RoomRepository é responsável por armazenar e gerenciar as salas.

Método find_all()
Este método retorna todas as salas disponíveis.

- Retorno: Uma lista de objetos Room representando as salas.

Método find_by_id(id)
Este método encontra uma sala com base em seu ID.

* Parâmetros:
* id (str): O ID da sala a ser encontrada.
* Retorno: Um objeto Room representando a sala encontrada ou None se não for encontrada.

Método create_room(name, room_type)
Este método cria uma nova sala com um nome e um tipo especificado.

* Parâmetros:
* - name (str): O nome da sala.
* - room_type (str): O tipo da sala.
* Retorno: Um objeto Room representando a sala recém-criada.

## In-Memory Room Repository (in_memory_room_repository.py)
O módulo in_memory_room_repository.py implementa um repositório de salas em memória.

### Classe InMemoryRoomRepository
A classe InMemoryRoomRepository herda do RoomRepository e fornece uma implementação em memória para armazenar as salas.

Método find_all()
Este método retorna todas as salas disponíveis armazenadas em memória.

* Retorno: Uma lista de objetos Room representando as salas.

Método find_by_id(id)
Este método encontra uma sala com base em seu ID.

* Parâmetros:
* - id (str): O ID da sala a ser encontrada.
* Retorno: Um objeto Room representando a sala encontrada ou None se não for encontrada.

## Main (main.py)
O módulo main.py é o ponto de entrada da aplicação e configura o servidor Flask para disponibilizar os endpoints da API de salas.

Método __name__ == '__main__'
Este bloco de código inicia o servidor Flask quando o script é executado diretamente.

* Host: 0.0.0.0
* Porta: 5000
* Modo de Depuração: True (para depuração, você pode definir como False em produção)

## Endpoint da API

A API oferece os seguintes endpoints:

* /api/rooms (GET): Retorna todas as salas disponíveis.
* - ![Screenshot_3](https://github.com/jcr04/Gen_room.py/assets/70778525/e0fb7551-2564-4597-ab4f-80e4bc41d43b)
* /api/rooms (POST): Cria uma nova sala.
* - ![Screenshot_1](https://github.com/jcr04/Gen_room.py/assets/70778525/6676ecd9-26ec-4de0-8378-e0758951f81e)
* /api/rooms/<string:room_id>/reserve (POST): Reserva uma sala com base em seu ID.
* - ![Screenshot_2](https://github.com/jcr04/Gen_room.py/assets/70778525/72fa2c54-9d8b-4779-885e-6c9cd1860c00)
* /api/rooms/occupied (GET): Retorna todas as salas ocupadas.
* /api/rooms/<string:room_id> (GET): Retorna detalhes de uma sala com base em seu ID.
* - ![Screenshot_4](https://github.com/jcr04/Gen_room.py/assets/70778525/98471530-8c49-4133-b83f-8ed7de75eef2)

* /api/rooms/<string:room_id> (DELETE): Exclui uma sala com base em seu ID.
* /api/rooms/available (GET): Retorna todas as salas disponíveis que não estão ocupadas.
* /api/rooms/<string:room_id>/update-name (PUT): Atualiza o nome de uma sala com base em seu ID.
* /api/rooms/by-type/<string:room_type> (GET): Retorna todas as salas de um tipo específico.
* /api/rooms/<string:room_id>/reserve-by-period (POST): Reserva uma sala com base em seu ID durante um período especificado.

Lembre-se de que para utilizar a API, você deve executar o script main.py e acessar os endpoints conforme necessário.

## Executando o Projeto

Para executar o projeto, siga estas etapas:

* Certifique-se de ter o Python instalado em seu sistema.
* Instale as dependências do projeto executando pip install Flask.
* Execute o arquivo main.py com o comando python main.py.
* A API estará disponível em http://localhost:5000/api.

