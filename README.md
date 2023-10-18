# Dremwar_HMI
Задание: Написать программу реализующую task mamager на языке python.
1. Графический интерфейс:
   - Основное окно со списком активных процессов.
   - Возможность обновления списка процессов.
   - Информационная панель, отображающая общие ресурсы системы (использование ЦП, памяти и т. д.).

2. Список процессов:
   - Отображение PID (идентификатор процесса).
   - Отображение имени процесса.
   - Отображение использования ЦП и памяти конкретным процессом.
   - Возможность завершения выбранного процесса.
   - Возможность отсортировать список процессов по различным параметрам (например, использование ЦП, памяти).

3. Информационная панель. 
Обновление в реальном времени (matplotlib. FigureCanvasTkAgg):
   - Графическое представление загрузки ЦП.
   - Графическое представление использования оперативной памяти.
   - Графическое представление использования дискового пространства.
   - Отображение загруженности сети (загрузка/выгрузка).

4.:
   - Поиск процессов по имени.
   - Возможность просмотра дополнительной информации о процессе (например, путь к исполняемому файлу, время запуска).
   - Возможность изменения приоритета процесса.

5. Настройки и предпочтения:
   - Возможность выбора интервала обновления информации (например, каждые 2 секунды, 5 секунд и т. д.).

6. Безопасность и стабильность:
   - Информирование пользователя о потенциально опасных действиях (например, предупреждение при попытке завершить какой-либо процесс (напр. важный системный процесс))

