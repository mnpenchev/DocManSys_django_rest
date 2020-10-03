from tkinter import *
import requests

HEIGHT = 1000
WIDTH = 600


def format_response(document):
    try:
        # id = document['id']
        address = document['address']
        title = document['title']
        body = document['body']
        date = document['body']
        signed = document['signed']
        status = document['status']
        author = document['author']
        final_str = 'Address: %s, %s \nTitle: %s \nBody: %s \nDate: %s \nSigned: %s \nStatus: %s \nAuthor' % (address, title, body, date, signed, status, author)

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_document():
    # document_key = "8aa85aaa5057cb7d40c5eba10cc7daf8"
    url = 'http://localhost:8000/document/5/?format=json'
    # params = {'APPID': document_key, 'q': city, 'units': 'metric'}
    response = requests.get(url)
    document = response.json()
    label['text'] = format_response(document)
    print(response.json())


root = Tk()
root.title("Document app")
root.iconbitmap('')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bd=5, bg='#80c1ff')  # bd - border
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry = Entry(frame, bg='green', font=('Courier', 12))
# entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get document", bg='grey', fg='red', font=40, command=lambda: get_document())
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bd=10, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()

# pyinstaller.exe --onefile --icon=myicon.ico main.py
