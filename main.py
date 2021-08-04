
from banner import Banner
from morse_code import morseCode
print(Banner.text)

inputText = input("Input text to convert to Morse Code: ")

print("\nMorse Code:")
for character in inputText:
    print("\t" + morseCode[character.upper()])
print("\n")
