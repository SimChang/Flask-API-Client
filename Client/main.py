
import datetime
import requests

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


window = Tk()

window.title("Flask API Event Client")

window.geometry('600x400')

base_url = "http://127.0.0.1:5000/"

# Add tabs to the window
tab_control = ttk.Notebook(window)

add_tab = ttk.Frame(tab_control)
get_tab = ttk.Frame(tab_control)
delete_tab = ttk.Frame(tab_control)

"""Add Event"""
tab_control.add(add_tab, text='Add Event')

lbl1 = Label(add_tab, text='New event name (Required): ', padx=10, pady=10)
lbl1.grid(column=0, row=0)

txt1 = Entry(add_tab, width=30)
txt1.insert(END, 'New event name')
txt1.grid(column=1, row=0)


lbl2 = Label(add_tab, text='New event start date (format Y-m-d H:M): ', padx=10, pady=10)
lbl2.grid(column=0, row=1)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
txt2 = Entry(add_tab, width=30)
txt2.insert(END, now)
txt2.grid(column=1, row=1)

lbl3 = Label(add_tab, text='New event stop date (format Y-m-d H:M) (Optional): ', padx=10, pady=10)
lbl3.grid(column=0, row=2)

txt3 = Entry(add_tab, width=30)
txt3.grid(column=1, row=2)

lbl4 = Label(add_tab, text='Tags (separated with commas) (Optional): ', padx=10, pady=10)
lbl4.grid(column=0, row=3)

txt4 = Entry(add_tab, width=30)
txt4.insert(END, 'red,blue')
txt4.grid(column=1, row=3)


def add_btn_clicked():
    url = base_url + "event/add_event"

    body = {
        'name': txt1.get(),
        'start': txt2.get(),
        'stop': txt3.get(),
        'tags': txt4.get().split(',')
    }

    body = {k: v for k, v in body.items() if (v is not None and v != "")}

    req = requests.post(url, json=body)

    messagebox.showinfo('Validation message', str(req.status_code) + " - " + req.json()["message"])


btn1 = Button(add_tab, text="Add new event", command=add_btn_clicked, padx=10, pady=10)
btn1.grid(column=0, row=4)


"""Get Events"""
tab_control.add(get_tab, text='List Events')


"""Remove Events"""
tab_control.add(delete_tab, text='Delete Events')


tab_control.pack(expand=1, fill='both')
window.mainloop()


