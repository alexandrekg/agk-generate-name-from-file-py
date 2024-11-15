import random



def main():
    with open('names.txt') as nomes_file:
        lista_nomes = [nome.replace("\n", "") for nome in nomes_file]
    print(f"Nome gerado automaicamente: {random.choice(lista_nomes)}")


if __name__ == "__main__":
    main()