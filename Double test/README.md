# Atividade — dois doublés de teste no cadastro de usuários

Projeto didático em Python inspirado na estrutura dos exemplos da Aula06. O tema foi adaptado para usuários com **nome, e-mail e telefone**. Os dados usados são fictícios.

## Classes da aplicação

- `Usuario`: representa os três campos do cadastro. Telefone é texto para preservar zeros e permitir sinais de formatação.
- `UsuarioRepositorio`: contrato abstrato com o método `inserir`.
- `UsuarioServico`: recebe o repositório por injeção de dependência e cadastra usuários. Os três campos são obrigatórios; campo vazio ou composto somente de espaços gera `ValueError` antes de chamar o repositório. A atividade não valida formatos de e-mail ou telefone.

## 1. Fake — UsuarioRepositorioFake

Implementa um repositório funcional em memória. Substitui o banco de dados por uma lista e permite inserir, listar e contar usuários. O teste cadastra Ana e Bruno pelo serviço real e verifica a quantidade e todos os campos dos registros. O foco é o **estado armazenado**.

## 2. Spy — UsuarioRepositorioSpy

Registra os objetos recebidos em cada chamada a `inserir`. O teste verifica duas chamadas, sua ordem e os argumentos recebidos. O foco são as **interações com a dependência**. As expectativas são verificadas depois da ação, no teste.

Embora ambos utilizem listas, elas têm papéis diferentes: no Fake, a lista é o armazenamento; no Spy, é o histórico das chamadas.

## Execução

Com Python 3.10 ou superior, abra o terminal nesta pasta e execute:

```console
python -m pip install -r requirements.txt
python -m pytest -v -s --color=no
```

São cinco casos: um para o Fake, um para as chamadas do Spy e três casos de campos obrigatórios (nome, e-mail e telefone). Os testes usam `assert` e `pytest.raises`; as mensagens são impressas somente após as verificações passarem. Não há acesso à rede ou banco de dados.

## Arquivos e resultados

- `src/`: classes da aplicação.
- `tests/`: classes dos dois doublés e testes.
- `resultados.txt`: saída real da execução.
- `resultados.png`: reprodução visual da saída real, para incluir na entrega; não é uma captura da interface do terminal.

Resultado obtido: **5 testes aprovados**.
