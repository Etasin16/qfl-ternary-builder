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
      qList = [float(x.strip()) for x in cleaned_q.split(',') if x.strip()]

      # Feldspar
      cleaned_f = anvil.server.call('clean_commas', AaF_str)
      fList = [float(x.strip()) for x in cleaned_f.split(',') if x.strip()]

      # Lithics
      cleaned_l = anvil.server.call('clean_commas', AaL_str)
      lList = [float(x.strip()) for x in cleaned_l.split(',') if x.strip()]

    except ValueError:
      alert("Invalid input. Please enter numerical values separated by commas.")
      exit()
    if len(qList) != len(fList) or len(qList) != len(lList):
      alert("Maybe some data is missing.")
      alert("Away, Here's the output with what we have")
    max_len = min(len(qList), len(fList), len(lList))

    qList = qList[:max_len]
    fList = fList[:max_len]
    lList = lList[:max_len]

    if not qList or not fList or not lList:
      alert("No valid data entered or uploaded.")
      exit()
    
    df = anvil.server.call('DataFrm1', qList, fList, lList)
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
      qList = [float(x.strip()) for x in cleaned_q.split(',') if x.strip()]

      # Feldspar
      cleaned_f = anvil.server.call('clean_commas', AaF_str)
      fList = [float(x.strip()) for x in cleaned_f.split(',') if x.strip()]

      # Lithics
      cleaned_l = anvil.server.call('clean_commas', AaL_str)
      lList = [float(x.strip()) for x in cleaned_l.split(',') if x.strip()]

    except ValueError:
      print("Invalid input. Please enter numerical values separated by commas.")
      exit()
    max_len = min(len(qList), len(fList), len(lList))

    qList = qList[:max_len]
    fList = fList[:max_len]
    lList = lList[:max_len]

    df = anvil.server.call('DataFrm', qList, fList, lList)
    csv_file = anvil.server.call('get_csv_download',df)
    anvil.media.download(csv_file)

  def file_loader_1_change(self, file, **event_args):
    self.DATAtable.visible = not self.DATAtable.visible
    self.PlotCard.visible = not self.PlotCard.visible
    if file:
      result = anvil.server.call('extract_QFL_from_csv', file)

      if isinstance(result, str) and result.startswith("ERROR"):
        alert(result)
      else:
        AaQ_str, AaF_str, AaL_str = result
        self.Quartz.text = AaQ_str
        self.Feldspar.text = AaF_str
        self.Lithics.text = AaL_str

    try:
      # Quartz
      cleaned_q = anvil.server.call('clean_commas', AaQ_str)
      qList = [float(x.strip()) for x in cleaned_q.split(',') if x.strip()]

      # Feldspar
      cleaned_f = anvil.server.call('clean_commas', AaF_str)
      fList = [float(x.strip()) for x in cleaned_f.split(',') if x.strip()]

      # Lithics
      cleaned_l = anvil.server.call('clean_commas', AaL_str)
      lList = [float(x.strip()) for x in cleaned_l.split(',') if x.strip()]

    except ValueError:
      alert("Invalid input. Please enter numerical values separated by commas.")
      exit()
    if len(qList) != len(fList) or len(qList) != len(lList):
      alert("Maybe some data is missing.")
      alert("Any way, Here's the output with what we have")
    max_len = min(len(qList), len(fList), len(lList))

    qList = qList[:max_len]
    fList = fList[:max_len]
    lList = lList[:max_len]

    if not qList or not fList or not lList:
      alert("No valid data entered or uploaded.")
      exit()

    df = anvil.server.call('DataFrm1', qList, fList, lList)
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


    
