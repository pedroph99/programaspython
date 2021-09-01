from tkinter import *


class descanso:
    def __init__(self):
        self.root=Tk()
        self.frame=Frame(self.root)
        self.frame.pack()
        self.canvas=Canvas(self.frame, width=400, height=400)
        self.canvas['bg']='black'
        self.canvas.pack()
        self.posx=10
        self.posy=10
        self.vx=5
        self.vy=4
        self.canvas.create_oval(self.posx,self.posy,self.posx+90,self.posy+90, tag='bola', fill='yellow')
        self.canvas.create_oval(self.posx+20,self.posy+20,self.posx+40,self.posy+40, tag='bola', fill='darkblue')
        self.canvas.create_oval(self.posx+50,self.posy+20,self.posx+70,self.posy+40, tag='bola', fill='darkblue')
        self.canvas.create_line(self.posx+20,self.posy+60,self.posx+40,self.posy+80,self.posx+ 75,self.posy+60, smooth="true")
        self.velocidadex=5
        old_x0=10

        old_x1=30

        space=10

        delta=20

        self.lista=[]

        for x in range(7):
            if x==0:
                a=self.canvas.create_rectangle(10, 20, 30, 40, fill='green')
                self.lista.append(a)
            else:
                a=self.canvas.create_rectangle(10+(x*30),20, 30+(x*30),40, fill='green')
                self.lista.append(a)
        self.velocidadey=10
        self.botao=Button(self.root,text='teste')
        self.botao.pack()
        self.jogar=True
        self.jogo()
        self.root.mainloop()
        self.teste=[None, None, None, None]
    def jogo(self):
        if self.jogar:
            self.update()
            self.draw()
            self.localiza()

            self.root.after(20, self.jogo)                
            
            
    def localiza(self):
            
            self.cordenada=self.canvas.bbox('bola')
            self.colisao=self.canvas.find_overlapping(*self.cordenada)
            p=self.canvas.find_closest(self.cordenada[0], self.cordenada[1])
            if p[0] in self.lista:
                print('ok')
                self.canvas.delete(p[0])
        
    def draw(self):
        self.canvas.delete('bola')
        self.canvas.create_oval(10+self.posx,10+self.posy,100+self.posx,100+self.posy, tag='bola', fill='yellow')
        self.canvas.create_oval(self.posx+20,self.posy+20,self.posx+40,self.posy+40, tag='bola', fill='darkblue')
        self.canvas.create_oval(self.posx+50,self.posy+20,self.posx+70,self.posy+40, tag='bola', fill='darkblue')
        self.canvas.create_line(self.posx+20,self.posy+60,self.posx+40,self.posy+80,self.posx+ 75,self.posy+60, smooth="true")

    def update(self):
        self.posx+=self.vx
        self.posy+=self.vy
        if self.posx+90  >=400:
            self.vx*=-1
        if self.posy+90 >=400:
            self.vy*=-1
        if self.posx <=-10:
            self.vx *=-1
        if self.posy <=0:
            self.vy *=-1
            


teste=descanso()
