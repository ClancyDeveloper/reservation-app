📌 Projeto de Estudos – Sistema de Usuários, Clientes e Reservas

Este projeto é um estudo em Python que integra API, banco de dados e um aplicativo com interface gráfica.
O sistema permite gerenciar usuários, clientes e reservas, simulando um fluxo real de uma aplicação moderna.

🚀 Funcionalidades

Usuários

Criar e gerenciar usuários.

Cada usuário possui sua própria lista de clientes.

Clientes

Cada cliente pertence a um usuário.

Relacionamento 1 usuário → N clientes.

Reservas

Cada cliente pode criar várias reservas.

Cada reserva possui:

Nome da reserva

Descrição

Data/hora de criação

Data/hora de expiração

🛠️ Tecnologias Utilizadas

Python (linguagem principal)

Flask (API REST)

SQLAlchemy (ORM para o banco de dados)

SQLite

PyQt

Requests (comunicação do app com a API)