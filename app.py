import tkinter as tk
from functools import partial


class Calculator:
    def __init__(self, root, title) -> None:
        self.root = root
        self.root.title(title)
        self.nbtns: list[tk.Button] = list()
        self.ent = tk.Entry(root)
        self.total = 0
        self.sign = str()
        self.makebtns()
        self.arrange()

    def npress(self, n):
        if n in "1234567890":
            self.ent.insert("end", n)
        elif n in "+*/":
            if len(self.ent.get()) == 0:
                return
            self.total = int(self.ent.get())           
            self.sign = n
            self.ent.delete(0, "end")
        elif n == "-":
            if len(self.ent.get()) == 0:
               self.ent.insert("end", n)
            else:
                if len(self.ent.get()) == 0:
                    return
                self.total = int(self.ent.get())           
                self.sign = n
                self.ent.delete(0, "end")
        elif n == "=":
            if n == "=":
                if self.sign == "+":
                    self.total = self.total + int(self.ent.get())
                    self.ent.delete(0, "end")
                    self.ent.insert(0, str(self.total))
                elif self.sign == "-":
                    self.total = self.total - int(self.ent.get())
                    self.ent.delete(0, "end")
                    self.ent.insert(0, str(self.total))
                elif self.sign == "*":
                    self.total = self.total * int(self.ent.get())
                    self.ent.delete(0, "end")
                    self.ent.insert(0, str(self.total))
                elif self.sign == "/":
                    self.total = self.total // int(self.ent.get())
                    self.ent.delete(0, "end")
                    self.ent.insert(0, str(self.total))
        elif n == "C":
            self.ent.delete(len(self.ent.get())-1, "end")
        else:
            pass
                

    def makebtns(self):
        for i in range(10):
            self.nbtns.append(
                tk.Button(
                    root,
                    text=str(i),
                    command=partial(self.npress, n=str(i)),
                    padx=20,
                    pady=20,
                )
            )
        for i in "+-*/=.CR":
            self.nbtns.append(
                tk.Button(
                    root,
                    text=i,
                    command=partial(self.npress, n=i),
                    padx=20,
                    pady=20,
                )
            )

    def arrange(self):
        self.ent.grid(row=0, column=0, columnspan=3, sticky="news")
        self.nbtns[0].grid(row=5, column=0, columnspan=2, sticky="news")
        self.nbtns[1].grid(row=4, column=0, sticky="news")
        self.nbtns[2].grid(row=4, column=1, sticky="news")
        self.nbtns[3].grid(row=4, column=2, sticky="news")
        self.nbtns[4].grid(row=3, column=0, sticky="news")
        self.nbtns[5].grid(row=3, column=1, sticky="news")
        self.nbtns[6].grid(row=3, column=2, sticky="news")
        self.nbtns[7].grid(row=2, column=0, sticky="news")
        self.nbtns[8].grid(row=2, column=1, sticky="news")
        self.nbtns[9].grid(row=2, column=2, sticky="news")
        self.nbtns[10].grid(row=2, column=3, rowspan=2, sticky="news")
        self.nbtns[11].grid(row=1, column=3, sticky="news")
        self.nbtns[12].grid(row=1, column=2, sticky="news")
        self.nbtns[13].grid(row=1, column=1, sticky="news")
        self.nbtns[14].grid(row=4, column=3, rowspan=2, sticky="news")
        self.nbtns[15].grid(row=5, column=2, sticky="news")
        self.nbtns[16].grid(row=0, column=3, sticky="news")
        self.nbtns[17].grid(row=1, column=0, sticky="news")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root, "Calculator")
    root.mainloop()
