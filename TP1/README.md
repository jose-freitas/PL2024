# TP1

## Autor

- José Paulino Ribeiro Freitas
- A96140

## Inunciado

- 1. Proibido usar o módulo CSV;
- 2. Ler o dataset, processá-lo e criar os seguintes resultados:
    1. Lista ordenada alfabeticamente das modalidades desportivas;
    2. Percentagens de atletas aptos e inaptos para a prática desportiva;
    3. Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

## Resolução

- A resolução foi feita num só módulo: code.py
- Foi feito o parsing do documento .csv de modo a exolar cada dado de cada atleta criando assim uma lista de listas à qual eu chamei "data".
- De seguida, foi criado um ciclo for para iterar sobre a lista "data" e retirar e trabalhar os dados de cada atleta para gerar o output.

## Input / Output

- Input: cat emv.csv | python3 import_sys.py
- Output: O resultado é imprimido no terminal em 4 linhas:
    1. Modalidades praticadas
    2. Percentagem de atletas aptos
    3. Percentagem de atletas inaptos
    4. Distribuição por ascalão de idades
