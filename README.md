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
O Genroom é uma plataforma robusta para o gerenciamento eficiente de salas. 
Aqui estão as funcionalidades chave que foram implementadas:


Funcionalidades Implementadas
O Genroom é uma plataforma robusta para o gerenciamento eficiente de salas. Aqui estão as funcionalidades chave que foram implementadas:

* Visão Geral das Salas: Capacidade de listar todas as salas disponíveis na plataforma.
* Insights Detalhados: Fornece informações detalhadas de uma sala específica, incluindo características e sua disponibilidade.
* Criação de Espaço: Permite aos usuários criar novas salas conforme as necessidades.
* Gestão de Reservas: Funcionalidade para reservar salas para eventos específicos e também para liberá-las após o uso.
* Monitoramento em Tempo Real: Listagem instantânea de todas as salas que estão atualmente ocupadas.
* Eventos e Programações: Capacidade de criar, visualizar, editar e excluir eventos específicos associados a uma sala.
