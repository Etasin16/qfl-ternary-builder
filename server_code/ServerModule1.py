import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
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
