# coding: utf-8

import os
import requests
import pandas as pd

CACHE_DIR = 'cache'


os.makedirs(CACHE_DIR, exist_ok=True)


def download(name, query):
    '''
    Baixa os CSVs de uma query, agrupando e exportando todos para um único CSV.
    '''
    json_data = requests.get(query).json()
    resources = json_data['result']['results'][0]['resources']
    dfs = []
    print('>', name)
    for resource in resources:
        url = resource['url']

        # Evita processar arquivo de dicionário
        if resource['name'].startswith('Dicionário'):
            continue

        ano, periodo = (resource['name'].rpartition(' ')[-1]
                        .strip('.').split('.'))
        print('Processando', ano, periodo)
        filename = '%s_%s-%s.csv' % (name, ano, periodo)
        filepath = os.path.join(CACHE_DIR, filename)

        # Baixar se necessário
        if not os.path.exists(filepath):
            print('Baixando')
            print(url)
            content = requests.get(url).content
            with open(filepath, 'wb') as f:
                f.write(content)

        df = pd.read_csv(filepath, delimiter=";",
                         # Ignora linhas mal formatadas
                         error_bad_lines=False)
        df['ano'] = ano
        df['periodo'] = periodo
        dfs.append(df)
    pd.concat(dfs).to_csv(name + '.csv', sep=';', index=False)


download('turmas',
         'http://dados.ufrn.br/api/3/action/package_search?q=turmas de')
download('matriculas',
         'http://dados.ufrn.br/api/3/action/package_search?q=matriculas de')
