def main():
    resposta = input("você concorda? ").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "S":
        print("Eu concordo")
    elif resposta == "não" or resposta == "N":
        print("Não concordo")

  
main()       