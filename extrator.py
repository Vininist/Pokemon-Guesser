import json
import requests

print("Iniciando o pipeline de Extração de Dados (ETL)...\n")

# Lista que servirá de Staging Area para consolidação dos dados
banco_de_dados_completo = []

# Iteração sobre a base de IDs da geração clássica da PokeAPI
for i in range(1, 152):
    # Definição do Endpoint da API com interpolação dinâmica do ID
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    
    # Execução da requisição HTTP (método GET)
    resposta = requests.get(url)
    
    # Parse do payload JSON retornado pela API
    dados_brutos = resposta.json()
    
    # --- FASE DE TRANSFORMAÇÃO E LIMPEZA (DATA CLEANING) ---
    nome_extraido = dados_brutos["name"]
    peso = dados_brutos["weight"]
    numero_id = dados_brutos["id"]
    
    # Tratamento de lista aninhada para unificação de características múltiplas (Tipagem dupla)
    tipos_temporarios = []
    for tipologia in dados_brutos["types"]:
        tipos_temporarios.append(tipologia["type"]["name"])
        tipo = " / ".join(tipos_temporarios)
    
    # Modelagem do schema alvo padronizado para as necessidades da aplicação cliente (jogo.py)
    pokemon_limpo = {
        "nome": nome_extraido.capitalize(), 
        "dica1": f"Tipagem Oficial: {tipo}",
        "dica2": f"Peso: Pesa cerca de {peso/10}Kg.",
        "dica3": f"Número: É o número {numero_id} na Pokédex Mundial.",
        "dica4": f"Altura: Tem a altura de {dados_brutos['height']*10} cm.",
        "dica5": "Faz parte da primeira geração!"
    }
    
    # Carga contínua na Staging Area local
    banco_de_dados_completo.append(pokemon_limpo)
    
    # Log de output para monitoramento em tempo real
    print(f"Log: Captura estruturada do registro [ {pokemon_limpo['nome']} ] concluída.")

print("\nExtração e Transformação concluídas. Iniciando a etapa final de Load...")

# --- FASE DE CARGA E PERSISTÊNCIA (LOAD) ---
# Exportação da Staging Area para um banco físico persistente em formato JSON
with open("pokedex.json", "w", encoding="utf-8") as arquivo:
    json.dump(banco_de_dados_completo, arquivo, ensure_ascii=False, indent=4)

print("Pipeline ETL Concluído: Arquivo 'pokedex.json' exportado e pronto para consumo em banco de dados!")
