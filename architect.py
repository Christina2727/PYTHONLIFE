#Christina Roberts
#How to Code 2.0

from tkinter import*

print("Please click the 'Draw Skyscraper' button at bottom of canvas")

def new_skyscraper():
    win_w = 10
    win_h = 15
    w = 15
    h = 20
    gap = 4

    my_building.create_rectangle(gap, gap, (win_w +2)*gap + win_w * w,
                             (win_h + 2)* gap + win_h * h, outline = "purple",
                             fill = "purple")

    for i in range (win_w):
        for j in range (win_h):
            my_building.create_rectangle(((w + gap) * i + 2 * gap),
                                         ((h + gap) * j + 2 * gap),
                                         ((w + gap) * i + (2* gap + w)),
                                         ((h + gap) * j + (2 * gap + h)),
                                         outline = "black", fill = "pink")

    my_building.pack(fill = BOTH, expand = 1)

root = Tk()
my_building = Canvas(root, width = 500, height = 500)
root.title("Skyscraper")
my_building.pack()

button = Button(root, text = "Draw Skyscraper At Sunset", command = new_skyscraper)
button.pack()

root.mainloop()



                             
