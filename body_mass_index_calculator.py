from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')


def delete_entry():
    height_tf.delete(0, tk.END)
    weight_tf.delete(0, tk.END)


window = tk.Tk()
window.title('Калькулятор индекса массы тела (ИМТ)')
window.iconbitmap('./icon/weight_body_scales_control_fitness_diet_icon_149040.ico')
window.geometry('400x300')
window.resizable(False, False)

frame = tk.Frame(window, padx=10, pady=10)
frame.pack(expand=True)

height_lb = ttk.Label(frame, text="Введите свой рост (в см)  ", font=('Roboto', 10))
height_lb.grid(row=3, column=1, sticky='w')

weight_lb = ttk.Label(frame, text="Введите свой вес (в кг)  ", font=('Roboto', 10))
weight_lb.grid(row=4, column=1, sticky='w')

height_tf = ttk.Entry(frame)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = ttk.Entry(frame)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = ttk.Button(frame, text='Рассчитать ИМТ', command=calculate_bmi)
cal_btn.grid(row=5, column=2, sticky='we')

clear_btn = ttk.Button(frame, text='Очистить поля', command=delete_entry)
clear_btn.grid(row=6, column=2, sticky='we')

window.mainloop()
