import tkinter


def button_click():
    print('I got clicked')
    my_label['text'] = 'Button clicked'
    my_label.config(text=entry.get())


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

# label
my_label['text'] = 'New Text'
my_label.config(text='New Text')
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=0)

# Entry
entry = tkinter.Entry(width=10)
print(entry.get())
# entry.pack()
entry.grid(column=2, row=0)

window.mainloop()
