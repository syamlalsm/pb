from tkinter import*

window=Tk()
window.title("my window")
window.geometry("250x150")

def save_value():
    print("**********************")

b=Label(window,text="PLEASE ENTER ANYTHING  ",background="black",foreground="yellow",font=("helvetica",12,"bold"),padx=5,pady=5)
b.pack()
btn=Button(window,text="CLICK ME",bg="grey",fg="white",command=save_value,font=("helvetica",7,"bold"))
btn.pack()
window.config(bg="green")
window.mainloop()