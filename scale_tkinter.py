import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)
#scale物件 建立 showvalue 0代表不顯示 1代表顯示 在label 上
#resolutuin 0.01取決到小數第二位
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=2, resolution=0.1, command=print_selection)
s.pack()

window.mainloop()
