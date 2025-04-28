# Cotação de Moedas

Este projeto consulta a cotação atual do **Dólar** e **Euro** usando a API da HG Brasil e salva as informações em um banco de dados **SQLite**.

## Tecnologias usadas
- Python
- Biblioteca Requests
- Banco de dados SQLite3

## Como funciona
1. Faz uma requisição para a API de cotações.
2. Pega o valor do Dólar e Euro.
3. Salva a data, o valor do Dólar e o valor do Euro no banco de dados `bdcotacoes.db`.

## Observação
Antes de rodar o projeto, certifique-se que a tabela `moedas` já existe no banco de dados.

Exemplo de criação da tabela:
```sql
CREATE TABLE moedas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Data TEXT,
    Dolar REAL,
    Euro REAL
);
```
