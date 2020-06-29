# Game Ping-Pong

# Importando a bibliotecas que serão utilizadas
from tkinter import * 
import random
import time

# Solicita o nível ao usuário
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
# Variável length recebe 500 dividido pelo level inserido pelo usuário
length = 500/level


root = Tk() # Não sei
root.title("Ping Pong") # Está atribuindo um titulo ao root
root.resizable(0,0) # definindo o tamanho de alguma coisa
root.wm_attributes("-topmost", -1)  # Não sei

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)  # Não sei
canvas.pack()  # Não sei

root.update() # Atualizando root

count = 0 # cont recebe 0
lost = False # Lost igual a Falso

class Bola: # Criando a classe Bola
    def __init__(self, canvas, Barra, color): # Definindo os valores da classe Bola
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self): # Definindo o métodos da classe Bola 
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra:  # Definindo a classe Barra 
    def __init__(self, canvas, color): # Definindo os valores de Barra 
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):   # Definindo os métodos de Barra
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):   # Definindo os métodos de Barra
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):   # Definindo os métodos de Barra
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):  # Criando uma função de start game
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score(): # Função de Score
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over(): # Função Game Over 
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()