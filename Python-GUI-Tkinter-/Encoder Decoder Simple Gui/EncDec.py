from tkinter import *
import base64

# Initaialize window
window = Tk()
window.geometry('460x480')
window.title('Encoder Decoder')
window.resizable(0 ,0)

# Labels
Label(window, text="Encode Decode", font="lucida 20 bold").pack()
Label(window, text="Nabin", font="lucida 10 bold").pack(side=BOTTOM)

# Declare Variables
inpVal = StringVar()
key = StringVar()
decEnc = StringVar()
Result = StringVar()

# ----------Functions-------------
# Encode Function

def encode_func(Key, Text):
    encoded_data = []
    for i in range(len(Text)):
        key_coded = Key[i % len(Key)]
        encoded_data.append(chr((ord(Text[i]) + ord(key_coded)) % 232))
    return base64.urlsafe_b64encode(''.join(encoded_data).encode()).decode()

# Decode Function

def decode_func(Key, Text):
    decoded_data = []
    Text = base64.urlsafe_b64decode(Text).decode()
    for i in range(len(Text)):
        key_decoded = Key[i % len(Key)]
        decoded_data.append(chr(( ord(Text[i]) - ord(key_decoded)) % 232))
    return ''.join(decoded_data)

# Set Mode function

def set_mode():
    if (decEnc.get() == 'e'):
        Result.set(encode_func(key.get(), inpVal.get()))
    elif (decEnc.get() == 'd'):
        Result.set(decode_func(key.get(), inpVal.get()))
    else:
        Result.set('Please Enter the correct mode!!')
        

# Reset Function
def reset():
    inpVal.set("")
    Result.set("")
    decEnc.set("")
    key.set("")
# Exit Function
def exit_window():
    window.quit()

# ---Labels, Entrys And Buttons
Label(window, text="Input Text: ", font="cursive 12 bold").place(x=21, y=80)
Entry(window, textvariable=inpVal, font='arial 10 bold').place(x=255, y=85)

Label(window, text="Key: ", font="cursive 12 bold").place(x=21, y=130)
Entry(window, textvariable=key, font='arial 10 bold').place(x=255, y=135)

Label(window, text="Type(d-Decode & e-Encode)", font="cursive 12 bold").place(x=21, y=170)
Entry(window, textvariable=decEnc, font='arial 10 bold').place(x=255, y=175)

Button(window, text="Result: ",command=set_mode, font="cursive 12 bold").place(x=210, y=220)
Entry(window, textvariable=Result,fg='red', font='arial 10 bold', width=70).place(x=0, y=270)

Button(window, text="Reset", command=reset, font="cursive 12 bold").place(x=150, y=350)
Button(window, text="Exit",command=exit_window , font="cursive 12 bold").place(x=270, y=350)

window.mainloop()