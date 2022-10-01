import tkinter as tk
import random

ENTRY_FONT = ('Helvetica', 20)
LISTBOX_FONT = ('Arial', 15, 'bold')


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry = ('1024x1024')
        self.root.title('Maszyna Losująca')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(False, False)


        self.elements = set()

        self.build_elements()

        self.root.mainloop()

    def build_elements(self):

        self.list_box = tk.Listbox(self.root, height=20, font=LISTBOX_FONT)
        self.list_box.grid(sticky=tk.E, padx=55)

        self.entry_box = tk.Entry(self.root, font=ENTRY_FONT)
        self.entry_box.grid(sticky=tk.W, padx=10)

        self.button_los = tk.Button(self.root, text='losuj', font=ENTRY_FONT, command=self.randomize)
        self.button_los.grid(row=0, column=1, sticky=tk.W)

        self.button_add = tk.Button(self.root, text='Dodaj', font=ENTRY_FONT, command=self.add_listbox)
        self.button_add.grid(row=1, column=1, sticky=tk.W)

        self.button_del = tk.Button(self.root, text='Remove', font=ENTRY_FONT, command=self.del_listbox)
        self.button_del.grid(row=1, column=2, sticky=tk.W, padx=20)

        self.losu_label = tk.Label(self.root, text='', font=ENTRY_FONT)
        self.losu_label.grid(row=0, column=2, sticky=tk.W)

    def add_listbox(self):
        self.list_box.delete(0, tk.END)
        self.element = self.entry_box.get()
        self.elements.add(self.element)
        if self.element != '':
            for entry in self.elements:
                self.list_box.insert(tk.END, entry)

    def del_listbox(self):
        self.element = self.list_box.get(self.list_box.curselection())
        self.elements.remove(self.element)
        self.list_box.delete(tk.ANCHOR)

    def randomize(self):
        self.elements_list = list(self.elements)
        self.random_element = random.choice(self.elements_list)

        self.losu_label.configure(text=self.random_element)
Window()