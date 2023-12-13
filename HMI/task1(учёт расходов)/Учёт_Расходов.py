import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Учёт расходов")
        self.geometry("1920x1080")
        self.fig, self.ax = plt.subplots(figsize=(4, 4))

        #Создание переменных
        self.x = []
        self.y = []
        self.z = []
        self.dict_prise={}
        self.dict_time={}
        self.dict = {}

        self.notebook = ttk.Notebook()
        self.notebook.pack(expand=True, fill="both")
        self.notebook.pack(fill="both", expand=True)

        # Надписи для обозначения полей ввода
        self.label = ttk.Label(self.notebook, text="Введите Значения")
        self.label.grid(row=1, column=0)
        self.label1 = ttk.Label(self.notebook, text="Дата:")
        self.label1.grid(row=2, column=0)
        self.label2 = ttk.Label(self.notebook, text="Категория:")
        self.label2.grid(row=3, column=0)
        self.label3 = ttk.Label(self.notebook, text="Цена")
        self.label3.grid(row=4, column=0)

        # Поля ввода данных
        self.enter1 = ttk.Entry(self.notebook)
        self.enter1.grid(row=2, column=1)
        self.enter2 = ttk.Entry(self.notebook)
        self.enter2.grid(row=3, column=1)
        self.enter3 = ttk.Entry(self.notebook)
        self.enter3.grid(row=4, column=1)

        # Кнопка ввода
        self.select_button = ttk.Button(self.notebook, text="Ввод данных", command=self.check_enter)
        self.select_button.grid(row=2, column=2,columnspan=10)

        # Настройка Scrollbar
        self.scrollbar = ttk.Scrollbar(self.notebook, orient="vertical")
        self.scrollbar.grid(row=0, column=2, sticky="ns")

        self.tree = ttk.Treeview(self.notebook, columns=("Data", "Type", "Summ"), yscrollcommand=self.scrollbar.set, show="headings")  # yscrollcommand = self.scrollbar.set
        self.tree.heading("Data", text="Дата", command=lambda: self.sort(0, False))
        self.tree.heading("Type", text="Тип", command=lambda: self.sort(1, False))
        self.tree.heading("Summ", text="Цена расходов", command=lambda: self.sort(2, False))

        # Настройка таблицы
        self.tree.column("Data", width=300)
        self.tree.column("Type", width=300)
        self.tree.column("Summ", width=300)
        self.tree.grid(row=0, column=0,columnspan=50, sticky="s")

        # Связываем полосу прокрутки с Treeview
        self.scrollbar.config(command=self.tree.yview)  # Метод yview управляет вертикальной прокруткой в Treeview.

        # Кнопка удаления
        self.delete_button = ttk.Button(self.notebook, text="Удалить значение", command=self.delete_selected)
        self.delete_button.grid(row=3, column=2, columnspan=10)

    # Проверка ввода
    def check_enter(self):
        format = "%m.%d.%Y"
        mem = True

        # Настройка полей ввода и исключение ввода неправильных данных
        try:
            mem = bool(datetime.strptime(self.enter1.get(), format))
        except ValueError:
            mem = False
        if not self.enter3.get().isdigit():
            mem = False
        if not mem:
            showwarning(title="Ошибка ввода Данных", message="Введите или исправьте данные")
            return True
        else:
            self.add_data()

    # Функция занесения данных в таблицу
    def add_data(self):
        self.ax.clear()
        data = [self.enter1.get(), self.enter2.get(), self.enter3.get()]
        self.tree.insert("", "end", values=data)
        self.x.append(self.enter1.get())

        # Создание словарей для начертания графика
        self.dict_prise[self.enter2.get()] = self.y
        self.dict_time[self.enter2.get()] = self.x
        self.dict[self.enter1.get()] = int(self.enter3.get())
        self.d=dict(sorted(self.dict.items()))

        #Создание графика отслеживания
        self.ax.plot(self.d.keys(), self.d.values())
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.notebook)
        self.dataPlot.draw()
        self.dataPlot.get_tk_widget().grid(row=3, column=20,rowspan=20)

    # Кнопка удаление из таблицы данных
    def delete_selected(self):
        selected_items = self.tree.selection()
        for item in selected_items:
            self.tree.delete(item)

    # Сортировка
    def sort(self, col, reverse):
        # получаем все значения столбцов в виде отдельного списка
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        # сортируем список
        l.sort(reverse=reverse)
        # переупорядочиваем значения в отсортированном порядке
        for index, (_, k) in enumerate(l):
            self.tree.move(k, "", index)
        # в следующий раз выполняем сортировку в обратном порядке
        self.tree.heading(col, command=lambda: self.sort(col, not reverse))

#Запуск программы
if __name__ == "__main__":
    app = App()
    app.mainloop()