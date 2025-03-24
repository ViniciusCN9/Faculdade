pessoas_idade = [("Ana", 30), ("João", 25), ("Maria", 35)]

pessoas_idade.sort(key=lambda x: x[1])

for pessoa, idade in pessoas_idade:
    print(f"{pessoa}: {idade} anos")