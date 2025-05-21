from ._anvil_designer import QFLTemplate
from anvil import *
import requests

class QFL(QFLTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def clean_commas(input_string):
    cleaned_string = re.sub(r',+', ',', input_string)
    if cleaned_string.endswith(','):
      cleaned_string = cleaned_string[:-1]
    return cleaned_string

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.InputArea.visible = not self.InputArea.visible

  def SubmitButton_click(self, **event_args):
    AaQ_str = input("Enter Quartz values separated by commas (,): ")
    AaF_str = input("Enter Feldspar values separated by commas (,): ")
    AaL_str = input("Enter Lithics values separated by commas (,): ")

    try:
    # Quartz
     cleaned_q = clean_commas(AaQ_str)
     qList = [int(x.strip()) for x in cleaned_q.split(',') if x.strip()]

    # Feldspar
     cleaned_f = clean_commas(AaF_str)
     fList = [int(x.strip()) for x in cleaned_f.split(',') if x.strip()]

    # Lithics
     cleaned_l = clean_commas(AaL_str)
     lList = [int(x.strip()) for x in cleaned_l.split(',') if x.strip()]

    except ValueError:
     print("Invalid input. Please enter numerical values separated by commas.")