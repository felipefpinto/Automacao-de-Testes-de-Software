"""AP2 — interação Selenium com formulário local; dados fictícios."""
import time
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    pasta = Path(__file__).resolve().parent
    navegador = webdriver.Chrome()
    navegador.set_window_size(1440, 1100)
    try:
        navegador.get((pasta / "avaliacao.html").as_uri())
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, "nome")))

        navegador.find_element(By.ID, "nome").send_keys("Marina Costa")
        time.sleep(0.8)
        navegador.find_element(By.NAME, "ra").send_keys("2026001234")
        time.sleep(0.8)
        navegador.find_element(By.ID, "dia").send_keys("15")
        time.sleep(0.8)
        navegador.find_element(By.CSS_SELECTOR, "input[name='mes']").send_keys("8")
        time.sleep(0.8)
        navegador.find_element(By.NAME, "ano").send_keys("2002")
        time.sleep(0.8)
        Select(navegador.find_element(By.ID, "curso")).select_by_value("ads")
        time.sleep(0.8)
        Select(navegador.find_element(By.NAME, "aproveitamento")).select_by_visible_text("9")
        time.sleep(0.8)
        navegador.find_element(By.CSS_SELECTOR, "textarea#sugestoes").send_keys(
            "Mais exercícios práticos com Selenium e projetos em equipe."
        )
        time.sleep(0.8)
        navegador.find_element(By.ID, "observacoes").send_keys(
            "As demonstrações em aula facilitaram o aprendizado."
        )
        time.sleep(0.8)
        if not navegador.save_screenshot(str(pasta / "print_formulario.png")):
            raise RuntimeError("Não foi possível salvar o print do formulário.")
        navegador.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(0.8)

        WebDriverWait(navegador, 10).until(EC.text_to_be_present_in_element(
            (By.ID, "resultado"), "Feedback enviado com sucesso!"
        ))
        mensagem = navegador.find_element(By.ID, "resultado").text
        assert "Marina Costa" in mensagem
        if not navegador.save_screenshot(str(pasta / "print_confirmacao.png")):
            raise RuntimeError("Não foi possível salvar o print de confirmação.")
        print(mensagem)
        print("Automação concluída. Prints salvos na pasta do projeto.")
        with ZipFile(pasta / "entrega_ap2_com_prints.zip", "w", ZIP_DEFLATED) as entrega:
            for nome in ("avaliacao.html", "automacao_avaliacao.py", "requirements.txt",
                         "LEIA-ME.txt", "print_formulario.png", "print_confirmacao.png"):
                entrega.write(pasta / nome, arcname=nome)
        print("Arquivo para entrega: entrega_ap2_com_prints.zip")
    finally:
        navegador.quit()


if __name__ == "__main__":
    main()
