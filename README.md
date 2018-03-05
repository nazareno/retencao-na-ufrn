# retencao-na-ufrn

disciplinas de que períodos reprovam mais na ufrn? 

## baixar_dados.py

Esse script baixa os dados das turmas e matrículas, os agrupando em 2 CSVs.

Para instalar usando `virtualenv`:

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt
    
(caso já tenha o `pip` e queira instalar as dependências no sistema como um todo, usar só o último comando)
    
Depois rodar com:

    python baixar_dados.py

Os CSV final de matrículas não foi inserido diretamente no repositório porque tem quase 1GB.
