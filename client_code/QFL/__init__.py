from ._anvil_designer import QFLTemplate
from anvil import *
import plotly.graph_objects as go
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
    self.DATAtable.visible = not self.DATAtable.visible
    self.PlotCard.visible = not self.PlotCard.visible
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
    if len(qList) != len(fList) or len(qList) != len(lList):
      print("Maybe some data is missing.")
      print("Any way, Here's the output with what we have")
    max_len = min(len(qList), len(fList), len(lList))

    qList = qList[:max_len]
    fList = fList[:max_len]
    lList = lList[:max_len]

    if not qList or not fList or not lList:
      print("No valid data entered or uploaded.")
      exit()
    print(qList,fList,lList)
    df = anvil.server.call('DataFrm', qList, fList, lList)
    self.repeating_panel_1.items = df

    #ploting
    plot_image = anvil.server.call('ModelPlotPrymary', qList, fList, lList )
    if isinstance(plot_image, anvil.BlobMedia):
      self.image_1.source = plot_image
    else:
      alert(f"Unexpected server response: {plot_image}")

    plot_Prov = anvil.server.call('ModelProvenence', qList, fList, lList )
    if isinstance(plot_Prov, anvil.BlobMedia):
      self.image_2.source = plot_Prov
    else:
      alert(f"Unexpected server response: {plot_Prov}")
    

  def DownloadCSV_click(self, **event_args):
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
    if len(qList) != len(fList) or len(qList) != len(lList):
      print("Maybe some data is missing.")
      print("Any way, Here's the output with what we have")
    max_len = min(len(qList), len(fList), len(lList))

    qList = qList[:max_len]
    fList = fList[:max_len]
    lList = lList[:max_len]

    if not qList or not fList or not lList:
      print("No valid data entered or uploaded.")
      exit()
    df = anvil.server.call('DataFrm', qList, fList, lList)
    print(df)
    csv_file = anvil.server.call('get_csv_download',df)
    anvil.media.download(csv_file)

    

    
