palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

palavra1 = palavra1.replace(" ", "").lower()
palavra2 = palavra2.replace(" ", "").lower()

if sorted(palavra1) == sorted(palavra2):
    print("As palavras são anagramas")
else:
    print("As palavas não são anagramas")