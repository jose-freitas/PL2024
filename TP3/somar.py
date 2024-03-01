import sys
import re

def somar(t):

    total = 0
    switch = True

    numero = '[+-]?\d+'
    on = '[Oo][Nn]'
    off = '[Oo][Ff]{2}'
    soma = '='

    delimitador = f"(?P<on>{on})|(?P<off>{off})|(?P<numero>{numero})|(?P<soma>{soma})"

    linha = re.finditer(delimitador, t)

    for l in linha:

        if l.lastgroup == 'soma':
            print(f"{total}\n")

        elif l.lastgroup == 'on':
            switch = True

        elif l.lastgroup == 'off':
            switch = False

        elif l.lastgroup == 'numero' and switch:
            total += int(l.group('numero'))

    print(f"Soma total: {total}\n")

if __name__ == '__main__':

    teste = "ONhbfcufg8hfjbc=off78jfjkon94"
    print(somar(teste))