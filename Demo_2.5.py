from tkinter import *

####################################
#----------| класс Стек |----------#
####################################

class steck:
    def __init__(self):             #конструктор
        print("контруктор_steck")
        self.arr = []
        self.inc = 0
        self.collor = ['#f5fc3e', '#ebd019', '#ebb219', '#eb7719', '#eb3219', '#eb195e',
                       '#eb1990', '#eb19e4', '#bc19eb', '#ba85f7', '#8a85f7', '#85c3f7',
                       '#85f6f7', '#85f7d0', '#85f7a2', '#a8f785', '#c8f785', '#ebf785']
    
    def pop(self, button, edit):
        string = edit.get()                         #get() - возвращает введеный в поле текст
        if self.arr:
            edit.configure(state = 'normal')        #configure() - изменение пар-ов
            edit.delete(0, END)
            edit.insert(0, self.arr.pop(0))
            edit.configure(state = 'disabled')
            canvas.delete("rec" + str(self.inc))
            canvas.delete("txt" + str(self.inc))
            self.inc -= 1
            self.y += 23
            text(len(self.arr))
        else:
            button.configure(state = 'disabled')
 
    def push(self, button, edit):
        string = edit.get()
        if (len(self.arr) == 0):
            self.y = 442
            self.x = 30
        if (string) and (len(self.arr) <= 17):
            if(len(string) > 29):
                string = string[0:29]               #обрезает после 29 символа
            self.inc += 1
            self.y -= 23
            self.arr.insert(0, string)
            canvas.create_rectangle(self.x, self.y, self.x + 260, self.y - 20,
                                    fill=self.collor[self.inc - 1], tag = "rec" + str(self.inc))
            canvas.create_text(self.x, self.y - 10, anchor = W, text = string,
                               tag = "txt" + str(self.inc))
            edit.delete(0, END)
            text(len(self.arr))
        if (len(self.arr) > 17):
            button.configure(state = 'disabled')

    def delete_all(self):
        self.arr.clear()                            #clear() - очистка списка
        canvas.delete("all")                        #удаление с холста всего
        self.inc = 0
        text(len(self.arr))
        
    def arr_empty(self, button):
        if (len(self.arr) > 0):
            button.configure(state = 'normal')
        else:
            button.configure(state = 'disabled')
        
    def __del__(self):              #деструктор
        print("деструктор_steck")


#####################################################
#----------| класс всплывающих подсказок |----------#
#####################################################

class toolTips:
    def __init__(self, widget, text):
        print("контруктор_toolTips")
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter_cursor)
        self.widget.bind("<Leave>", self.exit_cursor)
        self.id = None
        self.top_lvl = None

    def enter_cursor(self, event = None):
        self.id = self.widget.after(500, self.show_tooltip)     #после 500 милисек - вызов метода

    def exit_cursor(self, event = None):
        id = self.id                            #id - показ. какая команда должна быть отменена
        self.id = None
        if id:
            self.widget.after_cancel(id)        #after_cancel() - отменяет ранее выполненую команду
        top_lvl = self.top_lvl
        self.top_lvl = None
        if top_lvl:
            top_lvl.destroy()                   #destroy() - уничтожение окна

    def show_tooltip(self, event = None):
        x = y = 0
        x += self.widget.winfo_rootx() + 25         #winfo_rootx() - воз-ет x левого угла виджета
        y += self.widget.winfo_rooty() + 20
        self.top_lvl = Toplevel(self.widget)        #Toplevel - окно верхнего уровня
        self.top_lvl.wm_overrideredirect(True)
                     #wm_overrideredirect - окно показывается без обрамления(без загловка и прочего)
        self.top_lvl.wm_geometry("+%d+%d" % (x, y))     #%d - дес-е число
        label = Label(self.top_lvl, text = self.text, borderwidth = 1, wraplength = 180,
                      background="#ffffff")
                    #wraplength - если стр не входит - перенесется
        label.pack(ipadx = 2)

################################################
#----------| класс панели элементов |----------#
################################################
        
