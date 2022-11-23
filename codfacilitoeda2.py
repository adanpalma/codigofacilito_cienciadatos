# %%
import os
import zipfile 
from  pathlib  import Path
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as request
from tqdm import tqdm
import html5lib 



# %%
url_datos = "https://portal.inmet.gov.br/dadoshistoricos"
datos_html = request.get(url_datos).content

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/106.0'
}
datos_html = request.get(url_datos, headers=headers).content


soup = bs(datos_html,"html5lib")
#print(soup.prettify())
links = [
    link.get("href")
    for link in soup.find_all("a")
    if "zip" in (link.get("href") if link.get("href") else "")
  ]
print(links)
# %%
def download_progressbar_files(url):
  response = request.get(url,stream=True)
  total_size_in_bytes = int(response.headers.get("content-length",0))
  block_size = 1024
  progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
  
  
  with open(Path(url).name, "wb") as file:
    for data in response.iter_content(block_size):
      progress_bar.update(len(data))
      file.write(data)
  progress_bar.close()


for url_file in links:
  download_progressbar_files(url_file)


#%%
try:
  os.makedirs("csv_2020")
except:
  pass
finally:
  pass

filename = '2022.zip'
with zipfile.ZipFile(filename, "r") as zip_ref:
  filename_date_size = [ zip_ref.printdir() ]
  print(filename_date_size[2:])
  #zip_ref.extractall("csv_2020")

# %%
