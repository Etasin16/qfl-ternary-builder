import anvil.server
anvil.server.connect("server_JZOCNSMKQ47PWJCHFIFMA7JI-GNGZTW2B2JR4ERZQ")
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.media
import pandas as pd
import matplotlib.pyplot as plt
import mpltern

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#

# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
@anvil.server.callable
def hello():
  return "Hello from Render!"

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
def DataFrm1(d1,d2,d3):
  # Creating dataframe using inputed data
  df = pd.DataFrame({'Quartz': d1, 'Feldspar': d2, 'Lithics': d3})
  # calculation
  df['Total'] = df['Quartz'] + df['Feldspar'] + df['Lithics']
  
  df['%Q'] =  df['Quartz'] / df['Total'] * 100
  df['%F'] =  df['Feldspar'] / df['Total'] * 100
  df['%L'] =  df['Lithics'] / df['Total'] * 100
  df = df.round(2)
  return df.to_dict(orient='records')

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
    headers = list(dss[0].keys())
  
    # Step 2: Create CSV rows
    csv_rows = [",".join(headers)]  # Header row
    for row in dss:
      csv_rows.append(",".join(str(row[h]) for h in headers))
    
      # Step 3: Combine rows into single CSV string
      csv_string = "\n".join(csv_rows)
    return anvil.BlobMedia("text/csv", csv_string.encode("utf-8"), name="data.csv")

@anvil.server.callable
def ModelPlotPrymary(d1,d2,d3):
    df = pd.DataFrame({'Quartz': d1, 'Feldspar': d2, 'Lithics': d3})
    # calculation
    df['Total'] = df['Quartz'] + df['Feldspar'] + df['Lithics']
  
    df['%Q'] =  df['Quartz'] / df['Total'] * 100
    df['%F'] =  df['Feldspar'] / df['Total'] * 100
    df['%L'] =  df['Lithics'] / df['Total'] * 100
  
    fig = plt.figure()
    ax = fig.add_subplot(projection='ternary')

    # setting_labels and scale
    ax.set_tlabel("Quartz")
    ax.set_llabel("Feldspar")
    ax.set_rlabel("Lithics")

    tick_vals = [0, 20, 40, 60, 80, 100]

    ax.taxis.set_ticklabels(tick_vals)
    ax.laxis.set_ticklabels(tick_vals)
    ax.raxis.set_ticklabels(tick_vals)

    # plotting data points
    ax.plot(df['%Q'], df['%F'], df['%L'], 'ko', label='Data Points') # 'ko' means black circles

    # legend and griding
    ax.legend(fontsize='small')
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='gray')

    file_path = "/tmp/ternary_plot.png"
    fig.savefig(file_path)
    plt.close(fig)
    
    with open(file_path, "rb") as f:
      img_bytes = f.read()

    return anvil.BlobMedia("image/png", img_bytes, name="ternary_plot.png")

@anvil.server.callable
def ModelProvenence(d1,d2,d3):
    df = pd.DataFrame({'Quartz': d1, 'Feldspar': d2, 'Lithics': d3})
    # calculation
    df['Total'] = df['Quartz'] + df['Feldspar'] + df['Lithics']
  
    df['%Q'] =  df['Quartz'] / df['Total'] * 100
    df['%F'] =  df['Feldspar'] / df['Total'] * 100
    df['%L'] =  df['Lithics'] / df['Total'] * 100
  
    fig = plt.figure()
    ax = fig.add_subplot(projection='ternary')
  
    # setting_labels and scale
    ax.set_tlabel("Quartz")
    ax.set_llabel("Feldspar")
    ax.set_rlabel("Lithics")
  
    tick_vals = [0, 20, 40, 60, 80, 100]
  
    ax.taxis.set_ticklabels(tick_vals)
    ax.laxis.set_ticklabels(tick_vals)
    ax.raxis.set_ticklabels(tick_vals)


    provenance_fields = {
    'Basement Uplift': [(100,0,0),(0,100,0),(0,85,15),(96,0,4)],
    'Recycled Orogen': [(25, 0, 75),(51,40,9),(96,0,4)],
    'Undissected Arc': [(0, 50, 50), (25, 0, 75),(0,0,100)],
    'Transitional Arc': [(0, 50, 50), (25, 0, 75),(33,12,55),(17,70,13),(0,85,15)],
    'Dissected Arc'  : [(51,40,9),(17,70,13),(33,12,55)]
  }

  #colors = {
  #    'Basement Uplift': 'green',
  #    'Recycled Orogen': 'orange',
  #    'Undissected Arc': 'brown',
  #    'Transitional Arc': 'teal',
  #    'Dissected Arc'  : 'olive'
  #}

    colors = {
    'Basement Uplift': 'lightyellow',
    'Recycled Orogen': 'skyblue',
    'Undissected Arc': 'cyan',
    'Transitinal Arc': 'lightgreen',
    'Dissected Arc'  : 'lightblue'
    }

  # Plotting provenance fields as shaded regions
    for label, vertices in provenance_fields.items():
      # Convert percentage to the required format for fill
      fill_vertices = [(v[0]/100, v[1]/100, v[2]/100) for v in vertices]
      ax.fill(*zip(*fill_vertices), label=label, alpha=0.3 ,color=colors.get(label))

    # plotting data points
    ax.plot(df['%Q'], df['%F'], df['%L'], 'ko', label='Data Points') # 'ko' means black circles
  
    # legend and griding
    ax.legend(fontsize='small',loc='upper left', bbox_to_anchor=(0.8, 1))
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='gray')
  
    file_path = "/tmp/ternary_plot_PROV.png"
    fig.savefig(file_path)
    plt.close(fig)
    
    with open(file_path, "rb") as f:
      img_bytes = f.read()

    return anvil.BlobMedia("image/png", img_bytes, name="ternary_plot_PROV.png")

@anvil.server.callable
def extract_QFL_from_csv(file):
  # Step 1: Get CSV contents as string
  csv_str = file.get_bytes().decode('utf-8')

  # Step 2: Split into lines
  lines = csv_str.strip().split('\n')
  headers = lines[0].split(',')

  # Step 3: Get column indexes
  try:
    q_idx = headers.index('Quartz')
    f_idx = headers.index('Feldspar')
    l_idx = headers.index('Lithics')
  except ValueError as e:
    return f"ERROR: Missing required column: {e}"

    # Step 4: Parse values into separate lists
  q_vals, f_vals, l_vals = [], [], []
  for line in lines[1:]:
    cells = line.split(',')
    if len(cells) >= max(q_idx, f_idx, l_idx) + 1:
      q_vals.append(cells[q_idx].strip())
      f_vals.append(cells[f_idx].strip())
      l_vals.append(cells[l_idx].strip())

    # Step 5: Create comma-separated strings
  AaQ_str = ', '.join(q_vals)
  AaF_str = ', '.join(f_vals)
  AaL_str = ', '.join(l_vals)

  return AaQ_str, AaF_str, AaL_str

anvil.server.wait_forever()

