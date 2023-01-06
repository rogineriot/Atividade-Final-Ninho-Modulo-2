def batalhar(poke1,poke2):
    round = 0
    print(f"{poke1.nome} VS {poke2.nome}")
    [hp1,hp2] = [poke1.hp, poke2.hp]

#Loop da batalha    
    while (hp1 > 0 and hp2>0):
        if hp2 > 0:
            hp1 -= poke2.ataque
        if hp1 > 0:
            hp2 -= poke1.ataque
        round += 1 

#Verificação se poke1 ganhou      
    if hp1 > 0 and hp1 > hp2 :
       
        print(f"{poke1.nome} foi o vencedor em {round} rounds")
 
#Verificação se poke2 ganhou            
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
            
#Verificação se pokemon do treinador ganhou a batalha contra o pokemon selvagem            
        if hp1 > 0 and hp1 > hp2 :
        
            print(f"você capturou {pokemonSelvagem.nome} ")
            treinador.pokedex.append(pokemonSelvagem)

#Verificação se pokemon selvagem ganhou a batalha contra o pokemon do treinador               
        elif hp2 > 0 and hp2 > hp1:
            print(f"Você não capturou")  
            

