def morse_translation():
    message = input('Enter a message: ')
    morse_list = []
    morse_dictionary = {' ': '/','A': '.-', 'B': '-...', 'C': '-.-.','D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--','N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    for char in message:
        char = char.upper()
        morse_list.append(morse_dictionary[char])
    return "".join(morse_list)
