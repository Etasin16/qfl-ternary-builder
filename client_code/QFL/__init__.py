from ._anvil_designer import QFLTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class QFL(QFLTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.InputArea.visible = not self.InputArea.visible

  def SubmitButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    AaQ_str = self.Quartz.text
    AaF_str = self.Feldspar.text
    AaL_str = self.Lithics.text

    try:
      # Quartz
      cleaned_q = anvil.server.call('clean_commas', AaQ_str)
      qList = [int(x.strip()) for x in cleaned_q.split(',') if x.strip()]
    
      # Feldspar
      cleaned_f = anvil.server.call('clean_commas', AaF_str)
      fList = [int(x.strip()) for x in cleaned_f.split(',') if x.strip()]
    
      # Lithics
      cleaned_l = anvil.server.call('clean_commas', AaL_str)
      lList = [int(x.strip()) for x in cleaned_l.split(',') if x.strip()]
    
    except ValueError:
      print("Invalid input. Please enter numerical values separated by commas.")
      exit()
    print(fList)