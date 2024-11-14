from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader
from gtts import gTTS
import requests
import os


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        file_loc_entry.delete(0, END)
    
        file_loc_entry.insert(0, file_path)


def convert_():
    reader = PdfReader(f'{file_loc_entry.get()}')

    # printing number of pages in pdf file
    print(len(reader.pages))

    page = reader.pages[7]
    text = page.extract_text()
    print(text)
    txt_in_str=""
    # print(reader.pages)

    for i in range(7):
        pg=reader.pages[i]
        txt=pg.extract_text()
        # print(txt)
        txt_in_str+=txt


    print(txt_in_str)

    mytext = txt_in_str

    
    language = 'en'

    
    myobj = gTTS(text=mytext, lang=language, slow=False)

    
    myobj.save("pdf_aud.mp3")

    
    os.system("start pdf_aud.mp3")


root=Tk()
root.title("Pdf to Audio")
root.minsize(500,100)
title=Label(text="PDF TO AUDIO CONVERT",font=("arial",30))
title.grid(column=1,columnspan=4,row=0)

file_loc=Label(text="PDF File Location:")
file_loc.grid(column=1,row=3)

file_loc_entry=Entry(width=20)
file_loc_entry.grid(column=2,row=3)

browse=Button(text="Browse",command=browse_file)
browse.grid(column=3,row=3)

covert=Button(text="Convert",command=convert_)
covert.grid(column=2,row=7,pady=30)
root.mainloop()