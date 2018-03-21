'''

Python - Web crawler

2018-03-20

vídeo no youtube https://www.youtube.com/watch?v=tuI_Z6VolbE

crawler utilizando BS4 (Beautiful Soup)

define a função extract_title, que recebeo conteudo de uma página html.
instancia a classe BeautifulSoup com o conteudo, utilizando o parser lxml

procura a tag title com texto dentro dela

verifica se a tag não é nula, e então retorna a string dessa tag

o programa final procura, de forma recursiva, todos os links de uma página, e faz um print do titulo da pagina e da sua url

'''


from bs4 import BeautifulSoup
import requests

def extract_title(content):
  soup = BeautifulSoup(content, "lxml")
  tag = soup.find("title", text=True)

  if not tag:
    return None
  
  # strip é um trim da string
  return tag.string.strip() 

def extract_links(content):
  soup = BeautifulSoup(content, "lxml")
  # set é um conjunto/array, sem elementos duplicados
  links = set()

  for tag in soup.find_all("a", href=True):
    # não considera links relativos, só links diretos
    if tag['href'].startswith("http"):
      links.add(tag['href'])

  return links

def crawl(start_url):
  seen_urls = set([start_url])
  available_urls = set([start_url])

  while available_urls:
    url = available_urls.pop()

    try:
      content = requests.get(url, timeout=3).text 
    except Exception:
      continue
    
    title = extract_title(content)

    if title:
      print(title)
      print(url)
      print()

    for link in extract_links(content):
      if link not in seen_urls:
        seen_urls.add(link)
        available_urls.add(link)

try:
  crawl("https://www.python.org/")
except KeyboardInterrupt:
  print()
  print("Bye!")

