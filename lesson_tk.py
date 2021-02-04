import tkinter as tk 
x = 100
y = 200
def move_by_key(event):
    info_coords = canvas.coords(oval1)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + '   ' + str(y))
    if event.keysym == 'Up':
        canvas.move(oval1, 0 , -20)
    if event.keysym == 'Down':
        canvas.move(oval1, 0 , 20)
    if event.keysym == 'Right':
        canvas.move(oval1, 20 , 0)
    if event.keysym == 'Left':
        canvas.move(oval1, -20 , 0)
    if event.keysym == 'Escape':
        exit()
    # if info_coords[0] >= 700:
    #     canvas.move(oval1, 0 , 0)

win = tk.Tk()


label = tk.Label(text='Inginirium',
    fg='green',
    bg='yellow',
    
)
label.pack()

canvas = tk.Canvas(win, bg='#12f41f', width=700, height=700)
# canvas.create_oval((300, 300), (500, 500), fill='#0ff', outline='#fb0', width=3)
oval1 = canvas.create_oval((x, x), (y, y), fill='#1ff', outline='#fb3', width=3)
# canvas.create_line((0,0),(100,200),(300,300),(200,100),(0,0), fill='yellow', width=3)

canvas.pack()
win.bind("<KeyPress>", move_by_key)

win.mainloop()
