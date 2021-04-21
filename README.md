# list_proxy
Find proxys in freeproxylists.net

# configure o ambiente 
instale as dependencias que estão no arquivo requeriments.txt
* Selenium
* Requests
baixe o webdrive do chrome e cole na pasta do projeto
* https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/

# Iniciar o Crawler
O arquivo que funciona é o main_selenium.py, o main.py é feito com requests
porém o freeproxyslists bloqueia suas requisições por isso que usei o selenium.
Há chances de encontrar um bypass para usar a bibioteca requests.