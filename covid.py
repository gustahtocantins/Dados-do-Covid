import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import PhotoImage
win = Tk()
win.maxsize(width=500, height=400)
win.minsize(width=500, height=400)
win.title("Dados sobre o Covid-19 no Brasil")

imagem = PhotoImage(file="covid19.png")
ba = Label(win, image=imagem)
ba.grid()
ba.place(bordermode=OUTSIDE, y = -40, x=-20)
#titulo
titulo = Label(win, text="DADOS COVID-19")
titulo["fg"], titulo["bg"] = "white", "blue"
titulo["font"] = ("arial", "30", "bold")
titulo.grid()
titulo.place(bordermode=OUTSIDE, x=75, y=20)

#casos confirmados
confirmado = Label(win, text="Confirmados: ")
confirmado["fg"], confirmado["bg"] = "white", "red"
confirmado["font"] = ("arial", "25", "bold")
confirmado.grid()
confirmado.place(bordermode=OUTSIDE, x=20, y=100)
#mortes
mortes = Label(win, text="Mortes: ")
mortes["fg"], mortes["bg"] = "white", "black"
mortes["font"] = ("arial", "25", "bold")
mortes.grid()
mortes.place(bordermode=OUTSIDE, x=20, y=180)
#recuperados
recuperados = Label(win, text="Recuperados: ")
recuperados["fg"], recuperados["bg"] = "white", "green"
recuperados["font"] = ("arial", "25", "bold")
recuperados.grid()
recuperados.place(bordermode=OUTSIDE, x=20, y=260)
#pesquisar numeros
def editar():
    url = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
    html = BeautifulSoup(url.text,"html.parser")
    s = html.find_all("div", {"class":"maincounter-number"})
    confirmado["text"] = f"Confirmados: {s[0].text[1:-1]}"
    mortes["text"] = f"Mortes: {s[1].text[1:-1]}"
    recuperados["text"] = f"Recuperados: {s[2].text[1:-1]}"
#botão
atualizar = Button(win, text="Atualizar", command=editar)
atualizar["fg"], atualizar["bg"] = "white", "blue"
atualizar["font"] = ("arial", "20", "bold")
atualizar.grid()
atualizar.place(bordermode=OUTSIDE, x=170, y=324)

win.mainloop()
