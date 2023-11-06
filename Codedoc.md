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

## Main (main.py)
O módulo main.py é o ponto de entrada da aplicação e configura o servidor Flask para disponibilizar os endpoints da API de salas.

Método __name__ == '__main__'
Este bloco de código inicia o servidor Flask quando o script é executado diretamente.

* Host: 0.0.0.0
* Porta: 5001
* Modo de Depuração: True (para depuração, você pode definir como False em produção)

## Endpoint da API
### Requisições pelo Postman
* - ![Screenshot_10](https://github.com/jcr04/Gen_room.py/assets/70778525/d708c954-e4e7-415a-ae12-addb724f36c2)

A API oferece os seguintes endpoints:
### Room
* /api/rooms (GET): Retorna todas as salas disponíveis.
* - ![Screenshot_3](https://github.com/jcr04/Gen_room.py/assets/70778525/e0fb7551-2564-4597-ab4f-80e4bc41d43b)
* /api/rooms (POST): Cria uma nova sala.
* - ![Screenshot_9](https://github.com/jcr04/Gen_room.py/assets/70778525/876442c3-3033-4200-8797-4429206997cb)
* /api/rooms/<string:room_id>/reserve (POST): Reserva uma sala com base em seu ID.
* - ![Screenshot_16](https://github.com/jcr04/Gen_room.py/assets/70778525/2c6576db-eb8e-43ff-b6d0-9dc72a49b981)
* /api/rooms/occupied (GET): Retorna todas as salas ocupadas.
* - ![Screenshot_15](https://github.com/jcr04/Gen_room.py/assets/70778525/bc254d91-0672-4d2d-8fd7-c09844e4cd83)
* - ![Screenshot_16](https://github.com/jcr04/Gen_room.py/assets/70778525/941f07dd-a34b-44be-ab5d-4eae02e1b9f5)
* - ![Screenshot_17](https://github.com/jcr04/Gen_room.py/assets/70778525/efc219e0-e33f-4157-bcb9-cd2695a4c210)
* /api/rooms/<string:room_id> (GET): Retorna detalhes de uma sala com base em seu ID.
* - ![Screenshot_11](https://github.com/jcr04/Gen_room.py/assets/70778525/fcc8beb7-a2d0-484b-96fd-64a897269861)
* - ![Screenshot_12](https://github.com/jcr04/Gen_room.py/assets/70778525/4b324287-c89f-4802-a597-8fa47b1970f2)
* /api/rooms/<string:room_id> (DELETE): Exclui uma sala com base em seu ID.
* - ![Screenshot_7](https://github.com/jcr04/Gen_room.py/assets/70778525/ffade6f0-b184-4222-ab26-e11b862550a2)
* - ![Screenshot_8](https://github.com/jcr04/Gen_room.py/assets/70778525/d2a5c38c-854b-4694-80f8-98a0fb7017c3)
* /api/rooms/available (GET): Retorna todas as salas disponíveis que não estão ocupadas.
* - ![Screenshot_5](https://github.com/jcr04/Gen_room.py/assets/70778525/51bf0a09-8f7f-41e7-aa41-19ed0cc01d73)
* /api/rooms/<string:room_id>/update-name (PUT): Atualiza o nome de uma sala com base em seu ID.
* - ![Screenshot_13](https://github.com/jcr04/Gen_room.py/assets/70778525/33c0061d-cce3-41e2-8bce-3d4ce9ea99b8)
* - ![Screenshot_14](https://github.com/jcr04/Gen_room.py/assets/70778525/bdd4e4ae-0b34-44a4-b186-c97a410d0419)
* /api/rooms/by-type/<string:room_type> (GET): Retorna todas as salas de um tipo específico.
* - ![Screenshot_19](https://github.com/jcr04/Gen_room.py/assets/70778525/2116084d-1899-471b-8e4d-26d69a5380ed)
* /api/rooms/<string:room_id>/reserve-by-period (POST): Reserva uma sala com base em seu ID durante um período especificado.
* - ![Screenshot_18](https://github.com/jcr04/Gen_room.py/assets/70778525/eebe1038-8388-45b5-babc-df36208562a5)
  
## Events
* /api/events (POST) criar um Evento.
* - ![Screenshot_10](https://github.com/jcr04/Gen_room.py/assets/70778525/d51273b0-8205-4e76-9fc8-9c13d56616ff)
* /api/events (GET) Obter todos os eventos de todas as salas.
* - ![Screenshot_11](https://github.com/jcr04/Gen_room.py/assets/70778525/219925a1-bb68-4310-a2e3-82af1e8d7686)
* /api/rooms/<int:room_id>/events (PUT) Atualizar um Evento.
* - ![Screenshot_12](https://github.com/jcr04/Gen_room.py/assets/70778525/5d35be89-e42a-4c1d-8aee-5ffcae9c177d)
* /api/rooms/{room_id}/events (DELETE) Deletar Evento
* - ![Screenshot_13](https://github.com/jcr04/Gen_room.py/assets/70778525/fa178755-b0d4-478f-b941-4edb6968d64b)
* - ![Screenshot_14](https://github.com/jcr04/Gen_room.py/assets/70778525/aba26541-b959-4e8c-8ace-273fbaec930f)
* - ![Screenshot_15](https://github.com/jcr04/Gen_room.py/assets/70778525/d13846bf-1e32-4dcc-b775-7d27c16ac441)
* - ![Screenshot_16](https://github.com/jcr04/Gen_room.py/assets/70778525/497f969c-9e4c-4d97-b542-ef61c2f03fd2)

## Report
* /api/rooms/report (GET): Analise de dados
* - ![Screenshot_1](https://github.com/jcr04/Gen_room.py/assets/70778525/b3035ee2-60a0-46d0-8507-a282e4626de0)

Lembre-se de que para utilizar a API, você deve executar o script main.py e acessar os endpoints conforme necessário.

## Executando o Projeto

Para executar o projeto, siga estas etapas:

* Certifique-se de ter o Python instalado em seu sistema.
* Instale as dependências do projeto executando pip install Flask.
* Execute o arquivo main.py com o comando python main.py.
* A API estará disponível em http://localhost:5001/api.

### Executando o Postman:
#### Passo 1: Instalar o Postman

Se você ainda não tem o Postman instalado, pode baixá-lo e instalá-lo a partir do site oficial do Postman.

#### Passo 2: Iniciar o Postman

Após a instalação, inicie o Postman.

#### Passo 3: Criar uma Coleção

No Postman, as solicitações são organizadas em coleções. Vamos criar uma coleção para suas solicitações da GenRoom:

* Clique na guia "Coleções" no canto superior esquerdo.
* Clique em "Nova Coleção".
* Dê um nome para a coleção, por exemplo, "GenRoom API".
* Opcionalmente, você pode adicionar uma descrição.
* Clique em "Criar".

#### Passo 4: Adicionar uma Solicitação

Agora que temos uma coleção, vamos adicionar uma solicitação:

* Selecione a coleção "GenRoom API" que você acabou de criar.
* Clique no botão "Adicionar Solicitação".
* Dê um nome para a solicitação, por exemplo, "Obter Todas as Salas".
* No campo "Método", selecione o método HTTP apropriado para a solicitação, por exemplo, "GET".
* No campo "URL", insira a URL da sua API GenRoom local, por exemplo, "http://localhost:5001/rooms" (certifique-se de que o servidor GenRoom esteja em execução).
* Clique em "Salvar para GenRoom API".

#### Passo 5: Enviar a Solicitação

Agora que você tem uma solicitação configurada:

* Clique na solicitação que você acabou de criar ("Obter Todas as Salas").
* Clique no botão "Enviar".
* Você deve receber uma resposta da sua API GenRoom, que será exibida na parte inferior da janela do Postman.

#### Passo 6: Adicionar mais Solicitações (Opcional)

Você pode repetir o "Passo 4" para adicionar mais solicitações à sua coleção GenRoom API, como "Criar Nova Sala", "Reservar Sala" e assim por diante, dependendo de quantos endpoints sua API GenRoom possui.

### Passo 7: Exportar a Coleção (Opcional)

Se desejar, você pode exportar sua coleção GenRoom API para compartilhá-la com outros ou usá-la em outro local:

* Clique com o botão direito na coleção "GenRoom API" na barra lateral.
* Selecione "Exportar".
* Escolha um formato de exportação (geralmente JSON é uma boa escolha).
* Escolha o local onde deseja salvar o arquivo exportado.
* Clique em "Salvar".

### editando o postman

Coloque a requisição desejada, certifique-se de que a solicitação está configurada corretamente e que o método HTTP (por exemplo, GET, POST) e a URL (por exemplo, http://localhost:5001/api/rooms) estão configurados conforme necessário.

Clique na guia "Headers" (Cabeçalhos) na parte superior da solicitação no Postman.

Certifique-se de que você tenha um cabeçalho "Content-Type" configurado com o valor "application/json". Se não existir, adicione-o.
adicione no Body da requisição Raw e depois Json e adicione: 
{

}

algumas requisições vão precisar de um Body com mais detalhes, elas estão no print de cada requisição acima
