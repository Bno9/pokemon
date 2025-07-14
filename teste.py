import random 
import json

pokemons_json = [] #formatação do json pra lista dentro do código

ataques = [] #por enquanto não tem utilidade, a não ser pra mostrar todos ataques existentes

pokemons_lista = [] #formatação da lista json pra objetos da classe pokemon

pokedex = {} #Pokedex é onde eu to salvando os pokemons capturados por enquanto

#abertura do json
with open("pokemons.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
        

#criação da classe pokemon
class Pokemon:
    def __init__(self, nome, level, xp, vida_max, vida, vida_base, tipo, ataques):
        self.nome = nome
        self.level = level
        self.xp = xp
        self.vida_max = vida_max
        self.vida = vida
        self.vida_base = vida_base
        self.tipo = tipo
        self.ataques = ataques

    #xp necessario para upar
    def xp_proximo_nivel(self):
        return int(100 * (self.level ** 1.2))
    
    #metodo de ganhar xp
    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        while self.xp >= self.xp_proximo_nivel():
            self.xp -= self.xp_proximo_nivel()
            self.level += 1
            print(f"{self.nome} subiu para o level {self.level}!")
            self.vida_max = int(self.vida_base * (self.level ** 1.2))
            self.vida = self.vida_max

            for ataque in self.ataques:
                ataque.dano = int(ataque.dano * (1 + 0.05 * self.level))

    #metodo pra curar
    def curar_pokemon(self):
        self.vida = self.vida_max

    #formatação do print
    def __str__(self):
        return f"{self.nome} (Level {self.level}) - Tipo: {self.tipo}\nStatus:\nVida_max: {self.vida_max}\nVida_atual: {self.vida}\nXP: {int(self.xp)}\nXP necessário pro próximo nivel:{self.xp_proximo_nivel()}"

#criação da classe ataque
class Ataques:
    def __init__(self, nome, dano_base, dano, tipo):
        self.nome = nome
        self.dano_base = dano_base
        self.dano = dano
        self.tipo = tipo

    #formatação do print
    def __str__(self):
        return f"{self.nome} ({self.tipo}) - {self.dano} de dano"

#formatação do json pra lista de pokemon e ataque
for p in dados:
    pokemons_json.append(p)
    for i in p["ataques"]:
        objeto_ataque = Ataques(i["nome"], i["dano"], i["dano"], i["tipo"])
        ataques.append(objeto_ataque)

#formatação da lista de pokemon pra objeto pokemon, e respectivos ataques
for p in pokemons_json:
    ataques_do_pokemon = []
    for i in p["ataques"]:
        dano_base = random.randint(10,30)
        dano = random.randint(30,50)
        ataque_obj = Ataques(i["nome"], dano_base, dano, i["tipo"])
        ataques_do_pokemon.append(ataque_obj)

    objeto_pokemon = Pokemon(p["nome"], p["level"], p["xp"], p["vida_max"], p["vida"], p["vida"], p["tipo"], ataques_do_pokemon)
    pokemons_lista.append(objeto_pokemon)
    
#função principal do jogo
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

        #captura de pokemon
        if opcao == 1:
            while True:

                pokemon_aleatorio = pokemons_lista[random.randint(0, len(pokemons_lista) - 1)]
                level = random.randint(3, 20)
                vida_max = random.randint(3,7) * level
                vida_base = random.randint(10,20)
                
                try:
                    captura = int(input(f"você encontrou um {pokemon_aleatorio.nome}, de level {level}. Deseja captura-lo?\n"
                                    "Digite 1 para sim e 2 para fugir\n"))
                except ValueError:
                    print("Utilize apenas numeros")
                if captura == 1:
                    pokemon_aleatorio.level = level
                    pokemon_aleatorio.vida_max = vida_max
                    pokemon_aleatorio.vida_base = vida_base
                    pokemon_aleatorio.vida = pokemon_aleatorio.vida_max
                    pokedex[pokemon_aleatorio.nome] = pokemon_aleatorio
                    break
                else:
                    break

        #ver pokemons capturados
        if opcao == 2:
            for nome, pokemon in pokedex.items():
                print(pokemon)

        #deletar pokemon da pokedex
        if opcao == 3:
            pokemon = input("Digite o nome do pokemon que deseja soltar\n")
            del pokedex[pokemon]

        #lutar
        if opcao == 4 and pokedex:

            #definindo qual pokemon ira aparecer, e os stats
            pokemon_aleatorio = pokemons_lista[random.randint(0, len(pokemons_lista) - 1)]
            level = random.randint(3, 20)
            vida = random.randint(5,11) * level
            pokemon_aleatorio.vida = vida

            luta = int(input(f"Um {pokemon_aleatorio.nome}, de level {level} apareceu. Deseja lutar?\n"
                         "1 para sim e 2 para não\n"))

            if luta == 1:
                #definindo pokemon da luta
                nome_pokemon = next(iter(pokedex))
                primeiro_pokemon = pokedex[nome_pokemon]
                print(f"você jogou seu {primeiro_pokemon.nome}")

                xp = int(random.randint(80, 600) * level)

                #começo da luta
                while True:
                    print(primeiro_pokemon.nome)
                    for i, ataque in enumerate(primeiro_pokemon.ataques):
                        print(f"{i}  - {ataque}")

                    escolha = int(input("Escolha qual ataque usar (numero):"))
                    
                    ataque_escolhido = primeiro_pokemon.ataques[escolha]

                    pokemon_aleatorio.vida -= ataque_escolhido.dano
                    print(f"{pokemon_aleatorio.nome} tomou {ataque_escolhido.dano} de dano e ficou com {pokemon_aleatorio.vida} de vida.")

                    ataque_inimigo = pokemon_aleatorio.ataques[random.randint(0,1)]

                    primeiro_pokemon.vida -= ataque_inimigo.dano
                    print(f"{pokemon_aleatorio.nome} usou {ataque_inimigo.nome} e deu {ataque_inimigo.dano} de dano, seu pokemon ficou com {primeiro_pokemon.vida} de vida.")

                    if pokemon_aleatorio.vida <= 0:
                        print(f"você derrotou {pokemon_aleatorio.nome} e ganhou {xp} de experiencia")
                        primeiro_pokemon.ganhar_xp(xp)
                        break

                    elif primeiro_pokemon.vida <=0:
                        print(f"Você foi derrotado por {pokemon_aleatorio.nome}")
                        primeiro_pokemon.curar_pokemon()
                        # primeiro_pokemon = next(iter(pokedex)) aqui eu queria que continuasse mandando o proximo pokemon, mas nao sei se essa seria a melhor logica
                        break

            #fugir
            if luta == 2:
                pass

        #sair do jogo
        if opcao == 5:
            break

main()