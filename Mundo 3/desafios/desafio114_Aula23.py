#crie um códiog em python que teste se o site pudim está acessivel pelo computador usado
import requests

try:
    r= requests.get('https://www.pudim.com.br/')
    print('\033[33mO site pudim está acessivel\033[m')
except:
    print('\033[31mO site pudim está inacessivel\033[m')
