from os import system as syst
from time import sleep


def layout():
    syst('cls')
    print("*"*97)
    print("* "*20+" M I N I G R A M "+' *'*20)
    print('*'*97+'\n')

def lazy_loading(Start,Text,Time):
    sleep(Start)
    for i in range(Time):
        layout()
        print(Text+' in '+str(Time-i)+' seconds....')
        sleep(1)

