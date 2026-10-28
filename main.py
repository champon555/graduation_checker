import logic
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import scrolledtext

def find_csv():
    csv_path = filedialog.askopenfilename()
    if not csv_path:
        return
    selected_course = combo.get()
    if var_jh.get() and var_hs.get():
        selected_certification = "中高英語"
    elif var_jh.get():
        selected_certification = "中学英語"
    elif var_hs.get():
        selected_certification = "高校英語"
    else:
        selected_certification = "資格なし"

    df_filled = logic.load_csv(csv_path)
    grad_res = logic.graduation_check(df_filled, selected_course)

    if selected_certification != "資格なし":
        cer_res = logic.certification_check(df_filled, selected_certification)
        final_text = "卒業判定" +"\n\n" + grad_res + "\n\n" +  selected_certification + "\n\n" + cer_res
    else:
        final_text = grad_res

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, final_text)


root = tk.Tk()
root.title("credits checker")
root.geometry("500x600")

label_1 = tk.Label(root, text = "専攻を選択してください。" "\n" "ゼミが決まっていない場合は進みたい方を選択してください。", foreground = "white")
label_1.pack(expand = True)

option = list(logic.Department.keys())
variable = tk.StringVar () 
combo = ttk.Combobox (root , values = option , textvariable = variable)
combo.pack(expand = True)

label_2 = tk.Label(root, text = "取得を目指している資格をチェックしてください。", foreground = "white")
label_2.pack(expand = True)

var_jh = tk.IntVar()

check_1 = tk.Checkbutton(root, text = "中学校英語教員免許", foreground = "white", variable = var_jh)
check_1.pack(expand = True)

var_hs = tk.IntVar()

check_2 = tk.Checkbutton(root, text = "高校英語教員免許", foreground = "white", variable = var_hs)
check_2.pack(expand = True)

button = tk.Button(root, text = "ファイルを選択して判定", command = find_csv)
button.pack(expand = True)

result_box = scrolledtext.ScrolledText(root, width=55, height=18)
result_box.pack(pady=10)

root.mainloop()