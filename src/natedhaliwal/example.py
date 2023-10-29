import json
import os
import random
import time
import sys
import requests

def display(text, colour=None):
  '''Displays text in the output, with the optional colour feature.'''
  empty = "\033[0m"
  bold = "\033[1m"
  italic = "\033[3m"
  underline = "\033[4m"
  grey = "\033[30m"
  red = "\033[31m"
  pink = "\033[32m"
  yellow = "\033[33m"
  blue = "\033[34m"
  purple = "\033[35m"
  green = "\033[36m"

  color_dict = {
    'empty': empty,
    'bold': bold,
    'italic': italic,
    'underline': underline,
    'grey': grey,
    'red': red,
    'pink': pink,
    'yellow': yellow,
    'blue': blue,
    'purple': purple,
    'green': green,
  }

  if colour:
    # Check if a color was specified
    formatted_text = color_dict.get(colour.lower())
    if formatted_text:
      # If the specified color is recognized, apply the formatting
      print(f'{formatted_text}{text}\033[0m')
    else:
      # If the specified color is not recognized, print an error message
      print('Unknown colour')
  else:
    # If no color was specified, print the text without any formatting
    print(text)


def clear():
  '''Clears the output to a blank screen.'''
  name=os.name
  if name=='nt':
    os.system('cls')
  elif name=='posix':
    os.system('clear')

def randnum(start,end):
  '''Gets a random number from the range given.'''
  return random.randint(start,end)

def randomlist(listName):
  '''Picks a random value of a list provided, either referenced or entered in the parentheses.'''
  return random.choice(listName)

def wait(seconds):
  '''Pauses the program for the specified number of seconds.'''
  time.sleep(seconds)

def scrape(website_url):
  '''Scrapes the given website and returns the data in json format.'''
  url = website_url 
  if not website_url.startswith("https://"):
    url = ('https://'+ url)
  r = requests.get(url)
  data = r.json()
  return data
  
def jsontodict(json_data):
  '''Converts the json data to a dictionary.'''
  return json.loads(json_data)

def dicttojson(dict_data):
  '''Converts the dictionary to json.'''
  return json.dumps(dict_data)

def overwritefile(filename,data):
  '''Writes the data to the specified file.'''
  try:
    with open(filename,'w') as file:
      file.write(data)
  except FileNotFoundError:
    return '\033[31mError: File not found\033[0m'

def writefile(filename,data):
  '''Adds the data to the specified file.'''
  try:
    with open(filename,'a') as f:
      f.write(data)
  except FileNotFoundError:
    return '\033[31mError: File not found\033[0m'

def createfile(filename):
  '''Creates a new file with the specified name.'''
  try:
    open(filename,'x')
  except FileExistsError:
    pass

def readfile(filename):
  '''Reads the specified file and returns the data.'''
  try:
    with open(filename,'r') as f:
      data=f.read()
    return data
  except FileNotFoundError:
    return '\033[31mError: File not found\033[0m'

def typewrite(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
