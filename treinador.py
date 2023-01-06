#classe Treinador
class Treinador:
    def __init__(self,pokedex):
        self.pokedex = pokedex

#Método listar Pokemons    
    def listarPokemons(self):
       
        for i in range(len(self.pokedex)):
         print(f"{i}: Nome: {self.pokedex[i].nome} | Ataque {self.pokedex[i].ataque} | HP {self.pokedex[i].hp}")       

#Subclasse Treinador Inimigo
class Inimigo(Treinador):
    def __init__(self, pokedex):
        super().__init__(pokedex)
        
#Subclasse Treinador Jogador                
class Jogador(Treinador):
    def __init__(self, pokedex, nome):
        super().__init__(pokedex)        
        self.nome = nome