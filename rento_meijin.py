import tkinter   as tk
import pyautogui as gui
import time      as t
import pyperclip

def send(txt, amount): # 送信
    t.sleep(5)

    pyperclip.copy(txt)
    gui.keyDown('command')

    for _ in range(amount):
        gui.press('v')
        gui.press('enter')

    gui.keyUp('command')

# -- tkinter 設定 -- #

root = tk.Tk()
root.title('連投先生')
root.geometry('200x190')

# spinbox入力
var = tk.IntVar(root)
var.set(5)

# 配置
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, pady=7, padx=10)

lbl1 = tk.Label(frame, text='連投する文を入力 ▼')
lbl1.pack(anchor=tk.W, padx=5)

input = tk.Text(frame, bg='white', fg='black', height=5)
input.pack(anchor=tk.W, fill=tk.X)

lbl2 = tk.Label(frame, text='回数')
lbl2.pack(padx=5, side='left')

spinbox = tk.Spinbox(
    frame,
    textvariable = var,
    from_        = 0,
    to           = 1000,
    increment    = 1,
    width        = 10,
    bg           = 'white',
    fg           = 'black'
)

spinbox.pack(side='left')

# ------------------ #

def run(): # 実行用
    s = input.get(1.0, tk.END)
    send( s[:-1], int(spinbox.get()) )

# 実行ボタン
button = tk.Button(text='実行', command=run)
button.pack()

root.mainloop()