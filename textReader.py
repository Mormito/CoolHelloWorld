import random
import time

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def bufferedReader():
    path = "./text.txt"

    try:
        with open(path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except IOError:
        print("Erro ao ler o arquivo.")

    return content #!

def function():
    letters = list(file_content)
    print()

    final_word = ""

    for letter in letters:
        x = letter
        for char in chars:
            if char == x:
                final_word = final_word + final_word.join(x)
                time.sleep(0.001)
                print(final_word)

                if final_word == file_content:
                    for i in range(5):
                        time.sleep(0.01)
                        print(final_word)
                    break
            else:
                final_word = final_word + final_word.join(char)
                time.sleep(0.001)
                print(final_word)
                final_word = final_word[:-1]
                

file_content = bufferedReader()
function()