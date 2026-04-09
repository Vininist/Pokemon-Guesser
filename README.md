# Quem é esse Pokémon? 🕹️

E aí! Esse é o meu primeiro projeto totalmente prático criado para treinar a lógica pura do Python. Em vez de criar aquele "Jogo da Forca" batido de sempre, eu decidi programar um jogo interativo de adivinhação usando a Pokédex. 

A mecânica do jogo é simples: o computador sorteia um Pokémon em segredo, te fala só quantas letras o nome dele tem, e a cada vez que você erra o chute, ele gasta uma das suas 5 vidas e "cospe" uma dica nova sobre as características dele (qual é o Tipo daquele Pokémon, curiosidades, qual a evolução, etc). Tudo até você adivinhar ou tomar Game Over!

## O que eu treinei aqui?
Usei esse projeto para fixar a base de qualquer linguagem de programação. Usei:

- **Dicionários e Listas (O Banco de Dados)**: Serviram para mapear as fichas e características completas dos Pokémons de forma organizada na memória.
- **Loops (`while`)**: Seguraram a tela do jogo rodando infinitamente impedindo que o Python fechasse na cara do usuário até que as Vidas cheguem a zero.
- **Checagens (`if / elif / else`)**: A base da inteligência do jogo para soltar a dica 1 se o cara tiver 1 erro, a dica 2 se ele tiver 2 erros, e por aí vai.
- **Interação (`input` e `print`)**: Captar e entregar frases com variáveis escondidas no meio do texto (usando f-strings).
- **Git & GitHub**: Versionar e usar commits no terminal como se deve!

## Como testar aí na sua máquina
Basta ter o Pyhton rodando normal no seu computador. Abra o terminal na pastinha desse e projeto e jogue o clássico:

```bash
python jogo.py
```

---
