import os

def run():
  print('start.py:run')
  resu = os.system('bash ./update.sh')
  return resu
