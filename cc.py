#!/usr/bin/python
# -*- coding: utf-8 -*-

abecedario = 'abcdefghijklmnopqrstuvwxyz'

def banner():                                                   
    print ''
    print '  __     ___  __        __   __   __      __   ___  __        __  '
    print ' /  ` | |__  |__)  /\  |  \ /  \ |__)    /  ` |__  /__`  /\  |__) '
    print ' \__, | |    |  \ /--\ |__/ \__/ |  \    \__, |___ .__/ /--\ |  \ '
    print '                                                      by: wh04m1 ◐  '
    print '──────━━━━━━━━── ● Elige tu lado y diviértete... ○ ──━━━━━━━━──────'
    print ''

def cifrar(palabra, clave):

    palabracifrada = ''

    for letra in texto:
        suma = abecedario.find(letra) + clave
        modulo = int(suma) % len(abecedario)
        palabracifrada = palabracifrada + str(abecedario[modulo])
    
    return palabracifrada

def descifrar(palabra, clave):

    palabradescifrada = ''

    for letra in texto:
        resta = abecedario.find(letra) - clave
        modulo = int(resta) % len(abecedario)
        palabradescifrada = palabradescifrada + str(abecedario[modulo])
    
    return palabradescifrada

def main():
    print ''
    cifrado = str(raw_input('[?] Ingrese palabra a cifrar: ')).lower()
    print ''
    clavecifrado = int(raw_input('[?] Ingrese clave numérica de cifrado: '))
    print ''
    print '[+] Palabra cifrada: ' + cifrar(cifrado, clavecifrado)
    print ''
    print ''
    print ''
    descifrado = str(raw_input('[?] Ingrese palabra a descifrar: ')).lower()
    print ''
    clavedescifrado = int(raw_input('[?] Ingrese clave numérica de descifrado: '))
    print ''
    print '[+] Palabra descifrada: ' + descifrar(descifrado, clavedescifrado)

if __name__ == "__main__":
    banner()
    main()
