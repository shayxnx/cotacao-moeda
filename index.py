import requests
import sqlite3
from datetime import datetime

chave = "ff88dbb3"
url = f"https://api.hgbrasil.com/finance?format=json-cors&key={chave}" 
#F substitui o formato

response = requests.get(url)
dados = response.json() # pega os dados que puxou do get e transforma em formato json

dolar = dados['results']['currencies']['USD']['buy'] # usa os dados chamados do json
euro = dados['results']['currencies']['EUR']['buy']
data = datetime.now().strftime("%d-%m-%Y %H:%M:%S") # formata o horário

con = sqlite3.connect('bdcotacoes.db') #conecta o banco de dados
cursor = con.cursor()
cursor.execute("INSERT INTO moedas (Data, Dolar, Euro) VALUES (?, ?, ?)", (data, dolar, euro))
con.commit()
cursor.close()
con.close()

print("Dados salvos na Tabela!")

print(f"Cotação do Dólar: {dolar}") 
print(f"Cotação do Euro: {euro}")
