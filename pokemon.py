import random    
import os
from pokemons import listaPokemon


class Treinador:
    def __init__(self,pokedex):
        self.pokedex = pokedex
        
    def listarPokemons(self):
       
        for i in range(len(self.pokedex)):
         print(f"{i}: Nome: {self.pokedex[i].nome} | Ataque {self.pokedex[i].ataque} | HP {self.pokedex[i].hp}")       

class Inimigo(Treinador):
    def __init__(self, pokedex):
        super().__init__(pokedex)
        
class Jogador(Treinador):
    def __init__(self, pokedex, nome):
        super().__init__(pokedex)        
        self.nome = nome
        
def batalhar(poke1,poke2):
    round = 0
    print(f"{poke1.nome} VS {poke2.nome}")
    [hp1,hp2] = [poke1.hp, poke2.hp]
    
    while (hp1 > 0 and hp2>0):
        if hp2 > 0:
            hp1 -= poke2.ataque
        if hp1 > 0:
            hp2 -= poke1.ataque
        round += 1 
      
    if hp1 > 0 and hp1 > hp2 :
       
        print(f"{poke1.nome} foi o vencedor em {round} rounds")
        
    elif hp2 > 0 and hp2 > hp1:
        print(f"{poke2.nome} foi o vencedor em {round} rounds")       

                        

def capturar(pokemonJogador, pokemonSelvagem,treinador):
        print(f"{pokemonJogador.nome} VS {pokemonSelvagem.nome}")
        [hp1,hp2] = [pokemonJogador.hp, pokemonSelvagem.hp]
        
        while (hp1 > 0 and hp2>0):
            if hp2 > 0:
                hp1 -= pokemonSelvagem.ataque
            if hp1 > 0:
                hp2 -= pokemonJogador.ataque
            
        
        if hp1 > 0 and hp1 > hp2 :
        
            print(f"você capturou {pokemonSelvagem.nome} ")
            treinador.pokedex.append(pokemonSelvagem)
            
        elif hp2 > 0 and hp2 > hp1:
            print(f"Você não capturou")     


pokemonsInimigo = [listaPokemon[random.randint(0,22)],listaPokemon[random.randint(0,22)],listaPokemon[random.randint(0,22)]]
escolha = 8
pokemonInicial = 1


treinadorInimigo = Inimigo(pokemonsInimigo)

for i in range(len(listaPokemon)) :
    print(f"{i} - {listaPokemon[i].nome}") 
pokemonsJogador = []

nome = str(input("Digite o nome do jogador: "))
jogador = Jogador(pokemonsJogador, nome)   

for i in range(3):
    pokeOp = int(input("Escolha um Pokemon: "))
    pokemonsJogador.append(listaPokemon[pokeOp])
    

os.system("cls") or None


while escolha !=0:

    print("1 - Listar Pokemons")
    print("2 - Capturar Pokemons")
    print("3 - Batalhar")
    print("0 - Sair")
    
    escolha = int(input("Escolha o que quer fazer: "))
    
    if escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3:
        print("Opção inválida!")
    
    if escolha == 1 :
       print("Pokemons ", jogador.nome)
       jogador.listarPokemons()
            
    elif escolha == 2:
        jogador.listarPokemons()
        poke = int(input("Escolha seu pokemon digitando seu código: "))  
        capturar(jogador.pokedex[poke],listaPokemon[random.randint(0,22)],jogador) 
            
    elif escolha == 3:
        jogador.listarPokemons()  
        poke = int(input("Escolha seu pokemon digitando seu código: "))          
        batalhar(jogador.pokedex[poke],treinadorInimigo.pokedex[random.randint(0,3)]) 
        
        
        







     