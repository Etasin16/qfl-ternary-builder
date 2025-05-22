import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
import pandas as pd
import matplotlib.pyplot as plt
import mpltern

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
@anvil.server.callable
def clean_commas(input_string):
  cleaned_string = ""
  prev_char = None
  for char in input_string:
    if char == ',' and prev_char == ',':
      continue  # Skip consecutive commas
    cleaned_string += char
    prev_char = char

  if cleaned_string.endswith(','):
    cleaned_string = cleaned_string[:-1]
  return cleaned_string

@anvil.server.callable
def DataFrm(d1,d2,d3):
  # Creating dataframe using inputed data
  df = pd.DataFrame({'Quartz': d1, 'Feldspar': d2, 'Lithics': d3})
  # calculation
  df['Total'] = df['Quartz'] + df['Feldspar'] + df['Lithics']
  
  df['%Q'] =  df['Quartz'] / df['Total'] * 100
  df['%F'] =  df['Feldspar'] / df['Total'] * 100
  df['%L'] =  df['Lithics'] / df['Total'] * 100
  return df.to_dict(orient='records')

@anvil.server.callable
def get_csv_download(dss):
  df=dss
  csv_str = df.to_csv(index=False)
  return anvil.media.from_string(csv_str, 'text/csv', name= f"export_{date.today()}.csv")