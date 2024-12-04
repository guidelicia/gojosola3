ninjas = {
    
    "Naruto" : {
      "clã": "uzumaki", 
      "rank": "Gennin",
      "idade": "14 anos",
      "nivel de ninjutsu": "3 pontos",
    },
    "Sasuke" : {
      "clã": "uchiha", 
      "rank": "Gennin", 
      "idade": "14 anos",
      "nivel de ninjutsu": "4 pontos",
    },
    "Kakashi" : {
      "clã": "hatake", 
      "rank": "Jonnin", 
      "idade": "32 anos",
      "nivel de ninjutsu": "5 pontos",
    },
    "Obito" : {
      "clã": "uchiha", 
      "rank": "Gennin", 
      "idade": "32 anos",
      "nivel de ninjutsu": "5 pontos",
    },
    "Neji" : {
      "clã": "hyuuga", 
      "rank": "Gennin", 
      "idade": "15 anos",
      "nivel de ninjutsu": "4 pontos",
    },
    "Minato" : {
      "clã": "namikaze", 
      "rank": "hogake", 
      "idade": "24 anos",
      "nivel de ninjutsu": "5 pontos",
    },
    "Itachi" : {
      "clã": "uchiha", 
      "rank": "Jonnin", 
      "idade": "22 anos",
      "nivel de ninjutsu": "5 pontos",
    },
    "Orochimaru" : {
      "clã": "desconhecido", 
      "rank": "Jonnin", 
      "idade": "30 anos",
      "nivel de ninjutsu": "5 pontos",
    },
    "Sakura" : {
      "clã" : "haruno", 
      "rank" : "Gennin", 
      "idade" : "14 anos",
      "nivel de ninjutsu" : "3 pontos",
    },
    "Hashirama" : {
      "clã" : "Senju", 
      "rank" : "hogake", 
      "idade" : "30 anos",
      "nivel de ninjutsu" : "10 pontos",
    },

}
def exibir(nome):
    if nome in ninjas:
        ninja = ninjas[nome]
        print(f"Nome: {nome}")
        print(f"clã: {ninja['clã']}")
        print(f"rank: {ninja['rank']}")
        print(f"idade: {ninja['idade']}")
        print(f"nivel de ninjutsu: {ninja['nivel de ninjutsu']}")
    else:
        print("ninja não encontrado")

g = input("digite um ninja de Naruto: ").title()

exibir(g)
 