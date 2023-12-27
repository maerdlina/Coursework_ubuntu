import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import subprocess

def run_another_file():
    subprocess.call(['python', 'main.py'])
def choose_file():
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def copy_file():
    src = entry.get()
    base, ext = os.path.splitext(src)
    if os.path.basename(src) == "blockMeshDict_old":
        dst = os.path.join(os.path.dirname(src), "blockMeshDict" + ext)
        shutil.copy2(src, dst)
        with open(dst, 'r') as file:
            filedata = file.read()

        p_xf_r_1_value = float(filedata.split("p_xf_r_1_const ")[1].split(";")[0])
        p_xs_r_1_value = float(filedata.split("p_xs_r_1_const ")[1].split(";")[0])
        print(p_xs_r_1_value)
        print(p_xf_r_1_value)
        filedata = filedata.replace("$inlet", a.get())
        filedata = filedata.replace("$outlet_y", str(outlet_entry.get()))
        filedata = filedata.replace("$p_xf_r_1", str(float(p_xf_r_1_value + float(move_entry.get()))))
        filedata = filedata.replace("$p_xs_r_1", str(float(p_xs_r_1_value + float(move_entry.get()))))

        filedata = filedata.replace("$p_xf_r_2", str(float(p_xf_r_1_value + float(move_entry.get()))))
        filedata = filedata.replace("$p_xs_r_2", str(float(p_xs_r_1_value + float(move_entry.get()))))

        with open(dst, 'w') as file:
            file.write(filedata)

def find_replace():
    src = entry.get()
    with open(src, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace("$inlet", a.get())
    with open(src, 'w') as file:
        file.write(filedata)

root = tk.Tk()
root.title("File Copier")

# style = ttk.Style()
# style.theme_use('clam')

# style = ttk.Style()
# style.theme_use('clam')
# style.configure('TButton', background='lightblue', foreground='black', padding=10, font=('Arial', 12))
# style.configure('TEntry', background='white', foreground='black', font=('Arial', 12))
# style.configure('TButton', background='lightblue', foreground='black', padding=10, font=('Arial', 12), borderwidth=5, relief="raised", bordercolor="black", focusthickness=3, focuscolor="none")

replace_button = tk.Button(root, text="Find and Replace", command=find_replace)
replace_button.pack(pady=10)

outlet_entry_lable = tk.Label(root, text="Replacement $outlet:")
outlet_entry_lable.pack()
outlet_entry = ttk.Entry(root)
outlet_entry.pack()

move_entry_lable = tk.Label(root, text="Add +-move:")
move_entry_lable.pack()
move_entry = ttk.Entry(root)
move_entry.pack()

replace_entry_label = tk.Label(root, text="Replacement $inlet:")
replace_entry_label.pack()
a = tk.StringVar()
replace_entry = tk.Entry(root, textvariable=a)
replace_entry.pack()

entry_label = tk.Label(root, text="Selected File Path:")
entry_label.pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

choose_button = tk.Button(root, text="Choose File", command=choose_file)
choose_button.pack()

copy_button = tk.Button(root, text="Copy File", command=copy_file)
copy_button.pack(pady=10)

run_button = tk.Button(root, text="Run Another File", command=run_another_file)
run_button.pack()

exit_button = tk.Button(root, text="EXIT", fg="red", command=root.destroy)
exit_button.pack(side="top", anchor="ne")


root.configure(bg="lightgray")
entry.config(bg="white", fg="black")
choose_button.config(bg="lightblue", fg="black")
copy_button.config(bg="lightgreen", fg="black")
replace_button.config(bg="lightcoral", fg="black")
replace_entry.config(bg="white", fg="black")

root.mainloop()
