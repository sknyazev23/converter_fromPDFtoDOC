from pypdf import PdfReader
from tkinter import *
from tkinter import filedialog, messagebox


class Window:
    def __init__(self, width, height, title='PDF Converter', resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+300')
        self.root.resizable(resizable[0], resizable[1])

        self.entry = Entry(self.root, width=50, fg='blue', font=('Veranda', 9), bg='yellow', justify=LEFT)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):

        self.entry.pack(anchor=NW, padx=10, pady=10, fill=X)
        Button(self.root, width=20, height=3, text='Выбрать файл', bd=4, activebackground='orange', command=self.file_open).pack(padx=10, pady=10, anchor=W)
        Button(self.root, width=20, height=3, text='Конвертировать', bd=4, activebackground='orange', command=self.convert).pack(padx=10, pady=10, anchor=W)
        Button(self.root, width=20, height=3, text='Сброс', bd=4, activebackground='orange', command=self.clear).pack(padx=10, pady=10, anchor=W)
        Button(self.root, width=20, height=3, text='Выход', bd=4, activebackground='red', command=self.root.destroy).pack(padx=10, pady=10, side=RIGHT)

    def clear(self):
        self.entry.delete(0, END)

    def convert(self):
        text = self.entry.get()
        print(text)
        reader = PdfReader(text)
        page = reader.pages[0]

        choice = messagebox.askyesno('Файл отформатирован', f'Хотите его сохранить: {len(reader.pages)} страниц')
        print(choice)
        if choice:
            result = open(r'C:\Users\USER\Desktop\result.doc', 'a+', encoding='utf-8')

            # Extracts all text from PDF page by page
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                res = page.extract_text()
                print(res)
                result.write(res)

            result.close()
            print(result.name)
        
            # Extracts images from PDF file
            if len(page.images) != 0:
                for i in page.images:
                    with open(i.name, 'wb') as f:
                        f.write(i.data)
            else:
                print('NO IMAGES IN THE FILE')

    def file_open(self):
        wanted_files = ("PDF", "*.pdf"),('ALL', '*.*')
        file_name = filedialog.askopenfilename(title='Выбрать файл', filetypes=wanted_files)
        self.entry.insert(0, file_name)


if __name__ == '__main__':
    window = Window(400, 500)
    window.run()
