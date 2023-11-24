from tkinter import *

window = Tk()
window.geometry('800x500')
window.title('Translator Machine By Munyin')
window.resizable(False, False)


# the place we store info

word = ''
translated = []

dict_origin = {
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

dict_swap = {v: k for k, v in dict_origin.items()}

# define functions

def thai_to_eng():
    global text
    text = entry_box.get()
    Thai_to_Eng_Command()
    return text

def eng_to_thai():
    global text
    text = entry_box.get()
    Eng_to_Thai_Command()
    return text

# converting
    
def Eng_to_Thai_Command():
    word = list(text)
    count = len(text)
    
    x = 0

    if x != count:
        for letters in text:
            index = text[x]
            value = dict_swap[index]
            translated.append(value)
        
            x += 1

    if x == count:
        sentence = ''.join(map(str, translated))     

        Output.insert('1.0', sentence)
        Output.place(x=10,y=300)
        
        translated.clear()




def Thai_to_Eng_Command():
    word = list(text)
    count = len(text)
    
    x = 0

    if x != count:
        for letters in text:
            index = text[x]
            value = dict_origin[index]
            translated.append(value)
        
            x += 1

    if x == count:
        sentence = ''.join(map(str, translated))     
        
        Output.insert('1.0', sentence)
        Output.place(x=10,y=300)
        
        translated.clear()

        
def copy_text_to_clipboard(event=None):
    # Get the selected text from the Text widget
    selected_text = Output.get("1.0", "end-1c")

    # Copy the selected text to the clipboard
    window.clipboard_clear()
    window.clipboard_append(selected_text)
    window.update()


# Welcome Text

welcome = 'Welcome, This is a Demo for a keyboard translator'
welcome_label = Label(window, text = welcome, font = ('Segoe UI', 10))
welcome_label.config(anchor= 'w')
welcome_label.place(x=10,y=10)




# Header

header = 'Type your Sentence'
header_label = Label(window, text = header, font = ('Segoe UI', 18))
header_label.config(anchor= 'w')
header_label.place(x=10,y=30)

# Entry Box

entry_box = Entry(window,width=30, font=('Arial', 16))
entry_box.place(x=10,y= 80)

# Buttons

label_button = Label(window, text = 'Translate From : ', bg ='light gray', bd = 1, relief = FLAT, pady = 1, height=1)
label_button.place(x=10,y=140)

button_1 = Button(window, text='Thai to English', command= thai_to_eng
                  , width = 15, font = ('Arial', 10), bg ='light gray', bd = 1, relief = RIDGE, height=2)
button_1.place(x=110,y= 130)

button_2 = Button(window, text='English to Thai', command= eng_to_thai
                  , width = 15, font = ('Arial', 10), bg ='light gray', bd = 1, relief = RIDGE, height=2)
button_2.place(x=250,y= 130)

Output = Text(window, height = 1,width=50, font= ('Segoe UI', 18))

button_Clear = Button(window, text='Clear and Copy', command= copy_text_to_clipboard 
                  , width = 15, font = ('Arial', 10), bg ='light gray', bd = 1, relief = RIDGE, height=2)
button_Clear.place(x=390,y=130)

button_Clear.bind("<Control-c>", copy_text_to_clipboard)




window.mainloop()