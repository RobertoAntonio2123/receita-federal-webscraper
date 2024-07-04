import concurrent.futures
import urllib.request
import time
import zipfile
import os

files = [
    ('https://dadosabertos.rfb.gov.br/CNPJ/Cnaes.zip', 'Cnaes.zip'),
    ('https://dadosabertos.rfb.gov.br/CNPJ/Empresas0.zip', 'Empresas0.zip'), 
    ('https://dadosabertos.rfb.gov.br/CNPJ/Empresas1.zip', 'Empresas1.zip')
    ]

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(filename)

start_time = time.monotonic()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(download_file, url, filename) for url, filename in files]
    for future in concurrent.futures.as_completed(results):
        pass

elapsed_time = time.monotonic() - start_time
print(f'resulatdo do download em segundos {elapsed_time:.2f}')
