import tkinter as tk
from typing import Union

FONT1 = "Arial 15 bold"
FONT2 = "Arial 11 bold"


class UrnaApp(tk.Tk):
    def __init__(self, eleitores, candidatos):
        super().__init__()

        self.titulo = ""
        self.frame_atual : str
        self.gui : Union[TituloFrame, VotoFrame]
        self.eleitores = eleitores
        self.candidatos = candidatos

        self.title("Urna Eletronica")
        self.geometry('780x500')
        self.configure(background="#D9D9D9")

        tela = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        tela.pack(side="left", padx=(15, 0), pady=15)
        TecladoFrame(self)

        self.frames = {}  # Dicionario onde a chave = nome da classe

        # Itera sobre uma tupla de diferntes layouts de paginas e adiciona elas no dicionario
        for F in (TituloFrame, VotoFrame, ErroFrame):
            page_name = F.__name__
            frame = F(parent=tela, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("TituloFrame")

    # Mostra o frame atual passado como parametro
    def show_frame(self, page_name):
        self.gui = self.frames[page_name]
        self.gui.tkraise()
        self.frame_atual = page_name

    def update_display_candidato(self, voto):
        if voto == 0:
            self.gui.candidato_display.config(text="Branco")

        elif voto in self.candidatos:
            self.gui.candidato_display.config(text=self.candidatos[voto].get_nome())

        else:
            self.gui.candidato_display.config(text="Nulo")

    def press(self, num):
        if self.frame_atual == "TituloFrame":
            self.titulo += num
            self.gui.titulo_entry.set(self.titulo)

            if int(self.titulo) in self.eleitores:
                self.gui.eleitor_display.config(text=self.eleitores[int(self.titulo)], font=FONT2)

            elif int(self.titulo) not in self.eleitores:
                self.gui.eleitor_display.config(text="Insira um Titulo de Eleitor", font=FONT1)

        elif self.frame_atual == "VotoFrame":
            if not self.gui.dgt1.get():
                self.gui.dgt1.set(num)

            elif not self.gui.dgt2.get():
                self.gui.dgt2.set(num)

                voto = int(self.gui.dgt1.get() + self.gui.dgt2.get())
                self.update_display_candidato(voto)

    def confirma(self):
        if self.frame_atual == "TituloFrame":
            try:
                if int(self.titulo) in self.eleitores:
                    self.frames["VotoFrame"].candidato_display.config(text="")
                    self.titulo = ""
                    self.gui.titulo_entry.set("")
                    self.gui.eleitor_display.config(text="Insira um Titulo de Eleitor", font=FONT1)
                    self.show_frame("VotoFrame")
                else:
                    raise Exception

            except(ValueError, Exception):
                self.titulo = ""
                self.gui.titulo_entry.set("")
                self.show_frame("ErroFrame")

        elif self.frame_atual == "VotoFrame":
            if self.gui.dgt1.get() and self.gui.dgt2.get():
                self.gui.dgt1.set("")
                self.gui.dgt2.set("")
                self.gui.candidato_display.config(text="Concluido!!!")
                self.after(1000, lambda: (self.gui.candidato_display.config(text=""), self.show_frame("TituloFrame")))

        elif self.frame_atual == "ErroFrame":
            self.show_frame("TituloFrame")

    def corrige(self):
        if self.frame_atual == "TituloFrame":
            self.gui.titulo_entry.set("")
            self.titulo = ""
            self.gui.eleitor_display.config(text="Insira um Titulo de Eleitor", font=FONT1)

        elif self.frame_atual == "VotoFrame":
            self.gui.dgt1.set("")
            self.gui.dgt2.set("")
            self.gui.candidato_display.config(text="")

    def branco(self):
        if self.frame_atual == "VotoFrame":
            self.gui.dgt1.set("0")
            self.gui.dgt2.set("0")
            self.gui.candidato_display.config(text="Branco")


class TituloFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.titulo_entry = tk.StringVar()
        self.configure(background="#E8E8E8")

        self.eleitor_display = tk.Label(self, text="Insira um Titulo de Eleitor", font=FONT1, background="#E8E8E8")
        self.eleitor_display.pack(side="top", pady=(85, 35))
        titulo = tk.Entry(self, font=FONT1, textvariable=self.titulo_entry, justify="center", state="disabled",
                               disabledforeground="black")
        titulo.pack()


class VotoFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.dgt1 = tk.StringVar()
        self.dgt2 = tk.StringVar()

        self.configure(background="#E8E8E8")

        frame_nome = tk.Frame(self, background="#E8E8E8")
        frame_nome.pack(side="top")

        self.candidato_display = tk.Label(frame_nome, font=FONT1, background="#E8E8E8")
        self.candidato_display.grid(row=1, column=0, pady=(75, 0), padx=100)

        voto_entry = tk.Frame(self, background="#E8E8E8")
        voto_entry.pack(side="bottom")

        digit1_entry = tk.Entry(voto_entry, width=2, font=FONT1, textvariable=self.dgt1, justify="center",
                                     state="disabled", disabledforeground="black")
        digit1_entry.pack(side="left", padx=(200, 5), pady=(25, 100))
        digit2_entry = tk.Entry(voto_entry, width=2, font=FONT1, textvariable=self.dgt2, justify="center",
                                     state="disabled", disabledforeground="black")
        digit2_entry.pack(side="right", padx=(0, 200), pady=(25, 100))


class ErroFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background="#E8E8E8")

        error_msg1 = tk.Label(self, text="Titulo digitado invalido!!!", font=FONT1, background="#E8E8E8")
        error_msg1.pack(pady=(100, 5))
        error_msg2 = tk.Label(self, text="Pressione 'Confirma' para retornar a tela anterior", font="Arial 12",
                                   background="#E8E8E8")
        error_msg2.pack()


class TecladoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(side="right", padx=15)
        self.configure(background="#D9D9D9")

        num_keys = tk.Frame(self, background="#D9D9D9")
        num_keys.pack(side="top", padx=(0, 12))

        btn1 = tk.Button(num_keys, text="1", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("1"))
        btn1.grid(row=10, column=10)

        btn2 = tk.Button(num_keys, text="2", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("2"))
        btn2.grid(row=10, column=11, padx=5)

        btn3 = tk.Button(num_keys, text="3", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("3"))
        btn3.grid(row=10, column=12)

        btn4 = tk.Button(num_keys, text="4", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("4"))
        btn4.grid(row=11, column=10, pady=5)

        btn5 = tk.Button(num_keys, text="5", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("5"))
        btn5.grid(row=11, column=11, padx=5, pady=5)

        btn6 = tk.Button(num_keys, text="6", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("6"))
        btn6.grid(row=11, column=12, pady=5)

        btn7 = tk.Button(num_keys, text="7", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("7"))
        btn7.grid(row=12, column=10)

        btn8 = tk.Button(num_keys, text="8", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("8"))
        btn8.grid(row=12, column=11, padx=5)

        btn9 = tk.Button(num_keys, text="9", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("9"))
        btn9.grid(row=12, column=12)

        btn0 = tk.Button(num_keys, text="0", foreground="#ffffff", background="#211C18", font=FONT2, justify="center",
                              activebackground="#211C18", activeforeground="#ffffff", command=lambda: parent.press("0"))
        btn0.grid(row=14, column=11, pady=5)

        action_keys = tk.Frame(self, background="#D9D9D9")
        action_keys.pack(side="bottom")

        btn_branco = tk.Button(action_keys, text="BRANCO", background="#ffffff", font=FONT2, justify="center",
                                   activebackground="#ffffff", activeforeground="#000000", command=lambda: parent.branco())
        btn_branco.grid(row=15, column=10, padx=(5, 0))

        btn_corrige = tk.Button(action_keys, text="CORRIGE", background="#DE5B0D", font=FONT2, justify="center",
                                    activebackground="#DE5B0D", activeforeground="#000000", command=lambda: parent.corrige())
        btn_corrige.grid(row=15, column=11, padx=5)

        btn_confirma = tk.Button(action_keys, text="CONFIRMA", background="#6B8C42", font=FONT2, justify="center",
                                     activebackground="#6B8C42", activeforeground="#000000", command=lambda: parent.confirma())
        btn_confirma.grid(row=15, column=12, padx=(0, 5))
