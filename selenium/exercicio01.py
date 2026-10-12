from pathlib import Path

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def main():
    # as_uri cria uma URL file:/// válida, inclusive em caminhos com espaços.
    pagina = Path(__file__).resolve().with_name("exercicio01.html").as_uri()
    opcoes = Options()
    opcoes.add_argument("--headless=new")
    chrome = Chrome(options=opcoes)
    try:
        chrome.get(pagina)

        # a) Título da página.
        print("Título:", chrome.title)

        # b) Conteúdo do parágrafo pelo nome da tag.
        paragrafo_tag = chrome.find_element(By.TAG_NAME, "p")
        print("TAG_NAME:", paragrafo_tag.text)

        # c) Conteúdo do parágrafo pelo seletor CSS solicitado.
        paragrafo_css = chrome.find_element(By.CSS_SELECTOR, "p.content")
        print("CSS_SELECTOR:", paragrafo_css.text)
    finally:
        chrome.quit()


if __name__ == "__main__":
    main()
