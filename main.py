import tkinter as tk

def sink(tile):
    print(f"{tile} sunk")

def generateRowCol():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    return [[letters[x%10], x//10] for x in range(100)]

root = tk.Tk()

print(generateRowCol())

lettertonumber = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9
}

for row,col in generateRowCol():
    button = tk.Button(root, command=lambda: sink(f"{row};{col}"))
    button.grid(row=lettertonumber[row], column=col)

root.mainloop()