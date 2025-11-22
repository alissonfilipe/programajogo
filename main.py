import json 

# importação dos dados json
def ImportarJson():
    with open("dados.json","r") as file:
        dados = json.load(file)
        return dados


def main():
    dados = ImportarJson()
    print(dados)
    
if __name__ == "__main__":
    main()