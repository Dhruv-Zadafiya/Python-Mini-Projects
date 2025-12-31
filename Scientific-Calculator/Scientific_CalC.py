from tkinter import *
import math as m

root = Tk()
root.title("Modern Scientific Calculator")
root.geometry("480x560")
root.config(bg="#0b0d1a")
root.resizable(True, True)

e = Entry(
    root, font=("Segoe UI", 22), bd=0, fg="#00ffd5",
    bg="#15172b", justify=RIGHT, insertbackground="white"
)
e.grid(row=0, column=0, columnspan=5, ipadx=10, ipady=15, padx=15, pady=20)


def click(val):
    e.insert(END, val)


def clear():
    e.delete(0, END)


def backspace():
    e.delete(len(e.get()) - 1, END)


def evaluate():
    try:
        e.insert(END, "")
        res = eval(e.get())
        e.delete(0, END)
        e.insert(0, res)
    except:
        e.delete(0, END)
        e.insert(0, "Error")


def sci(event):
    key = event.widget["text"]
    try:
        n = float(e.get()) if e.get() else 0
        ops = {
            "sin": m.sin(n), "cos": m.cos(n), "tan": m.tan(n),
            "lg": m.log10(n), "ln": m.log(n), "√": m.sqrt(n),
            "x!": m.factorial(int(n)), "1/x": 1/n,
            "π": m.pi, "e": m.e, "deg": m.degrees(n)
        }
        e.delete(0, END)
        e.insert(0, ops[key])
    except:
        e.delete(0, END)
        e.insert(0, "Error")


def key_event(event):
    if event.char in "0123456789+-*/().":
        click(event.char)
    elif event.char == "^":
        click("**")
    elif event.keysym == "Return":
        evaluate()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()
    elif event.char.lower() == "p":
        click(str(m.pi))
    elif event.char.lower() == "e":
        click(str(m.e))


root.bind("<Key>", key_event)

def modern_btn(txt, r, c, cmd=None, sci_btn=False, color="#1f233d"):
    b = Button(
        root, text=txt, font=("Segoe UI", 12, "bold"),
        fg="white", bg=color, activebackground="#00ffd5",
        activeforeground="black", bd=0, width=6, height=2,
        command=cmd
    )
    b.grid(row=r, column=c, padx=6, pady=6)

    b.bind("<Enter>", lambda e: b.config(bg="#00ffd5", fg="black"))
    b.bind("<Leave>", lambda e: b.config(bg=color, fg="white"))

    if sci_btn:
        b.bind("<Button-1>", sci)

    return b


modern_btn("lg", 1, 0, sci_btn=True)
modern_btn("ln", 1, 1, sci_btn=True)
modern_btn("(", 1, 2, lambda: click("("))
modern_btn(")", 1, 3, lambda: click(")"))
modern_btn(".", 1, 4, lambda: click("."))

modern_btn("^", 2, 0, lambda: click("**"))
modern_btn("deg", 2, 1, sci_btn=True)
modern_btn("sin", 2, 2, sci_btn=True)
modern_btn("cos", 2, 3, sci_btn=True)
modern_btn("tan", 2, 4, sci_btn=True)

modern_btn("√", 3, 0, sci_btn=True)
modern_btn("C", 3, 1, clear, "#e76f51")
modern_btn("⌫", 3, 2, backspace, "#e76f51")
modern_btn("%", 3, 3, lambda: click("%"))
modern_btn("/", 3, 4, lambda: click("/"))

modern_btn("x!", 4, 0, sci_btn=True)
modern_btn("7", 4, 1, lambda: click("7"), color="#3a3f7a")
modern_btn("8", 4, 2, lambda: click("8"), color="#3a3f7a")
modern_btn("9", 4, 3, lambda: click("9"), color="#3a3f7a")
modern_btn("*", 4, 4, lambda: click("*"))

modern_btn("1/x", 5, 0, sci_btn=True)
modern_btn("4", 5, 1, lambda: click("4"), color="#3a3f7a")
modern_btn("5", 5, 2, lambda: click("5"), color="#3a3f7a")
modern_btn("6", 5, 3, lambda: click("6"), color="#3a3f7a")
modern_btn("-", 5, 4, lambda: click("-"))

modern_btn("π", 6, 0, sci_btn=True)
modern_btn("1", 6, 1, lambda: click("1"), color="#3a3f7a")
modern_btn("2", 6, 2, lambda: click("2"), color="#3a3f7a")
modern_btn("3", 6, 3, lambda: click("3"), color="#3a3f7a")
modern_btn("+", 6, 4, lambda: click("+"))

modern_btn("e", 7, 1, sci_btn=True)
modern_btn("0", 7, 2, lambda: click("0"), color="#3a3f7a")
modern_btn("=", 7, 3, evaluate, "#f4a261")

root.mainloop()
