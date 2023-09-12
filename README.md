# Genroom - Sistema de Gerenciamento de Salas para Faculdades
O Genroom é um sistema de gerenciamento de salas desenvolvido para instituições de ensino superior, como faculdades e universidades. Ele foi projetado para simplificar a administração e a reserva de salas de aula, tornando a experiência acadêmica mais eficiente e organizada.

### Leia Codedoc.md para melhor entendimento técnico da aplicação.

## Arquitetura de Camadas: Interface do Usuário, Lógica de Negócios e Armazenamento de Dados
O Genroom adota uma arquitetura de camadas que separa claramente as responsabilidades do sistema, garantindo uma organização eficaz. Cada camada possui um propósito específico:
### Interface do Usuário (Presentation)
Esta camada é responsável pela interação direta com os usuários. Ela fornece as rotas da API e, quando aplicável, a interface gráfica para que os usuários acessem e utilizem as funcionalidades do sistema.
### Lógica de Negócios (Application)
A camada de lógica de negócios contém a essência do sistema. Aqui, encontramos as regras de negócios, serviços de aplicação e transformações de dados. Ela atua como a ponte entre a interface do usuário e o armazenamento de dados, garantindo que as operações sejam executadas de acordo com as regras estabelecidas.
### Armazenamento de Dados (Domain/Infrastructure)
Nesta camada, residem os repositórios responsáveis por acessar e persistir os dados do sistema. No caso do Genroom, utilizamos um repositório em memória para simplificar o exemplo, mas, em um cenário real, isso poderia ser substituído por um banco de dados.

## Princípios de Projetos Aplicados
O desenvolvimento do Genroom foi guiado por importantes princípios de projeto para garantir um código organizado, modular e de fácil manutenção:
### Modularidade
O sistema foi dividido em módulos bem definidos, como os controladores, serviços e repositórios. Isso facilita a manutenção e o desenvolvimento de novas funcionalidades.
### Ocultação da Informação
As camadas são projetadas para minimizar o acoplamento e proteger a informação sensível. Cada camada conhece apenas a camada imediatamente inferior, reduzindo dependências desnecessárias.
### Independência Funcional
As camadas têm responsabilidades bem definidas, permitindo que as alterações em uma camada não afetem outras partes do sistema.
### Design Orientado a Domínio
O Genroom é modelado em torno do domínio de gerenciamento de salas, garantindo que o código reflita a realidade do problema a ser resolvido.
### Coerência e Coesão
Cada componente do sistema tem uma única responsabilidade, garantindo que o código seja coeso e que as partes relacionadas estejam próximas.

## Funcionalidades Implementadas
O Genroom implementa várias funcionalidades essenciais para o gerenciamento de salas:

* Listagem de todas as salas disponíveis.
* Detalhes de uma sala específica.
* Criação de novas salas.
* Reserva e liberação de salas.
* Listagem de salas ocupadas.


### Como Executar a Aplicação
Para executar a aplicação, siga as seguintes etapas:

### Iniciar o Servidor Python HTTP:
* Você inicia um servidor HTTP Python executando o comando python -m http.server 8000 a partir do diretório onde o seu arquivo index.html está localizado.

### Acessar o Frontend:
* - Abra um navegador da web e vá para http://localhost:8000/index.html.
* - Isso carregará a página da web (frontend) no navegador.

### Preencher o Formulário:
* No frontend, você preenche o formulário com informações sobre uma nova sala que deseja criar.
* - Os campos do formulário são: Nome da Sala, Tipo da Sala, Capacidade, Descrição e Categoria.

### Enviar a Solicitação:
* Quando você clica no botão "Criar Sala", o JavaScript captura os dados do formulário.

### Enviar uma Solicitação para o Backend:
* O JavaScript usa a função fetch para enviar uma solicitação POST para o backend Flask no endpoint create_room (por exemplo, http://localhost:5001/api/rooms).
* A solicitação inclui os dados do formulário em formato JSON.

### Backend Processa a Solicitação:
* O backend, que já tem o CORS configurado para permitir solicitações do frontend, recebe a solicitação.
* - Ele processa os dados recebidos, cria uma nova sala no banco de dados ou armazenamento e envia uma resposta de volta para o frontend.

### Frontend Recebe a Resposta:
* O frontend aguarda a resposta do backend.
* - Se a criação da sala for bem-sucedida, o frontend exibe uma mensagem de sucesso e limpa o formulário.
* Se ocorrer um erro, o frontend exibe uma mensagem de erro.
### exemplo: 
### criando uma sala via Front-end
![Screenshot_4](https://github.com/jcr04/Gen_room.py/assets/70778525/b87fe405-c0a7-4dde-a331-a28b5c4c6d19)
### serve backend retorna requisição ao armazanamento 
![Screenshot_5](https://github.com/jcr04/Gen_room.py/assets/70778525/fe153ec6-3639-4058-9f11-b87e92ac45c6)
![Screenshot_6](https://github.com/jcr04/Gen_room.py/assets/70778525/b02e3a75-0cac-4093-b118-e4a2e397d4d5)