class imgbutton:
    def __init__(self, parent):
        print("контруктор_imgbutton")
        self.parent = parent
        self.btnMenu()

    def btnMenu(self):
        imgAdd = PhotoImage(file = '1.png')
        frame = Frame(self.parent, bd = 5, bg = '#122c81')          #bd = padding
        frame.pack(fill = X)                                    #fill - растягивается по x

        self.imgAdd = PhotoImage(file = 'add.png')
        self.btnAdd = Button(frame, image = self.imgAdd, compound='top', command = btnMenu_add,
                             bg = 'BLACK')
        self.btnAdd.pack(side = LEFT)
        btnAdd_ttp = toolTips(self.btnAdd, "Добавление элементов")

        self.imgDel = PhotoImage(file = 'del.png')
        self.btnDel = Button(frame, image = self.imgDel, compound='top', command = btnMenu_delete,
                             bg = 'black')
        self.btnDel.pack(side = LEFT)
        btnDel_ttp = toolTips(self.btnDel, "Удаление элементов")

        self.imgQue = PhotoImage(file = 'que.png')
        self.btnQue = Button(frame, image = self.imgQue, compound='top', command = btnMenu_about,
                             bg = 'black')
        self.btnQue.pack(side = LEFT)
        btnQue_ttp = toolTips(self.btnQue, "О программе")

        self.imgAll = PhotoImage(file = 'all.png')
        self.btnAll = Button(frame, image = self.imgAll, compound='top', bg = 'black',
                             command = getClass.delete_all)
        self.btnAll.pack(side = LEFT)
        btnAll_ttp = toolTips(self.btnAll, "Очистить стек")

        self.imgExit = PhotoImage(file = 'exit.png')
        self.btnExit = Button(frame, image = self.imgExit, compound='top', bg = 'black',
                              command = root.destroy)
        self.btnExit.pack(side = RIGHT)
        btnExit_ttp = toolTips(self.btnExit, "Выход")
   
    def __del__(self):
        print("деструктор_imgbutton")
        
#####################################################################################
        
def text(value):
    edit.configure(state = 'normal')
    edit.delete(0, END)
    edit.insert(0, "{0} / {1}".format(value, 18))
    edit.configure(state = 'disabled')

def btn_block(event, value, btn):       #value + event.char
    if value:
        btn.configure(state = 'normal')
    else:
        btn.configure(state = 'disabled')
    
def btnMenu_add():
    add_window = Toplevel(root)
    add_window.geometry("450x200+658+54")           
    add_window.resizable(False, False)
    add_window.title("Добавление в стек")
    bg_image = PhotoImage(file = 'add_win.png')
    bg_label = Label(add_window, image = bg_image)
    bg_label.place( x = -2, y = -2)
   
    label= Label(add_window, text = "Добавить элемент в стек:", font = "Arial 12 bold",
                 bg = '#455ead', fg = 'gray99', padx = 2)
    label.place(x = 10, y = 40)
    btn_push = Button(add_window, text = "Внести элемент", font = "Arial 10 bold",
                     bg = '#748bed', fg = 'gray99', padx = 5, state = DISABLED)        
    btn_push.place(x = 180, y = 80)
    edit1 = Entry(add_window, width = 35, bd = 3, bg = 'ghostwhite')
    edit1.bind('<Key>', lambda event: btn_block(event, edit1.get(), btn_push))
    edit1.place(x = 230, y = 40)
    btn_push['command'] = lambda: getClass.push(btn_push, edit1)
    btn_close = Button(add_window, text = "Закрыть окно", command = add_window.destroy,
                       font = "Arial 10 bold", bg = '#122c81', fg = 'gray99', width = 13)
    btn_close.place(x = 320, y = 150)
    add_window.grab_set()           #grab_set()- делаем окно модальным
    add_window.focus_set()          #focus_set()- фокусируемся на окне
    add_window.wait_window()        #wait_window()- пока не закрыть др. окно не открыть
    add_window.mainloop()
        
