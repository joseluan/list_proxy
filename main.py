import requests
import threading
import re
import queue

#Bloquea do IP
pilha = queue.Queue()

max_page = 1
min_page = 1
numero_threads = 2
list_proxys = []

for id_page in range(min_page, max_page+1):
    pilha.put(id_page)
    
def save_proxys_in_page():
    try:
        #Apenas para que seja usado o mesmo cookie.
        #Uma alternativa é passar o headers na requests
        session = requests.session() 
        while not pilha.empty(): #Enquando a pilha não for vazia
            id_page = pilha.get()
            print('Capturando proxys da página: {}'.format(id_page))
            url = 'http://www.freeproxylists.net/?page={}'.format(id_page)
            response = session.get(url)
            response = response.content.decode('UTF-8')
            #Para melhorar o funcionamento do regex pode restringir onde ele é passado
            #No lugar da página toda apenas num trecho de html
            regex_proxys = re.compile(r'(?P<ip>\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})[^<]*</a>[^<]*</td><td[^>]*>\s*(?P<porta>\d+)\s*</td>[^<]*<td[^>]*>(?P<protocolo>[^<]+)</td>[^<]*<td[^>]*>[^<]*</td>[^<]*<td><img[^>]*>(?P<pais>[^<]*)</td>[^<]*<td>[^<]*</td>[^<]*<td>[^<]*</td>[^<]*<td[^>]*>(?P<uptime>[^<]*)', flags=re.DOTALL)            
            print(response)
            for proxy_match in regex_proxys.finditer(response):                
                list_proxys.append({
                    'ip': proxy_match.group('ip'),
                    'porta': proxy_match.group('porta'),
                    'protoloco': proxy_match.group('protocolo').strip(),
                    'pais': proxy_match.group('pais').strip(),
                    'uptime': proxy_match.group('uptime').strip(),
                })

        pilha.task_done()
    except Exception as e:
        print(e)


save_proxys_in_page()
# for id_thread in range(0, numero_threads+1):
#     process_thread = threading.Thread(target=save_proxys_in_page, args=())
#     process_thread.daemon = True
#     process_thread.start()

pilha.join()

print(list_proxys)