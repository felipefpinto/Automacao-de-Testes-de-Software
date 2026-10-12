# Exercício Behave — Multiplicação

A função escolhida é `multiplicar(primeiro, segundo)`, que retorna o produto de dois números. O exercício contém três cenários: números positivos, multiplicação por zero e número negativo.

## Arquivos

- `multiplicacao.py`: função que será testada.
- `features/multiplicacao.feature`: cenários em Gherkin.
- `tests/test_multiplicacao.py`: implementação dos passos Given, When e Then.
- `features/steps/passos_multiplicacao.py`: importa os passos para que o Behave os encontre.

O `.feature` foi colocado em `features/`, separadamente dos passos Python em `features/steps/`. O arquivo de implementação fica em `tests/`, conforme pedido na atividade, e é carregado pelo arquivo de passos. Não é um teste pytest: sua execução é feita pelo Behave.

## Execução

Abra o terminal na pasta extraída do projeto:

```console
python -m pip install -r requirements.txt
python -m behave --no-capture
```

Os textos dos decoradores correspondem aos textos dos cenários. O parâmetro `{valor:d}` recebe um número inteiro, inclusive negativo. `And` reutiliza o tipo Given do passo anterior. O objeto `context` compartilha os valores entre os passos do mesmo cenário. A verificação final usa `assert`.

## Relação com o código gerado pelo Behave

Quando os passos ainda não foram implementados, o Behave mostra modelos com `StepNotImplementedError`. Esses modelos são substituídos por atribuições ao `context`, chamada da função e comparação do resultado, como no arquivo `tests/test_multiplicacao.py` desta entrega.
