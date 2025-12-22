import requests
import time
import pandas as pd
import numpy as np

def get_pokemon_name(input) :
  result = input['name'].capitalize()
  return result

def get_pokemon_type(input) :
  primary_type=np.nan
  secondary_type=np.nan
  if len(input['types']) > 1 :
    primary_type=input['types'][0]['type']['name'].capitalize()
    secondary_type=input['types'][1]['type']['name'].capitalize()
  else :
    primary_type=input['types'][0]['type']['name'].capitalize()

  return primary_type,secondary_type

def get_pokemon_basestat(input) :
  result = {
    input["stat"]["name"]: input["base_stat"]
    for input in input["stats"]
  }
  return result

def get_pokemon_image_url(input) :
  try :
    result = input["sprites"]["front_default"]
  except :
    result = None
  return result

def transform_to_dataframe(input) :
  rows = []

  for pokemon, deskripsi in input.items():
      stats = deskripsi["pokemon_stat"]

      rows.append({
          "pokemon_name": pokemon,
          "primary_type" : deskripsi["primary_type"],
          "secondary_type" : deskripsi["secondary_type"],
          "hp": stats["hp"],
          "attack": stats["attack"],
          "defense": stats["defense"],
          "special_attack": stats["special-attack"],
          "special_defense": stats["special-defense"],
          "speed": stats["speed"],
          "image_url" : deskripsi["pokemon_image_url"]
      })

  dataset = pd.DataFrame(rows)
  return  dataset


def get_dataset_information (number_of_pokemon) :
  dict_master_data_pokemon = {}

  if number_of_pokemon <1 :
    raise ValueError("Number of pokemomn must be greater than 0")

  #loop untuk fetch data tiap pokemon
  for pokemon_index in range(1,number_of_pokemon+1) :

    #url api pokeapi1
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_index}"

    #get response
    response=requests.get(url)

    #data
    data=response.json()

    #called functions to get desired value
    pokemon_name = get_pokemon_name(data)

    pokemon_type = get_pokemon_type(data)
    main_type,secondary_type = pokemon_type[0],pokemon_type[1]

    pokemon_stat = get_pokemon_basestat(data)

    pokemon_image_url = get_pokemon_image_url(data)

    #compile it as dict
    dict_master_data_pokemon[pokemon_name] = {
      'primary_type' : main_type,
      'secondary_type' : secondary_type,
      'pokemon_stat' : pokemon_stat,
      'pokemon_image_url' : pokemon_image_url
    }

    time.sleep(1)

  #convert to dataframe
  df_result=transform_to_dataframe(dict_master_data_pokemon)

  print(f"Done for all {number_of_pokemon} pokemons with the last pokemon was --- {pokemon_name} --- with index nomber : {pokemon_index} \n")


  return df_result