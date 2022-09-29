import tkinter as tk


class Tk(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title = "Input Equation"
        self.geometry = ("360x150")
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = Input(container, self)
        self.frames[Input] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Input)

    def show_frame(self, cont):
        frame = self.frames[cont]
        self.active_frame = frame
        frame.tkraise()


class Input(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        equation = tk.StringVar()

        label_equation = tk.Label(self, text='Equation')
        label_equation.grid(row=0, column=0, padx=5, pady=5)
        entry_equation = tk.Entry(self, textvariable=equation, width=20)
        entry_equation.grid(column=1, row=0)

        button_submit = tk.Button(self, text='Submit', command=lambda: self.Input(
            parent, controller, equation.get()))
        button_submit.grid(column=1, row=2)
