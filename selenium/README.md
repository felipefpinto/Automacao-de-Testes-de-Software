# Exercício 01 — Selenium

## Arquivos

- `exercicio01.html`: código fornecido no enunciado, salvo em UTF-8.
- `exercicio01.py`: abre o arquivo local e imprime, em sequência, o título e o conteúdo do parágrafo usando `By.TAG_NAME` e `By.CSS_SELECTOR` com `p.content`.
- `test_exercicio01.py`: três testes com `pytest`, verificando o título e o parágrafo pelos dois localizadores solicitados. Uma fixture abre a página para cada teste e fecha o navegador ao finalizar, mesmo em caso de falha.

## Como executar

É necessário ter Python e Google Chrome instalados. Abra o terminal na pasta destes arquivos:

```console
python -m pip install -r requirements.txt
python exercicio01.py
python -m pytest -v test_exercicio01.py
```

O Selenium Manager gerencia o driver do Chrome e pode precisar de internet na primeira execução. O navegador roda em modo headless (sem janela); remova a linha `opcoes.add_argument("--headless=new")` nos dois scripts se quiser exibir a janela.

## Saída esperada do script

```text
Título: Exercício 01
TAG_NAME: O conteúdo do site vem aqui
CSS_SELECTOR: O conteúdo do site vem aqui
```

Quando os três testes passarem, o pytest exibirá `3 passed`. Isso descreve o resultado esperado, não uma execução comprovada.

## Observações

O HTML foi mantido conforme o enunciado, inclusive o `</form>` sem abertura correspondente. O navegador normalmente ignora esse fechamento solto. Em uma página nova, o ideal é removê-lo e incluir `head` e `meta charset="utf-8"`.

Embora o enunciado use “teste de unidade”, testes com Selenium que abrem um navegador são testes de interface. Aqui, `pytest` é o framework usado para organizar as verificações.

## Verificação nesta entrega

A sintaxe dos dois scripts foi verificada com sucesso. O Selenium foi instalado, mas a execução do script parou na inicialização do Chrome com SessionNotCreatedException (Chrome failed to start: crashed / DevToolsActivePort). Por isso, os testes no navegador não foram confirmados neste ambiente.
