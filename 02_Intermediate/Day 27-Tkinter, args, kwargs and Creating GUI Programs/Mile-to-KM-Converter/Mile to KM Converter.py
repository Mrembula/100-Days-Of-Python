import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)
# input value
entry = tk.Entry(width=10, font=("Arial", 12))
entry.place(x=100)

miles_label = tk.Label(text="Miles")
miles_label.place(x=200)


def miles_to_km():
    # Calculation
    miles_km = round(float(entry.get()) * 1.6)
    answer = tk.Label(text=f"{miles_km}")
    answer.config(padx=30)
    answer.place(x=100, y=30)


is_equal = tk.Label(text="is equal to ")
is_equal.place(x=30, y=30)

km = tk.Label(text="Km")
km.place(x=200, y=30)

# button
button = tk.Button(text="Calculate", command=miles_to_km)
button.place(x=100, y=55)
window.mainloop()
