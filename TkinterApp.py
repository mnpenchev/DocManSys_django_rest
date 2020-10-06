from tkinter import *
import requests
from functools import partial

HEIGHT = 900
WIDTH = 600


def validateLogin(Username, Password):
    print("username entered :", Username.get())
    print("password entered :", Password.get())
    return


def format_response(document):
    try:
        # id = document['id']
        address = document['address']
        title = document['title']
        body = document['body']
        date = document['body']
        # signed = document['signed']
        # status = document['status']
        # author = document['author']
        #final_str = 'Address: %s, %s \nTitle: %s \nBody: %s \nDate: %s \nSigned: %s \nStatus: %s \nAuthor' % (address, title, body, date, signed, status, author)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_document():
    # document_key = "8aa85aaa5057cb7d40c5eba10cc7daf8"
    url = 'http://localhost:8000/document/4/?format=json'
    # params = {'APPID': document_key, 'q': city, 'units': 'metric'}
    response = requests.get(url)
    document = response.json()
    label_body['text'] = format_response(document)
    print(response.json())


root = Tk()
root.title("Document app")
root.iconbitmap('')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# login frame
top_frame = Frame(root, bd=5, bg='#ffc1ff')  # bd - border
usernameLabel = Label(top_frame, text="User Name")
username = StringVar()
usernameEntry = Entry(top_frame, textvariable=username)
passwordLabel = Label(top_frame, text="Password")
password = StringVar()
passwordEntry = Entry(top_frame, textvariable=password, show='*')
validateLogin = partial(validateLogin, username, password)
loginButton = Button(top_frame, text="Login", command=validateLogin)

top_frame.place(relx=0.5, rely=0.01, relwidth=0.9, relheight=0.06, anchor='n')
usernameLabel.place(relx=0.05, rely=0.1)
passwordLabel.place(relx=0.05, rely=0.5)
usernameEntry.place(relx=0.3, rely=0.1, relwidth=0.4)
passwordEntry.place(relx=0.3, rely=0.5, relwidth=0.4)
loginButton.place(relx=0.8, relheight=1, relwidth=0.2)

# search for document frame
get_frame = Frame(root, bd=5, bg='#80c1ff')  # bd - border
entry = Entry(get_frame, font=('Courier', 12))
button = Button(get_frame, text="Get document", bg='grey', fg='red', font=20, command=lambda: get_document())

get_frame.place(relx=0.5, rely=0.10, relwidth=0.9, relheight=0.05, anchor='n')
entry.place(relwidth=0.65, relheight=1)
button.place(relx=0.7, relheight=1, relwidth=0.3)

#address frame
address_frame = Frame(root, bd=2, bg='#80c1ff')
label_address = Label(address_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)

address_frame.place(relx=0.75, rely=0.18, relwidth=0.40, relheight=0.15, anchor='n')
label_address.place(relwidth=1, relheight=1)

#address1 frame
address1_frame = Frame(root, bd=2, bg='#80c1ff')
# label1_address = Label(address1_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)
address1_frame.place(relx=0.25, rely=0.18, relwidth=0.40, relheight=0.15, anchor='n')
# label1_address.place(relwidth=1, relheight=1)

#title frame
body_frame = Frame(root, bd=2, bg='#80c1ff')
label_body = Label(body_frame, font=('Courier', 16), anchor='nw', justify='left', bd=4)

body_frame.place(relx=0.5, rely=0.34, relwidth=0.7, relheight=0.04, anchor='n')
label_body.place(relwidth=1, relheight=1)

# body frame
body_frame = Frame(root, bd=2, bg='#80c1ff')
label_body = Label(body_frame, font=('Courier', 12), anchor='nw', justify='left', bd=4)

body_frame.place(relx=0.5, rely=0.40, relwidth=0.9, relheight=0.4, anchor='n')
label_body.place(relwidth=1, relheight=1)

#date frame
date_frame = Frame(root, bd=2, bg='#80c1ff')
label_date = Label(date_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)

date_frame.place(relx=0.20, rely=0.90, relwidth=0.30, relheight=0.05, anchor='n')
label_date.place(relwidth=1, relheight=1)

# signature frame
signature_frame = Frame(root, bd=2, bg='#80c1ff')
label_signature = Label(signature_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)

signature_frame.place(relx=0.75, rely=0.85, relwidth=0.40, relheight=0.10, anchor='n')
label_signature.place(relwidth=1, relheight=1)

root.mainloop()

# pyinstaller.exe --onefile --icon=myicon.ico main.py
