import random    
import os
from pokemons import listaPokemon
from funcoes import batalhar, capturar
from treinador import Inimigo, Jogador


pokemonsInimigo = [listaPokemon[random.randint(0,22)],listaPokemon[random.randint(0,22)],listaPokemon[random.randint(0,22)]]
escolha = 8
pokemonInicial = 1

#Criando objeto inimigo
treinadorInimigo = Inimigo(pokemonsInimigo)

#Listando todos od pokemons para escolha
for i in range(len(listaPokemon)) :
    print(f"{i} - {listaPokemon[i].nome}") 
pokemonsJogador = []

#criando o objeto jogador
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
        poke = int(input("Escolha o pokemon digitando seu código: "))  
        capturar(jogador.pokedex[poke],listaPokemon[random.randint(0,22)],jogador) 
            
    elif escolha == 3:
        jogador.listarPokemons()  
        poke = int(input("Escolha seu pokemon digitando seu código: "))          
        batalhar(jogador.pokedex[poke],treinadorInimigo.pokedex[0]) 
        
        
        







     