Листинг:
'''py
import tkinter as tk #Импортируем библеотеки
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

class App(tk.Tk): #Инициализируем основной Класс
    def __init__(self):
        self.n=5  #Добавляем переменные
        self.u=0
        self.a=[]
        self.a1 = []
        self.x=[]
        self.p = psutil
        super().__init__()
        self.title("TSKMNGR") #Создаём основное окно
        self.geometry("700x700")
        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)  #Добавляем вкладки в наше окно
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.fig, self.ax = plt.subplots(figsize=(4, 4)) #Добавляем фигуры для визуализации графиков
        self.fig2, self.ax1 = plt.subplots(figsize=(4, 4))
        self.fig3, self.ax2 = plt.subplots(figsize=(4, 4))

        def sort(col, reverse): #Добавляем сортировку процессов по столбцам
            l = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
            l.sort(reverse=reverse)
            for index, (_, k) in enumerate(l):
                self.tree.move(k, "", index)
            self.tree.heading(col, command=lambda: sort(col, not reverse))

        # Настройка Scrollbar
        self.scrollbar = ttk.Scrollbar(self.tab1, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        #Настройка кнопки изменения частоты обновления
        self.update_button = ttk.Button(self, text="Изменить частоту обновления", command=self.change)
        self.update_button_button.grid(row=0, column=0)
        self.txt = Entry(self, width=10)
        self.txt.grid(row=0, column=1)
        self.lable1 = Label(self, text="Введите частоту изменений(стандартная = 5с)")
        self.lable1.grid(row=0, column=3)

        #Настройка названия для вкладок
        self.tabControl.add(self.tab1, text='Процессы')
        self.tabControl.add(self.tab2, text='Процессор')
        self.tabControl.add(self.tab3, text='Память')
        self.tabControl.add(self.tab4, text='Диски')
        self.tabControl.add(self.tab5, text='Сеть')
        self.tabControl.grid(row=1, column=0, columnspan=10)

        #Настройка названия для столбцов таблицы в окне процессов
        self.tree = ttk.Treeview(self.tab1, columns=("Proccess", 'status', 'CPU', 'Memory', "Pid", 'Username'),height=30,yscrollcommand=self.scrollbar.set,show="headings")  # yscrollcommand=self.scrollbar.set
        self.tree.heading("Proccess", text="Процесс",command=lambda: sort(0, False))
        self.tree.heading('status', text="Статус процесса",command=lambda: sort(1, False))
        self.tree.heading("CPU", text="Загруженность ЦПУ",command=lambda: sort(2, False))
        self.tree.heading("Memory", text="Загруженность Памяти",command=lambda: sort(3, False))
        self.tree.heading("Pid", text="Pid",command=lambda: sort(4, False))
        self.tree.heading("Username", text="Название",command=lambda: sort(5, False))
        self.tree.column("Proccess", width=100)
        self.tree.column('status', width=120)
        self.tree.column("CPU", width=120)
        self.tree.column("Memory", width=140)
        self.tree.column("Pid", width=100)
        self.tree.column("Username", width=100)
        self.tree.grid(row=0, column=0, sticky="nsew")

        #Настройка названия для столбцов таблицы в окне Процессора
        self.tree1 = ttk.Treeview(self.tab2, columns=("process", "meaning"),show="headings")  # yscrollcommand=self.scrollbar.set
        self.tree1.heading("process", text="Процесс")
        self.tree1.heading("meaning", text="Значение")
        self.tree1.column("process", width=350)
        self.tree1.column("meaning", width=350)
        self.tree1.grid(row=0, column=0, sticky="nsew")

        #Настройка названия для столбцов таблицы в окне Памяти
        self.tree2 = ttk.Treeview(self.tab3, columns=("process", "meaning"),show="headings")  # yscrollcommand=self.scrollbar.set
        self.tree2.heading("process", text="Процесс")
        self.tree2.heading("meaning", text="Значение")
        self.tree2.column("process", width=350)
        self.tree2.column("meaning", width=350)
        self.tree2.grid(row=0, column=0, sticky="nsew")

        #Настройка названия для столбцов таблицы в окне Дисков
        self.tree3 = ttk.Treeview(self.tab4, columns=("process", "meaning"),show="headings",height=100)  # yscrollcommand=self.scrollbar.set
        self.tree3.heading("process", text="Процесс")
        self.tree3.heading("meaning", text="Значение")
        self.tree3.column("process", width=350)
        self.tree3.column("meaning", width=350)
        self.tree3.grid(row=0, column=0, sticky="nsew")

        #Настройка названия для столбцов таблицы в окне Интернета
        self.tree4 = ttk.Treeview(self.tab5, columns=("process", "meaning"),show="headings")  # yscrollcommand=self.scrollbar.set
        self.tree4.heading("process", text="Процесс")
        self.tree4.heading("meaning", text="Значение")
        self.tree4.column("process", width=350)
        self.tree4.column("meaning", width=350)
        self.tree4.grid(row=0, column=0, sticky="nsew")

        #Задаем вес столбцов и строк, чтобы Treeview мог растягиваться
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Кнопка удаления
        self.delete_button = ttk.Button(self.tab1, text="Delete Selected", command=self.delete_selected)
        self.delete_button.grid(row=1, column=0, columnspan=2, pady=20)

        #Функция обновления окон
        def update_window():
            #С помошью for я обновляю каждое из окон task manegera
            for _ in self.tree.get_children():
                self.tree.delete(_)
            for __ in self.tree1.get_children():
                self.tree1.delete(__)
            for ___ in self.tree2.get_children():
                self.tree2.delete(___)
            for ____ in self.tree3.get_children():
                self.tree3.delete(____)
            for ____ in self.tree4.get_children():
                self.tree4.delete(____)
            for process in psutil.process_iter(['name', 'status', 'cpu_percent', 'memory_percent', 'pid', 'username']):
                self.tree.insert('', 'end',values=[process.info['name'], process.info['status'], process.info['cpu_percent'],round(process.info['memory_percent'], 2), process.info['pid'],process.info['username']])

            # Настройка окна отвечающего за процессор
            q = self.p.cpu_freq()
            e=self.p.cpu_percent(interval=None)
            self.tree1.insert("", 'end', values=(f"Загруженность процессора", e))
            self.tree1.insert("", 'end', values=(f"Текущая частота", q[0]))
            self.tree1.insert("", 'end', values=(f"Минимальная частота", q[1]))
            self.tree1.insert("", 'end', values=(f"Максимальна частота", q[2]))
            self.a.append(e)
            plt.title('Загруженность процессора')
            self.u=self.u+self.n
            self.x.append(self.u)
            self.ax.plot(self.x,self.a,color='black')
            self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.tab2)
            self.dataPlot.draw()
            self.dataPlot.get_tk_widget().place(x=0, y=200)

            # Настройка окна отвечающего за Память
            mem = self.p.virtual_memory()
            self.tree2.insert("", 'end', values=(f"Общая память", str(mem[0]//1024**2)+' Mb'))
            self.tree2.insert("", 'end', values=(f"Доступная память", str(mem[1]//1024**2)+' Mb'))
            self.tree2.insert("", 'end', values=(f"Процент занятости памяти", str(mem[2])+'%'))
            self.tree2.insert("", 'end', values=(f"Использованная память", str(mem[3]//1024**2) +' Mb'))
            self.tree2.insert("", 'end', values=(f"Свободная память", str(mem[4]//1024**2)+' Mb'))
            self.a1.append(mem[2])
            plt.title('Загруженность памяти')
            self.ax1.plot(self.x, self.a1,color='black')
            self.dataPlot = FigureCanvasTkAgg(self.fig2, master=self.tab3)
            self.dataPlot.draw()
            self.dataPlot.get_tk_widget().place(x=0, y=200)

            # Настройка окна отвечающего за Диски
            disk=['C:','D:']
            for i in disk:
                disks = self.p.disk_usage(i)
                self.tree3.insert("", 'end', values=(f"Общая память диска"+' '+i, str(disks[0] // 1024 ** 2) + ' Mb'))
                self.tree3.insert("", 'end', values=(f"Использованная память диска"+' '+i, str(disks[1] // 1024 ** 2) + ' Mb'))
                self.tree3.insert("", 'end', values=(f"Свободно места на диске"+' '+i, str(disks[2] // 1024 ** 2) + ' Mb'))
                self.tree3.insert("", 'end', values=(f"Процент занятости диска"+' '+i, str(disks[3]) + '%'))
            self.D = ['Занято', 'Свободно']
            data = [disks[3], 100-disks[3]]
            color=['red','blue']
            plt.title('Диск C')
            self.ax2.pie(data, labels=self.D, autopct='%.1f%%',colors=color)
            self.dataPlot = FigureCanvasTkAgg(self.fig3, master=self.tab4)
            self.dataPlot.draw()
            self.dataPlot.get_tk_widget().place (x = 0, y = 200)

            #Настройка окна отвечающего за интернет
            intrnet = self.p.net_io_counters()
            self.tree4.insert("", 'end', values=(f"Количество отправленных мегабайтов", str(intrnet [0] // 1024 ** 2) + ' Mb'))
            self.tree4.insert("", 'end', values=(f"Количество полученных мегабайтов", str(intrnet [1] // 1024 ** 2) + ' Mb'))
            self.tree4.insert("", 'end', values=(f"количество отправленных пакетов", intrnet [2]))
            self.tree4.insert("", 'end', values=(f"количество полученных пакетов", intrnet [3] ))
            self.tree4.insert("", 'end', values=(f"Общее количество ошибок при получении", intrnet [4]))
            self.tree4.insert("", 'end', values=(f"Общее количество ошибок при отправке", intrnet [5]))
            self.tree4.insert("", 'end', values=(f"Общее количество входящих пакетов, которые были удалены",intrnet [6]))

            self.after(self.n*1000, update_window)

        update_window()

    #Функция настройки частоты обновления
    def change(self):
        self.n=int(self.txt.get())

    #Функция завершения процесса
    def delete_selected(self):
        # try:
        selfected_items = self.tree.selection()
        a = [self.tree.item(i)["values"][4] for i in selfected_items]
        pid = int(a[0])
        print(pid)
        process = psutil.Process(pid)
        process.terminate()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
'''
Скриншот1:
![image](https://github.com/Dremwar/Dremwar_HMI/assets/96596871/6478e9d6-e851-4cf0-88cc-188339905d5b)
Скриншот2:
![image](https://github.com/Dremwar/Dremwar_HMI/assets/96596871/a5b530de-17ab-4135-a443-a71d269f12d1)
Скриншот3:
![image](https://github.com/Dremwar/Dremwar_HMI/assets/96596871/71874c6b-54cb-4c33-8f25-9b2ed2a8e4ff)

