import wolframalpha
import tkinter as tk

print('Package Loaded')

def getAnswer():
    # print("HEY")
    # pass
    query = entry.get()

    # create a response
    res = client.query(query)

    answer = next(res.results).text

    # create a label
    label = tk.Label(root, text=answer)
    # print(type(answer))
    label.pack()

cv_w = 400
cv_h = 300

root = tk.Tk()
canvas = tk.Canvas(root, width=cv_w, height=cv_h, bg='black')
canvas.pack()

# create an entry box
entry = tk.Entry(root)
canvas.create_window(cv_w / 2, cv_h / 2, window=entry)

enterBtn = tk.Button(root, text='Get the Answer', padx=20, pady=10, 
                    fg='white', bg='black', command=getAnswer)
enterBtn.pack()
# ask for users input
# python v2: raw_input
# python v3: input
# input = str(input('Question: '))

# wolframalpha APP ID
APP_ID = 'WU4636-7HLUH76QPL'

# # create a client
client = wolframalpha.Client(APP_ID);
# print(answer)

root.mainloop()