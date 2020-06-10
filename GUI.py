import tkinter
from tkinter import Tk, Frame, Label, Button, Entry, LEFT


# nessa classe serão criados os controles que serão exibidos na tela
class Application():
    
    def __init__(self, master=None):
        
        self.font = ('Arial', '10')

        # criando containers
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2['padx'] = 35
        self.container2['pady'] = 10
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3['pady'] = 10
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['pady'] = 10
        self.container4.pack()

        # título
        self.titulo = Label(self.container1, text='WIN10')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()
        self.titulo2 = Label(self.container1, text='Salvar fotos da tela de entrada')
        self.titulo2['font'] = ('Arial', '10', 'bold')
        self.titulo2.pack()

        # linha de inserção do usuário
        self.usuario_label = Label(self.container2, text='Digite o nome de usuário do Win10: ')
        self.usuario_label['font'] = self.font
        self.usuario_label.pack(side=LEFT)

        self.usuario = Entry(self.container2, font=self.font, width=30)
        self.usuario.pack(side=LEFT)

        # botão para dar continuidade
        self.button = Button(self.container3, text='Enviar', font=('Arial', 10, 'bold'))
        self.button['command'] = self.save_pics
        self.button.pack()

        # verificador de status
        self.status = Label(self.container4, text='', font=self.font)
        self.status.pack()

    def save_pics(self):
        from time import sleep
        import win10images
        user = self.usuario.get()
        try:
            win10images.save_pictures(user)
        except Exception:
            self.status['text'] = 'Ocorreu um erro. Não conseguimos salvar as fotos.'
        else:
            self.status['text'] = 'Copiando arquivos para pasta destino...'
            sleep(2)
            self.status['text'] = 'Renomeando extensão dos arquivos...'
            sleep(2)
            self.status['text'] = 'Removendo arquivos desnecessários...'
            sleep(2)
            self.status['text'] = 'Pronto! As fotos foram salvas na pasta "Fotos Windows 10" na Área de Trabalho.'


# a classe Tk() permite que os widgets sejam utilizados
root = Tk()
# passamos root como parametro do método construtor da Application
Application(root)
# mainloop faz a tela de interface ser exibida
root.mainloop()
