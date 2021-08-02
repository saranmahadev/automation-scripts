import pytumblr
import json 
import datetime 
import tkinter as tk
from tkinter import messagebox


def send_to_tumblr(body,emotion):
    with open('tumblr.json') as f:
        t = json.load(f)

    client = pytumblr.TumblrRestClient(
        t["consumer_key"],
        t["consumer_secret"],
        t["token"],
        t["token_secret"]
    )

    present = datetime.datetime.now()
    title = present.strftime("%d %B")
    body = present.strftime("** %H %M : **") + body
    return client.create_text("journal.saranmahadev.tech", state="published", title=title, body = body , tags=[emotion])


def callback(body,emotion):
    if body == "":
        messagebox.showerror("Empty Body", "Body is Empty")
    elif emotion == "":
        messagebox.showerror("Empty Emotion", "Emotion is Empty")
    else:
        if send_to_tumblr(body,emotion)['state'] == "published":
            messagebox.showinfo("Succes", "Sent!")
        else:
            messagebox.showerror("Failed", "Unable to send!")

def main():
    
    root = tk.Tk()
    root.title("Journal")
    root.resizable(0,0)
    
    root.wm_iconbitmap(bitmap = "assets/logo.ico")
    
    T1 = tk.Text()
    T1.pack(side = tk.LEFT)
  
    E2 = tk.Entry(root, bd =5)
    E2.pack(side = tk.LEFT)
    
    B = tk.Button(root, text ="Send", command = lambda: callback(T1.get("1.0","end-1c"),E2.get()),width=6,bg="#FD9000")
    B.pack(side=tk.LEFT)

    exit_button = tk.Button(root, text="Exit", command=root.destroy,width=15,bg="#FD9000")
    exit_button.pack(side = tk.BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()