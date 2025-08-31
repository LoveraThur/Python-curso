#Crie um pacote chamado UtilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando

from UtilidadesCeV import Moeda

valor = float(input('Digite o Preço: R$'))
Moeda.resumo(valor, 20, 12)