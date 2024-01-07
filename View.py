import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from openpyxl import load_workbook

class ViewAntrian:
    def __init__(self, master, file_path):
        self.master = master
        self.master.title("NOMOR ANTRIAN")


        self.main_frame = ttk.Frame(self.master, padding=(10, 20))
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        

        self.file_path = file_path
        self.load_and_display_data()

    def load_excel_data(self):
        workbook = load_workbook(self.file_path)
        sheet = workbook.active
        data = []

        data.append([sheet['A1'].value])

        return data

    def display_data(self, data):
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                text_above = "Nomor Antrian  "
                label_text = f"{text_above}{value}" 

                label = ttk.Label(self.main_frame, text=label_text, padding=(5, 5), font=('Helvetica', 50))
                label.grid(row=row_idx, column=col_idx, sticky='nsew')

    def load_and_display_data(self):
        data = self.load_excel_data()
        self.display_data(data)

if __name__ == "__main__":
    file_path = 'Data_user.xlsx'
    root = tk.Tk()
    root.geometry("700x500")
    style = Style(theme='solar')
    

    
    app = ViewAntrian(root, file_path)
    root.mainloop()
