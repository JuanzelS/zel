# cli-games/asciiart.py
import requests

r = requests.get('http://artii.herokuapp.com/make?text=Awesomesauce')
print(r.text)
import requests

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
print(r.text)
import requests

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)
data = requests.get('http://artii.herokuapp.com/fonts_list')
print(data)
fontsArray = data.text.split('\n')
# cli-games/asciiart.py
import requests
import random

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')
font = random.choice(fontsArray)
print(font)

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)
...

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')

for i in range(3):
  font = random.choice(fontsArray)
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
  print("Font:", font)
  print(r.text)
  # cli-games/asciiart.py
import requests
import random

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

if font == "":
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
  print("Font: default")
  print(r.text)
  if font:
  font = font
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
  print("Font:", font)
  print(r.text)
  if font == "random":
  data = requests.get('http://artii.herokuapp.com/fonts_list')
  fontsArray = data.text.split('\n')

  for i in range(3):
      font = random.choice(fontsArray)
      r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
      print("Font:", font)
      print(r.text)
      def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)
      for i in range(3):
      font = random.choice(fontsArray)
      getAsciiArt(text, font)
      
      # cli-games/asciiart.py
import requests
import random

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')
font = random.choice(fontsArray)
print(font)

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text