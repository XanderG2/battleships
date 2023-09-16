import tkinter as tk, random

root = tk.Tk()
root.title("Battleships")

def sink(row, col):
    print(f"({row}, {col}) sunk.")
    print(buttons[(row*10)+col])
    current_location = buttons[row+(col*10)][0]
    if [row,col] in opponents_location:
        current_location.config(bg=sunk_color)
        sunk.append([row,col])
        for key, value in opponents_locationdic.items():
            sunks = 0
            for coord in value:
                if coord not in sunk:
                    break
                else:
                    sunks += 1
            if sunks == key:
                for coord in value:
                    currentcoord = buttons[coord[0]+(coord[1]*10)][0]
                    currentcoord.config(bg=completed_color)
    else:
        current_location.config(bg=clicked_color)

def generateRowCol():
    return [[x % 10, x // 10] for x in range(100)]

def generateOpponentLocation(): #fix later
    locations = []
    locationsdic = {}
    for shiplength in [2,3,3,4,5]:
        currentcoords = []
        rotation = random.randint(0,1)
        repeating = True
        while repeating:
            if rotation == 0:
                while True:
                    topleft = [random.randint(0,9), random.randint(0,9)]
                    bottomright = [topleft[0] + shiplength, topleft[1]]
                    if bottomright[0] < 9:
                        break
                for x in range(shiplength):
                    currentcoords.append([topleft[0]+x, topleft[1]])
            elif rotation == 1:
                while True:
                    topleft = [random.randint(0,9), random.randint(0,9)]
                    bottomright = [topleft[0], topleft[1] + shiplength]
                    if bottomright[1] < 9:
                        break
                for x in range(shiplength):
                    currentcoords.append([topleft[1]+x, topleft[0]])
            for x in currentcoords:
                if x in locations:
                    currentcoords = []
                    continue
            repeating = False
            locations += currentcoords
            if shiplength not in locationsdic.keys():
                locationsdic[shiplength] = currentcoords
            else:
                locationsdic[str(shiplength)+" "+str(2)] = currentcoords
            print("looped")
    print(locations)
    return locations, locationsdic

clicked_color = "red"
sunk_color = "green"
completed_color = "yellow"

buttons = []
sunk = []

opponents_locations = generateOpponentLocation()
opponents_location = opponents_locations[0]
opponents_locationdic = opponents_locations[1]
print(opponents_locationdic)

for row, col in generateRowCol():
    button = tk.Button(root, text="    ")
    button.grid(row=row, column=col)
    button.configure(command=lambda r=row, c=col: sink(r, c))
    buttons.append([button])

root.mainloop()
