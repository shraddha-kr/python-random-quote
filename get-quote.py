import random

def primary():
  # print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  # To print first quote
  # print(quotes[0])
  
  # To print last quote 
  # last = len(quotes)-1
  # print(quotes[last])
  
  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  
  # print(quotes)
  
if __name__== "__main__":
  primary()
