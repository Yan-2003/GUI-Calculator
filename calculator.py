import tkinter as tk

input_String = ""
def calculate_string(input):
    global input_String
    input_String += str(input)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, input_String)


def eval_calculate_string():
    global input_String
    try:
        input_String = str(eval(input_String))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, input_String)
    except:
        clear_field()
        text_result.insert(1.0, "Error Calculation")

def clear_field():
    global input_String
    input_String = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator")
# this is the text field part
text_result = tk.Text(root, width=16, height=2, font=("Arial", 24), fg="green", bg="black")
text_result.grid(columnspan=5)
# this is the button parts
btn_1 = tk.Button(root, text="1", command=lambda: calculate_string(1), width=5, font=("Arial", 15), fg="white", bg="black")
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: calculate_string(2), width=5, font=("Arial", 15), fg="white", bg="black")
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: calculate_string(3), width=5, font=("Arial", 15), fg="white", bg="black")
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: calculate_string(4), width=5, font=("Arial", 15), fg="white", bg="black")
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: calculate_string(5), width=5, font=("Arial", 15), fg="white", bg="black")
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: calculate_string(6), width=5, font=("Arial", 15), fg="white", bg="black")
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: calculate_string(7), width=5, font=("Arial", 15), fg="white", bg="black")
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: calculate_string(8), width=5, font=("Arial", 15), fg="white", bg="black")
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: calculate_string(9), width=5, font=("Arial", 15), fg="white", bg="black")
btn_9.grid(row=4, column=3)

btn_cls = tk.Button(root, text="C", command=lambda: clear_field(), width=5, font=("Arial", 15), fg="white", bg="red")
btn_cls.grid(row=5, column=1)

btn_0 = tk.Button(root, text="0", command=lambda: calculate_string(0), width=5, font=("Arial", 15), fg="white", bg="black")
btn_0.grid(row=5, column=2)

btn_eq = tk.Button(root, text="=", command=lambda: eval_calculate_string(), width=5, font=("Arial", 15), fg="white", bg="green")
btn_eq.grid(row=5, column=3)

btn_plus = tk.Button(root, text="+", command=lambda: calculate_string("+"), width=5, font=("Arial", 15))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: calculate_string("-"), width=5, font=("Arial", 15))
btn_minus.grid(row=3, column=4)

btn_multi = tk.Button(root, text="*", command=lambda: calculate_string("*"), width=5, font=("Arial", 15))
btn_multi.grid(row=4, column=4)

btn_devide = tk.Button(root, text="/", command=lambda: calculate_string("/"), width=5, font=("Arial", 15))
btn_devide.grid(row=5, column=4)
btn_multi = tk.Button(root, text="*", command=lambda: calculate_string("*"), width=5, font=("Arial", 15))
btn_multi.grid(row=6, column=4)

btn_open = tk.Button(root, text="(", command=lambda: calculate_string("("), width=5, font=("Arial", 15))
btn_open.grid(row=6, column=1)
btn_close = tk.Button(root, text=")", command=lambda: calculate_string(")"), width=5, font=("Arial", 15))
btn_close.grid(row=6, column=2)

btn_erase = tk.Button(root, text="Off", command=lambda: exit(), width=5, font=("Arial", 15))
btn_erase.grid(row=6, column=3)

root.geometry("300x300")
root.mainloop()
