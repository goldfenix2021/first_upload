import os

def run():
  print('start.py:run')
  #resu = os.system('bash ./update.sh')
  resus = list()
  res = os.system('apt-get install python3-pip')
  resus.append(res)
  res = os.system('python3 -m pip install beautifulsoup4')
  resus.append(res)
  return resus


resu = run()
for i in resu:
  print(i)
