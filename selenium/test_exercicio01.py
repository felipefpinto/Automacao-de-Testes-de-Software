from pathlib import Path

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome():
    opcoes = Options()
    opcoes.add_argument("--headless=new")
    navegador = Chrome(options=opcoes)
    try:
        pagina = Path(__file__).resolve().with_name("exercicio01.html")
        navegador.get(pagina.as_uri())
        yield navegador
    finally:
        # Fecha o navegador mesmo se a abertura ou o teste falhar.
        navegador.quit()


def test_titulo_da_pagina(chrome):
    assert chrome.title == "Exercicio 01"


def test_paragrafo_por_tag_name(chrome):
    paragrafo = chrome.find_element(By.TAG_NAME, "p")
    assert paragrafo.text == "O conteudo do site vem aqui"


def test_paragrafo_por_css_selector(chrome):
    paragrafo = chrome.find_element(By.CSS_SELECTOR, "p.content")
    assert paragrafo.text == "O conteudo do site vem aqui"
    assert paragrafo.get_attribute("class") == "content"
