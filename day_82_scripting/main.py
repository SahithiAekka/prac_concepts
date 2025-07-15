# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.',   'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--',  'N': '-.',  'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-',   'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----',  '1': '.----', '2': '..---',
    '3': '...--',  '4': '....-', '5': '.....',
    '6': '-....',  '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    result = []
    for char in text.upper():
        morse = MORSE_CODE_DICT.get(char)
        if morse:
            result.append(morse)
        else:
            result.append('?')  # Unknown character
    return ' '.join(result)

if __name__ == "__main__":
    print("Morse Code Converter")
    while True:
        user_input = input("Enter text (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        print("Morse Code:", text_to_morse(user_input))
