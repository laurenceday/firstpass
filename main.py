from tkinter import *
from tkinter import ttk
import hashlib

def derive_passwords(*args):
    try:
        base_phrase = str(hashphrase.get())
        youtube_hash.set(hashlib.sha3_512((base_phrase + " YOUTUBE").encode('utf-8')).hexdigest())
        discord_hash.set(hashlib.sha3_512((base_phrase + " DISCORD").encode('utf-8')).hexdigest())
        twitter_hash.set(hashlib.sha3_512((base_phrase + " TWITTER").encode('utf-8')).hexdigest())
    except ValueError:
        pass

root = Tk()
root.title("FirstPass")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

hashphrase = StringVar()
hashphrase_entry = ttk.Entry(mainframe, width=25, textvariable=hashphrase)
hashphrase_entry.grid(column=2, row=1)

youtube_hash = StringVar()
discord_hash = StringVar()
twitter_hash = StringVar()
ttk.Entry(mainframe, width=25, textvariable=youtube_hash).grid(column=2, row=2)
ttk.Entry(mainframe, width=25, textvariable=discord_hash).grid(column=2, row=3)
ttk.Entry(mainframe, width=25, textvariable=twitter_hash).grid(column=2, row=4)

ttk.Label(mainframe, text="Secret phrase").grid(column=1, row=1)
ttk.Label(mainframe, text="YOUTUBE").grid(column=1, row=2)
ttk.Label(mainframe, text="DISCORD").grid(column=1, row=3)
ttk.Label(mainframe, text="TWITTER").grid(column=1, row=4)

ttk.Button(mainframe, text="Derive", command=derive_passwords).grid(column=1, row=5)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

hashphrase_entry.focus()
root.bind("<Return>", derive_passwords)

root.mainloop()