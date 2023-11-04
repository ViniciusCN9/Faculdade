def inverter_dicionario(dicionario):
    dicionario_invertido = {}
    for chave, valor in dicionario.items():
        if valor not in dicionario_invertido:
            dicionario_invertido[valor] = chave
        else:
            if isinstance(dicionario_invertido[valor], list):
                dicionario_invertido[valor].append(chave)
            else:
                dicionario_invertido[valor] = [
                    dicionario_invertido[valor], chave]
    return dicionario_invertido


codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

codigo_morse_invertido = inverter_dicionario(codigo_morse)

for chave, valor in codigo_morse_invertido.items():
    print(f"Valor: {chave}, Chave(s): {valor}")
