# type: ignore
"""
Documentação do selenium
https://selenium-python.readthedocs.io/locating-elements.html
"""

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
MSEDGEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'edgedriver' / 'msedgedriver.exe'


def make_edge_browser(*options: str) -> webdriver.Edge:
    edge_options = webdriver.EdgeOptions()

    if options is not None:
        for option in options:
            edge_options.add_argument(option)  # type: ignore

    edge_service = Service(
        executable_path=str(MSEDGEDRIVER_EXEC),
    )

    browser = webdriver.Edge(
        service=edge_service,
        options=edge_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Opções para serem usadas no chrome e no edge, ja que o navegador edge usa o mesmo motor que o chrome
    # Essa opções mudam o comportamento do seu navegador durante os teste
    # Exemplo: --headless, realiza o teste em segundo plano ou seja nada na tela será exibido e mesmo assim é executado
    # https://peter.sh/experiments/chromium-command-line-switches/

    options = ()
    browser = make_edge_browser(*options)

    browser.get('https://www.google.com/')

    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    search_input.send_keys('Victor')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[5].click()

    time.sleep(TIME_TO_WAIT)
