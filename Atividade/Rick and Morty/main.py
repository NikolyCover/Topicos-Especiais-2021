from numpy import character
import pandas as pd
from IPython import display

rick_morty_df = pd.read_json('https://raw.githubusercontent.com/jeffersonchaves/rick-and-morty-dados/main/character.json')

#Quantos personagens existe nessa lista?
linha, coluna = rick_morty_df.shape

print(f"Existem {100} personagens nesse arquivo")

#Quantos personagens são humanos?
humano_condicao = rick_morty_df['species'] == 'Human'

human_df = rick_morty_df.loc[humano_condicao]
qtty_humanos, col = human_df.shape

print(f'Existem {qtty_humanos} humanos nesse arquivo')

#Quantos personagens são alienígenas?
alien_condition = rick_morty_df['species'] == 'Alien'

alien_df = rick_morty_df.loc[alien_condition]
qtty_aliens, col = alien_df.shape

print(f'Existem {qtty_aliens} aliens nesse arquivo')

#Há quantos tipos de alienígenas diferentes?
x = alien_df['type'].value_counts()

qtty_alienTypes = x.shape
print(f'Existem {qtty_alienTypes[0]} tipos de aliens')

#Qual o nome do episódio em que o personagem Crocubot aparece?
episodes_df = pd.read_json('https://raw.githubusercontent.com/jeffersonchaves/rick-and-morty-dados/main/episode.json')

crocubot_condition = rick_morty_df['name'] == 'Crocubot'

crocubot = rick_morty_df[crocubot_condition]

episode_croc = crocubot['episode']
episode_croc = episode_croc[80]
episode_croc = int(episode_croc.split('/')[-1])
episode_croc = episodes_df[episode_croc]

print(f'O nome do episodio em que o Crocubot aparece é {episode_croc}')