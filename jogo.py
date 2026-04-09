
import random

print("Bem-vindo ao Descubra o Pokémon!")
nome_jogador = input("Qual o seu nome, Mestre Pokémon? ")
print(f"Muito prazer, {nome_jogador}! Prepare-se para o desafio...")

# 1. Definir o Pokémon Secreto e criar sua pequena "Pokédex" de dados na Memória.

lista_pokemons = [
    {
        "nome": "Charmander",
        "dica1": "Tipagem: Fogo",
        "dica2": "Geração: Primeira Geração (Kanto)",
        "dica3": "Evolução: É o estágio inicial do Charizard",
        "dica4": "Característica: Tem cor predominantemente laranja",
        "dica5": "Fato bizarro: Se a ponta do rabo dele apagar, ele morre..."
    },
    {
        "nome": "Squirtle",
        "dica1": "Tipagem: Água",
        "dica2": "Geração: Primeira Geração (Kanto)",
        "dica3": "Evolução: É o estágio inicial do Blastoise",
        "dica4": "Característica: É parecido com uma tartaruga azul",
        "dica5": "Fato do Anime: Liderou um esquadrão famoso usando óculos escuros"
    },
    {
        "nome": "Bulbasaur",
        "dica1": "Tipagem: Planta / Veneno",
        "dica2": "Geração: Primeira Geração (Kanto)",
        "dica3": "Evolução: É o estágio inicial do Venusaur",
        "dica4": "Característica: Tem pele verde",
        "dica5": "Fato da Pokédex: É oficialmente o Pokémon de nº 001 do mundo"
    }
]

#Sorteia alguém da lista sem nos contar quem é!
pokemon_secreto = random.choice(lista_pokemons)

# 2. Configurar o Banco de Vidas (Limite de 5 erros possíveis).

vidas = 5
erros = 0

# 3. Mostrar a Dica Inicial (O número de letras).
quantidade_letras = len(pokemon_secreto["nome"])
print(f"\n---> O Pokémon secreto tem {quantidade_letras} letras!")
print(f"---> Você tem o total de {vidas} chances para acertar.\n")
# 4. Criar o Loop Ininterrupto: o jogo fica rodando até ele acertar todas as letras ou perder as 5 vidas.

while vidas > 0:
    chute = input("\nQuem é esse Pokémon? ")
    
    
# 5. O Coração do Motor: Se errar, libera a próxima dica baseada na quantidade de erros que já teve. Se acertar, vence.
    if chute == pokemon_secreto["nome"]:
        print(f"\n🎉 PARABÉNS! Você provou ser um Mestre e acertou: era o {pokemon_secreto['nome']}!")
        break
    else:
        vidas = vidas - 1
        erros = erros + 1
        print(f"\n❌ Errado, sua Pokébola quebrou! Você perdeu 1 vida. Restam {vidas} chances.")
        
        # O Sistema da Pokédex (Múltipla Condição)
        if erros == 1:
            print(f"Pokédex diz -> {pokemon_secreto['dica1']}")
        elif erros == 2:
            print(f"Pokédex diz -> {pokemon_secreto['dica2']}")
        elif erros == 3:
            print(f"Pokédex diz -> {pokemon_secreto['dica3']}")
        elif erros == 4:
            print(f"Pokédex diz -> {pokemon_secreto['dica4']}")
        elif erros == 5:
            print(f"Derradeiro fato -> {pokemon_secreto['dica5']}")

if vidas == 0:
    print(f"\n💀 GAME OVER! O Pokémon fugiu e desapareceu na fumaça! Ele era o {pokemon_secreto['nome']}!")
