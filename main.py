from tkinter import *

window = Tk()
window.geometry('800x500')
window.title('Translator Machine By Munyin')
window.resizable(False, False)
word = ''
translated = []
dictionary = {
    'ๅ': '1',
    '/': '2',
    '-': '3',
    'ภ': '4',
    'ถ': '5',
    'ุ': '6',
    'ึ': '7',
    'ค': '8',
    'ต': '9',
    'จ': '0',
    'ข': '-',
    'ช': '=',
    'ๆ': 'q',
    'ไ': 'w',
    'ำ': 'e',
    'พ': 'r',
    'ะ': 't',
    'ั': 'y',
    'ี': 'u',
    'ร': 'i',
    'น': 'o',
    'ย': 'p',
    'บ': '[',
    'ล': ']',
    'ฃ': '',
    'ฟ': 'a',
    'ห': 's',
    'ก': 'd',
    'ด': 'f',
    'เ': 'g',
    '้': 'h',
    '่': 'j',
    'า': 'k',
    'ส': 'l',
    'ว': ';',
    'ง': '',
    'ผ': 'z',
    'ป': 'x',
    'แ': 'c',
    'อ': 'v',
    'ิ': 'b',
    'ื': 'n',
    'ท': 'm',
    'ม': ',',
    'ใ': '.',
    'ฝ': '/',
    '+': '!',
    '๑': '@',
    '๒': '#',
    '๓': '$',
    '๔': '%',
    'ู': '^',
    '฿': '&',
    '๕': '*',
    '๖': '(',
    '๗': ')',
    '๘': '_',
    '๙': '+',
    '๐': 'Q',
    '': 'W',
    'ฎ': 'E',
    'ฑ': 'R',
    'ธ': 'T',
    'ํ': 'Y',
    '๊': 'U',
    'ณ': 'I',
    'ฯ': 'O',
    'ญ': 'P',
    'ฐ': '{',
    ',': ']',
    'ฤ': 'A',
    'ฆ': 'S',
    'ฏ': 'D',
    'โ': 'F',
    'ฌ': 'G',
    '็': 'H',
    '๋': 'J',
    'ษ': 'K',
    'ศ': 'L',
    'ซ': ':',
    '.': '',
    '(': 'Z',
    ')': 'X',
    'ฉ': 'C',
    'ฮ': 'V',
    'ฺ': 'B',
    '์': 'N',
    '?': 'M',
    'ฒ': '<',
    'ฬ': '>',
    'ฦ': '?',
    ' ': ' ' }

inv_dictionary = {v: k for k, v in dictionary.items()}

def Thai_to_Eng():
    global text
    text = entry_box.get()
    Thai_to_Eng_Command()
    return text


def Eng_to_Thai():
    global text
    text = entry_box.get()
    Eng_to_Thai_Command()
    return text


def Thai_to_Eng_Command():
    wordlist = list(text)
    count = len(wordlist)
    x = 0
    if x != count:
        for letter in text:
            loop = text[x]
            doneloop = dictionary[loop]
            translated.append(doneloop)
            x += 1
        
    if x == count:
        print('\nDone')
        sentence = ''.join(map(str, translated))
        print(sentence)
        Output = Text(window,height = 1, font= ('Arial', 14))
        Output.insert(1, sentence)
        Output.place(x=0, y=200)


def Eng_to_Thai_Command():
    inv_dictionary = (dictionary.items())
    wordlist = list(text)
    count = len(wordlist)
    x = 0
    if x != count:
        for letter in text:
            loop = text[x]
            doneloop = inv_dictionary[loop]
            translated.append(doneloop)
            x += 1
            
    if x == count:
        print('\nDone')
        sentence = ''.join(map(str, translated))
        print(sentence)
        
        Output = Text(window, height= 1,font = ('Arial', 14))
        Output.insert(1, sentence)
        Output.place(x=0,y=200)

starting = 'Welcome, The Keyboard Translator is ready\n----------------------\nType your Sentence'
starting_label = Label(window, text = starting, width = 50, font = ('Roman', 15))
starting_label.config(anchor= CENTER)
starting_label.pack()

entry_box = Entry(window,width=30, font=('Arial', 16))
entry_box.place(x=70,y= 100)
entry_box.pack()

button_1 = Button(window, text='Translate From Thai to English', command=Thai_to_Eng
                  , width = 20, font = ('Arial', 10), padx = 10, pady = 18)

button_1.place(x=50, y=400)

button_2 = Button(window, text='Translate from English to Thai', command= Eng_to_Thai,width= 20,
                  font=('Arial', 10), padx=10, pady=18)
button_2.place(x=250, y=400)


delete_button = Button(window, text='Clear', width=10, font=('Arial', 10), padx=2, pady=7)
delete_button.place(x=400, y=450)
window.mainloop()
