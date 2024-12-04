def main():
    tamanho = int(input("informe o tamanho: "))
    bloco(tamanho)
    
def bloco(tamanho):
    bloco = ("[]" * tamanho)    
    print (f"{bloco}\n" * tamanho, end = '')

main() 