## API Escola - Django REST Framework

![Static Badge](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## Descrição

Este projeto implementa uma API REST para gerenciar os dados de uma escola. A API, desenvolvida com Django REST Framework, fornece acesso a informações sobre estudantes, cursos e matrículas, além de permitir a autenticação básica para operações de escrita.

## Tecnologias Utilizadas

- Python 3
- Django
- Django REST Framework
- Django Basic Authentication

## Funcionalidades Detalhadas

**Recursos:**

- **Estudantes:** Consultar, adicionar, editar e remover estudantes.
- **Cursos:** Consultar, adicionar, editar e remover cursos.
- **Matrículas:** Consultar, adicionar, editar e remover matrículas.

**Funcionalidades Adicionais:**

- **Autenticação:** Utiliza Basic Authentication para proteger as rotas de escrita da API.
- **Serializers:** Implementa serializers para formatar os dados dos modelos em JSON.
- **Views:** Utiliza ModelViewSet para fornecer uma interface completa de CRUD para os recursos da API.
- **Listas Personalizadas:** Fornece endpoints para listar matrículas de um estudante específico e estudantes matriculados em um curso específico.
