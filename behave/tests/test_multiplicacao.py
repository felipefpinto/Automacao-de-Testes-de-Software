"""Passos Behave implementados para os cenários da multiplicação."""
from behave import given, when, then
from multiplicacao import multiplicar


@given("o primeiro valor será {valor:d}")
def primeiro_valor(context, valor):
    context.primeiro = valor


@given("o segundo valor será {valor:d}")
def segundo_valor(context, valor):
    context.segundo = valor


@when("executa a função de multiplicação")
def executar_multiplicacao(context):
    context.resultado = multiplicar(context.primeiro, context.segundo)


@then("a saída deverá ser o valor {esperado:d}")
def verificar_resultado(context, esperado):
    assert context.resultado == esperado, (
        f"Esperado: {esperado}; obtido: {context.resultado}"
    )
    print(f"{context.primeiro} x {context.segundo} = {context.resultado} — OK")
