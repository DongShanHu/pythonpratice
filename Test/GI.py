import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x400')

var = tk.StringVar() #顯示的字符要用變量表示
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)
#l = tk.Label(root, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit #顯示或不顯示
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)  ##command 是點擊的函數 hit me方法
b.pack()


window.mainloop()