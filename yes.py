import tkinter as tk
import random
import math

def sink(tile):
    print(f"{tile} sunk")

def generateRowCol():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    return [[letters[x % 10], x // 10] for x in range(100)]

root = tk.Tk()

board = []

# Create labels for row headers
for i, letter in enumerate([""] + generateRowCol()[0:10]):
    label = tk.Label(root, text=letter)
    label.grid(row=i, column=0)

# Create buttons for the board
for row, col in generateRowCol():
    button = tk.Button(root, command=lambda row=row, col=col: sink(f"{row}{col}"))
    button.grid(row=int(col) + 1, column=row)
    board.append(button)

root.mainloop()
