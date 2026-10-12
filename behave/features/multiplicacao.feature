Feature: Multiplicação
    Implementação da função que multiplica dois números.

    Scenario: Multiplicar dois números positivos
        Given o primeiro valor será 5
        And o segundo valor será 2
        When executa a função de multiplicação
        Then a saída deverá ser o valor 10

    Scenario: Multiplicar por zero
        Given o primeiro valor será 8
        And o segundo valor será 0
        When executa a função de multiplicação
        Then a saída deverá ser o valor 0

    Scenario: Multiplicar um número negativo
        Given o primeiro valor será -3
        And o segundo valor será 4
        When executa a função de multiplicação
        Then a saída deverá ser o valor -12