def btnMenu_delete():
    delete_window = Toplevel(root)
    delete_window.geometry("510x200+658+54")
    delete_window.resizable(False, False)
    delete_window.title("Извлечение из стека")
    bg_image = PhotoImage(file = 'del_win.png')
    bg_label = Label(delete_window, image = bg_image)
    bg_label.place( x = -2, y = -2)

    label= Label(delete_window, text = "Последний извлеченный элемент:", font = "Arial 12 bold",
                 bg = '#455ead', fg = 'gray99')
    label.place(x = 2, y = 40)
    edit1 = Entry(delete_window, width = 35, bd = 3, bg = 'ghostwhite')
    edit1.place(x = 290, y = 40)
    edit1['state'] = DISABLED
    btn_pop = Button(delete_window, text = "Извлечь элемент", font = "Arial 10 bold",
                     bg = '#748bed', fg = 'gray99')
    btn_pop.place(x = 220, y = 80)
    btn_pop['command'] = getClass.arr_empty(btn_pop)
    btn_pop['command'] = lambda: getClass.pop(btn_pop, edit1) 
    btn_close = Button(delete_window, text = "Закрыть окно", command = delete_window.destroy,
                       font = "Arial 10 bold", bg = '#122c81', fg = 'gray99', width = 15)
    btn_close.place(x = 360, y = 150)
    delete_window.grab_set()        #grab_set()- делаем окно модальным
    delete_window.focus_set()       #focus_set()- фокусируемся на окне
    delete_window.wait_window()     #wait_window()- пока не закрыть др. окно не открыть
    delete_window.mainloop()

def btnMenu_about():
    window = Toplevel(root)
    window.geometry("300x250+658+54")
    window.resizable(False, False)
    window.title("О программе")
    bg_image = PhotoImage(file = 'about_win.png')
    bg_label = Label(window, image = bg_image)
    bg_label.place(x = -2, y = -2)
    
    lab = Label(window, text = """Программа моделирует стек \nсредствами языка Python
          \nВерсия программы: 2.5
          \nАвтор: Шульгина Мария
          \nКурган, 2018""", font = "Arial 12 bold", bg = '#455ead', fg = 'gray99')
    lab.place(x = 30, y = 30)
    btn_exit = Button(window, text = "Закрыть окно", command = window.destroy,
                      font = "Arial 10 bold", bg = '#122c81', fg = 'gray99')
    btn_exit.place(x = 95, y = 200)
    window.grab_set()           #grab_set()- делаем окно модальным
    window.focus_set()          #focus_set()- фокусируемся на окне
    window.wait_window()        #wait_window()- пока не закрыть др. окно не открыть
    window.mainloop()

####################################################################################
  
root = Tk()

getClass = steck() #создание экземпляра класса
ImageButton = imgbutton(root)

root.overrideredirect(True)                        #убираем кнопки свернуть, закр, на весь экр.
root.geometry("500x500+150+50")
root.resizable(False, False)
root.title("PYTHON STACK VER 2.0")
bg_image = PhotoImage(file = '1.png')
bg_label = Label(root, image = bg_image)
bg_label.place( x = -2, y = 45)

##############################
#----------| меню |----------#
##############################

main_menu = Menu(root)
root.config(menu = main_menu)
#1-й пункт меню
ps = Menu(main_menu, tearoff = 0)               #tearoff - закрепляем подпункты
main_menu.add_cascade(label = "Перечень операций", menu = ps)
ps.add_command(label = "Помещение в стек", command = btnMenu_add)
ps.add_command(label = "Извлечение из стека", command = btnMenu_delete)
ps.add_command(label = "Очистить стек", command = getClass.delete_all)
#2-й пункт меню
main_menu.add_cascade(label = "О программе", command = btnMenu_about)
#3-й пункт меню
main_menu.add_cascade(label = "Выход", command = root.destroy)

##############################
#----------| ввод |----------#
##############################

lab_1 = Label(root, text = "Содержимое стека:", font = "Arial 12 bold", bg = '#122c81',
              fg = 'gray99', padx = 10)
lab_1.place(x = 70, y = 47)

canvas = Canvas(root, width = 320, height = 420, bg='grey95')
canvas.place(x = 5, y = 70)

lab_2 = Label(root, text = "Элементов:", font = "Arial 14", bg = '#9abce0')
lab_2.place(x = 370, y = 220)
edit = Entry(root,width = 6, bd = 3, bg = 'ghostwhite')
edit.insert(0, "{0} / {1}".format(0, 18))
edit['state'] = DISABLED
edit.place(x = 400, y = 250)

btn_exit = Button(root, text = "Выход из приложения", font = "Arial 10 bold", bg = '#122c81',
              fg = 'gray99', command = root.destroy)
btn_exit.place(x = 335, y = 465)  #x = 340, y = 457 для картинки

root.mainloop()

del getClass
del ImageButton
