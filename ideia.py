#Ideia inicial do jogo 
# 
import random 

class Pokemon:
    def __init__(self, nome, level, tipo, ataques):
        self.nome = nome
        self.level = level
        self.ataques = ataques
        self.tipo = tipo

    def ataque(self):
        print("O pokemon atacou")
   
class Pikachu(Pokemon):
    def ataque(self):
        return f"{self.nome} usou {self.ataques}"
    
class Charizard(Pokemon):
    def ataque(self):
        return f"{self.nome} usou {self.ataques}"
    
class Blastoise(Pokemon):
    def ataque(self):
        return f"{self.nome} usou {self.ataques}"
    
class Venusaur(Pokemon):
    def ataque(self):
        return f"{self.nome} usou {self.ataques}"

pikachu = Pikachu("Pikachu", 15, "Eletrico", "Choque do trovão")  # print(pikachu.ataque())
charizard = Charizard("Charizard", 5, "Fogo", "Flamethrower")
blastoise = Blastoise("Blastoise", 20, "Agua", "Water blast")
venusaur = Venusaur("Venusaur", 30, "Grama", "Leech")

pokemons = [pikachu.nome, charizard.nome, blastoise.nome, venusaur.nome] # print(pokemons[numero_aleatorio])
pokedex = {}

def main():
    while True:
        try:
            opcao = int(input("O que deseja fazer?\n" 
            "1- capturar pokemon\n" 
            "2- olhar pokedex\n" 
            "3- desescravizar um pokemon\n" 
            "4- lutar\n"
            "5- sair\n"))
        except ValueError:
            print("Apenas numeros inteiros")

        if opcao == 1:
            while True:
                pokemon_aleatorio = random.randint(0, len(pokemons) - 1)
                pokemon_captura = pokemons[pokemon_aleatorio]
                level = random.randint(0,100)
                try:
                    captura = int(input(f"você encontrou um {pokemon_captura}, de level {level}. Deseja captura-lo?\n"
                                    "Digite 1 para sim e 2 para fugir\n"))
                except ValueError:
                    print("Utilize apenas numeros")
                if captura == 1:
                    pokedex = Pikachu(level)
                    break
                else:
                    break

        if opcao == 2:
            print(pokedex)

        if opcao == 3:
            pokemon = input("Digite o nome do pokemon que deseja soltar")
            del pokedex[pokemon]

        if opcao == 4:
            pokemon_aleatorio = random.randint(0, len(pokemons) - 1)
            luta = input(f"Um {pokemon_aleatorio}, de nivel {level} apareceu. Deseja lutar?\n"
                         "1 para sim e 2 para não\n")

#          if luta == 1: ##nada aqui é funcional, mas é a base da ideia (tenho que ver se assim vai funcionar)
#                primeiro_pokemon = next(iter(pokedex))
#                print(f"você jogou seu {primeiro_pokemon}")
#                print(primeiro_pokemon.ataques)
#                ataque = input("Escolha qual ataque usar")
#                
#                escolhido = ataques.ataque
#
#                escolhido.dano ou ataques.dano

#                ataques.dano -= pokemon_aleatorio.vida
#
#                print(f"{pokemon_aleatorio} tomou {ataques.dano} e ficou com {pokemon_aleatorio.vida}")

        if opcao == 5:
            break

main()