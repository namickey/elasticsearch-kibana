#encoding: utf-8

#sudo apt install scrot
#sudo apt install python3-tk
#sudo apt install python3-dev
#pip install pyautogui
#sudo apt-get install xclip
#pip install pyperclip

import pyautogui
pyautogui.PAUSE=1
import time
import pyperclip

def search(keyword):

    pyautogui.click(200, 151)
    time.sleep(1)

    pyautogui.click(459, 227) #70%〜100%

    pyperclip.copy(keyword)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.typewrite(['enter'])
    time.sleep(1)
    #un = pyautogui.locateAllOnScreen('unlimited_100.png') #100%
    un = pyautogui.locateAllOnScreen('unlimited_70.png')  #70%
    list = []
    for u in un:
        list.append((u[0], u[1]))
    if un:
        return list
    return un

def read():
    list=[]
    for x in open('data.txt'):
        x = trimR(x, ' (')
        x = trimR(x, '【')
        x = trimR(x, '読んだ本')
        x = trimL(x, '】')
        list.append(x.strip())
    return list

def trimR(x, word):
    pos = x.find(word)
    res = x.strip()
    if pos > 0:
        res = x[:pos]
    return res

def trimL(x, word):
    pos = x.find(word)
    res = x.strip()
    if pos > 0:
        res = x[pos+1:]
    return res

def loop():
    list = read()
    res = []
    for x in list: #limited
        print(x)
        r = search(x)
        if r:
            res.append((1, len(r), x, r))
        else:
            res.append((0, 0, x, r))
    print('***************************')
    a = open('a.txt', 'w')
    for x in res:
        print(x)
        a.write(str(x) + '\n')
loop()
