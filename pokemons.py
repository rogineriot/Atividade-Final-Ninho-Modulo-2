class Pokmemon :
    def __init__(self,nome,level, tipo, hp, ataque ,defesa):
        self.nome = nome
        self.level = level
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        
class PokemonAquatico(Pokmemon):
    def __init__(self, nome, level,tipo, hp, ataque, defesa):
        super().__init__(nome, level, tipo, hp, ataque, defesa) 
   
    
class PokemoPlanta(Pokmemon):
    def __init__(self, nome, level, tipo, hp, ataque, defesa):
        super().__init__(nome, level, tipo, hp, ataque, defesa)            
                           
class PokemonEletrico(Pokmemon):
    def __init__(self, nome, level, tipo, hp, ataque, defesa):
        super().__init__(nome, level, tipo ,hp, ataque, defesa)  
        
pokemon1 = PokemonAquatico("Squirtle",1,"Agua", 100,35,28)
pokemon2 = PokemonEletrico("Pikachu", 1, "Eletrico", 120, 36, 20) 
pokemon3 = PokemoPlanta("Bulbasaur",1,"Planta",120,30,30)
pokemon4 = PokemonAquatico("Wartortle",1,"Agua", 120,45,30)
pokemon5 = PokemonEletrico("Raichu", 1, "Eletrico", 130, 46, 30) 
pokemon6 = PokemoPlanta("Ivysaur",1,"Planta",130,40,40)
pokemon7 = PokemonAquatico('Blastoise', 1,"Agua",130,45,20)
pokemon8 = PokemonEletrico("Magnemit", 1, "Eletrico", 140, 40, 30)
pokemon9 = PokemoPlanta("Venusaur",1,"Planta",133,40,45)
pokemon10 = PokemonAquatico("Psyduck",1,"Agua", 120,39,35)
pokemon11 = PokemonEletrico("Magneton", 1, "Eletrico", 100, 44, 31)
pokemon12 = PokemoPlanta("Gloom",1,"Planta",137,43,40)
pokemon13 = PokemonAquatico("Golduck",1,"Agua", 110,44,230)
pokemon14 = PokemonEletrico("Voltorb", 1, "Eletrico", 130, 40, 27)
pokemon15 = PokemoPlanta("Vileplume",1,"Planta",130,45,38)
pokemon16 = PokemonAquatico("Poliwag",1,"Agua", 100,50,39)
pokemon17 = PokemonEletrico("Electrode", 1, "Eletrico", 118, 39, 28)
pokemon18 = PokemoPlanta("Bellsprout",1,"Planta",133,44,45)
pokemon19 = PokemonAquatico("Tentacruel",1,"Agua", 115,35,38)
pokemon20 = PokemonEletrico("Jolteon", 1, "Eletrico", 133, 40, 28)
pokemon21 = PokemoPlanta("Victreebel",1,"Planta",133,40,35)
pokemon22 = PokemonAquatico("Slowpoke",1,"Agua", 102,38,30)



listaPokemon = [pokemon1,pokemon2,pokemon3, pokemon4, pokemon5, pokemon6,pokemon7,
                pokemon8,pokemon9,pokemon10,pokemon11,pokemon12,pokemon13,pokemon14,
                pokemon15,pokemon16,pokemon17,pokemon18,pokemon19,pokemon20,pokemon21,
                pokemon22
            ]