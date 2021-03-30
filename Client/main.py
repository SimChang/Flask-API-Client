
import datetime
import json
import requests

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext


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

add_lbl1 = Label(add_tab, text='New event name (Required): ', padx=10, pady=10)
add_lbl1.grid(column=0, row=0)

add_txt1 = Entry(add_tab, width=30)
add_txt1.insert(END, 'New event name')
add_txt1.grid(column=1, row=0)


add_lbl2 = Label(add_tab, text='New event start date (format Y-m-d H:M): ', padx=10, pady=10)
add_lbl2.grid(column=0, row=1)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
add_txt2 = Entry(add_tab, width=30)
add_txt2.insert(END, now)
add_txt2.grid(column=1, row=1)

add_lbl3 = Label(add_tab, text='New event stop date (format Y-m-d H:M) (Optional): ', padx=10, pady=10)
add_lbl3.grid(column=0, row=2)

add_txt3 = Entry(add_tab, width=30)
add_txt3.grid(column=1, row=2)

add_lbl4 = Label(add_tab, text='Tags (separated with commas) (Optional): ', padx=10, pady=10)
add_lbl4.grid(column=0, row=3)

add_txt4 = Entry(add_tab, width=30)
add_txt4.insert(END, 'red,blue')
add_txt4.grid(column=1, row=3)


def add_btn_clicked():
    url = base_url + "event/add_event"

    body = {
        'name': add_txt1.get(),
        'start': add_txt2.get(),
        'stop': add_txt3.get(),
        'tags': add_txt4.get().split(',')
    }

    body = {k: v for k, v in body.items() if (v is not None and v != "")}

    req = requests.post(url, json=body)

    messagebox.showinfo('Validation message', str(req.status_code) + " - " + req.json()["message"])


add_btn1 = Button(add_tab, text="Add new event", command=add_btn_clicked, padx=10, pady=10)
add_btn1.grid(column=0, row=4)


"""Get Events"""
tab_control.add(get_tab, text='List Events')

get_lbl1 = Label(get_tab, text='Event name (or part of name): ', padx=10, pady=10)
get_lbl1.grid(column=0, row=0)

get_txt1 = Entry(get_tab, width=30)
get_txt1.grid(column=1, row=0)

get_lbl2 = Label(get_tab, text='Full name: ', padx=10, pady=10)
get_lbl2.grid(column=0, row=1)

selected = StringVar()

get_rad1 = Radiobutton(get_tab, text='True', value="True", variable=selected)
get_rad1.grid(column=1, row=1)

get_rad2 = Radiobutton(get_tab, text='False', value="False", variable=selected)
get_rad2.grid(column=2, row=1)

selected.set("True")

get_lbl3 = Label(get_tab, text='Minimum start date (format Y-m-d H:M): ', padx=10, pady=10)
get_lbl3.grid(column=0, row=2)

get_txt3 = Entry(get_tab, width=30)
get_txt3.grid(column=1, row=2)

get_lbl4 = Label(get_tab, text='Maximum start date (format Y-m-d H:M): ', padx=10, pady=10)
get_lbl4.grid(column=0, row=3)

get_txt4 = Entry(get_tab, width=30)
get_txt4.grid(column=1, row=3)

get_lbl5 = Label(get_tab, text='Minimum stop date (format Y-m-d H:M): ', padx=10, pady=10)
get_lbl5.grid(column=0, row=4)

get_txt5 = Entry(get_tab, width=30)
get_txt5.grid(column=1, row=4)

get_lbl6 = Label(get_tab, text='Maximum stop date (format Y-m-d H:M): ', padx=10, pady=10)
get_lbl6.grid(column=0, row=5)

get_txt6 = Entry(get_tab, width=30)
get_txt6.grid(column=1, row=5)

get_lbl7 = Label(get_tab, text='Tags (separated with commas): ', padx=10, pady=10)
get_lbl7.grid(column=0, row=6)

get_txt7 = Entry(get_tab, width=30)
get_txt7.grid(column=1, row=6)


def show_events(events):

    new_window = Toplevel(window)

    new_window.title("Events list")

    txt = scrolledtext.ScrolledText(new_window)
    txt.insert(INSERT, json.dumps(events, indent=4))

    txt.grid(column=0, row=0)


def get_btn_clicked():
    url = base_url + "event/list_events"

    param = {
        'name': get_txt1.get(),
        'name_exact': selected.get(),
        'start_min': get_txt3.get(),
        'start_max': get_txt4.get(),
        'stop_min': get_txt5.get(),
        'stop_max': get_txt6.get(),
        'tags': get_txt7.get()
    }

    param = {k: v for k, v in param.items() if (v is not None and v != "")}

    req = requests.get(url, params=param)

    show_events(req.json())


get_btn1 = Button(get_tab, text="Get events list", command=get_btn_clicked, padx=10, pady=10)
get_btn1.grid(column=0, row=7)

"""Remove Events"""
tab_control.add(delete_tab, text='Delete Events')


tab_control.pack(expand=1, fill='both')
window.mainloop()


