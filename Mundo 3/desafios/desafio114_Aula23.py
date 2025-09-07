#crie um códiog em python que teste se o site pudim está acessivel pelo computador usado
import requests

try:
    r= requests.get('https://www.pudim.com.br/')
except:
    print('\033[31mO site Pudim está inacessivel\033[m')
else:
    print('\033[33mO site Pudim está acessivel\033[m')