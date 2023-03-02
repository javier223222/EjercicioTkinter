import tkinter
from tkinter import ttk
window=tkinter.Tk()
window.columnconfigure(0,weight=1)
window.columnconfigure(0,weight=3)
selecciont=tkinter.StringVar()
selecciont1=tkinter.StringVar()
selecciont2=tkinter.StringVar()
cuadro=0
def reiniciar():
     cuadro=ttk.Label(text="                                         ")
     cuadro.grid(column=4,row=1 )


calcular=ttk.Button(window,text="reiniciar",command=reiniciar)
calcular.grid(column=4,row=1 )
calcular.place(x=230,y=150)
def x():
     a=selecciont.get()
     cuadro=ttk.Label(text="la opcion es linux Linux")
     cuadro.grid(column=4,row=1 )
def y():
     a=selecciont1.get()
     cuadro=ttk.Label(text="la opcion es macos")
     cuadro.grid(column=4,row=1 )
def z():
      a=selecciont2.get()
      cuadro=ttk.Label(text="la opcion es macos")
      cuadro.grid(column=4,row=1 )

r1=ttk.Radiobutton(window,text="Linux",value="1",variable=selecciont, command=x)
r2=ttk.Radiobutton(window,text="macos",value="2",variable=selecciont1,command=y)
r3=ttk.Radiobutton(window,text="windows",value="3",variable=selecciont2,command=z)
r1.grid(column=0,row=1,padx=5,pady=5)
r2.grid(column=0,row=2,padx=5,pady=5)
r3.grid(column=0,row=3,padx=5,pady=5)
print(selecciont)
window.mainloop()