from ._anvil_designer import QFLTemplate
from anvil import *

class QFL(QFLTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.InputArea.visible = not self.InputArea.visible

  def INPUTarea(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    
