# 🕹️ Quem é esse Pokémon? (Versão 2.0: ETL Edition)

Bem-vindo ao meu primeiro projeto de Data Science e Programação em Python! 
O que começou didaticamente como um divertido "jogo de adivinhação" evoluiu rapidamente para um sistema completo de **Engenharia de Dados (ETL)** operando com conceitos reais do mercado de TI.

Ao invés de depender de dados falsos ou digitados à mão no código, o motor desse projeto consome os dados oficiais direto da API internacional para gerar toda inteligência dos desafios! 🚀

## 🧠 Arquitetura do Projeto
Para que a mágica inteira funcione com escalabilidade, a máquina foi fracionada em dois blocos:

### 1. O Pipeline Extrator (`extrator.py`)
Esse é o trator que trabalha sujo nos bastidores! É um Script massivo de ETL *(Extract, Transform and Load)* construído do zero, responsável por abastecer o projeto:
- **Extrair (Extract):** Executa conexões automatizadas usando o pacote `requests` na nuvem pública da [PokéAPI](https://pokeapi.co/) varrendo os 151 Monstros da Geração 1.
- **Transformar (Data Cleaning):** Recebe e ignora um JSON gigantesco cheio de lixo (Payload), filtrando cirurgicamente apenas informações cruciais para o jogo (Nome, Altura, Peso, Tipo). Como diferencial, possui lógica de Tratamento de Sublistas para concatenar e tratar exceções de Pokémons de dupla ou tripla tipagem (como o *Edge Case* do Omastar 🪨/💧). Faz também conversões de matemática pura no meio do texto, passando unidades imperiais para o Sistema Métrico de CM e KG.
- **Carregar (Load):** Consolida toda a limpeza em uma Staging Area de memória RAM, convertendo as chaves para nosso schema oficial e exportando diretamente ao HD no nosso repositório em formato `pokedex.json`.

### 2. O Motor Interativo (`jogo.py`)
O front-end onde tudo ganha vida através da pura base estrutural da linguagem, focado no Usuário (UX):
- O sistema importa a biblioteca nativa, lê (`r`) nosso banco carregado `pokedex.json` com centenas de linhas instantaneamente e sorteia um alvo de forma invisível.
- Toda a lógica da experiência é refém de uma Roda Gigante da Programação (`while vidas > 0`) para controlar os inputs e outputs textuais (`f-strings`) com o usuário.
- Mapeamentos lógicos super ramificados (`if / elif / else`) testam a cadeia consecutiva de erros para engatilhar sempre uma dica mais valiosa que a anterior vinda da Pokédex sem quebrar o algoritmo (Impedindo o KeyError).

## 💻 Tech Stack & Fundamentos da Sessão
> 🔧 `Python 3`, `Requests Library`, `REST APIs`, `Manipulação JSON`, `Lógica de Estruturas Condicionais`, `Loops Ininterruptos` e Versionamento com `Git`.

## 🎲 Como jogar no seu Terminal?
Abra sua pasta local no prompt de comando e digite:

```bash
# 1º Passo: Rode nosso trator pelo menos 1 vez para "Puxar a Pokedex" pra sua máquina:
python extrator.py

# 2º Passo: Dê start e comece a adivinhar!
python jogo.py
```

---
*Construído na raça com muito código quebrado durante a solidificação das minhas bases iniciais para ingressar na área de TI & Ciência de Dados! Temos que pegar todos os dados!* 🔴⚪
