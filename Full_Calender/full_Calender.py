from tkinter import *
from tkinter import ttk, messagebox
import calendar

HOLIDAYS = [
      (1, 14, "Makarshankranti / Pongal"),
    (1, 26, "Republic Day"),
    (8, 15, "Independence Day"),
    (12, 25, "Christmas"),
]

def showCal():
    year_text = year_field.get()

    if not year_text.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid year.")
        return

    fetch_year = int(year_text)
    if fetch_year < 1800 or fetch_year > 9999:
        messagebox.showerror("Invalid Year", "Please enter a year between 1800 and 9999.")
        return

    new_window = Toplevel(root)
    new_window.title(f"Calendar - {fetch_year}")
    new_window.geometry("620x700")
    new_window.config(background="white")

    title = ttk.Label(new_window, text=f"Calendar - {fetch_year}", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    text_frame = Frame(new_window)
    text_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(text_frame, font=("Consolas", 12), yscrollcommand=scrollbar.set)
    text_area.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text_area.yview)

    text_area.tag_config("holiday", foreground="red", font=("Consolas", 12, "bold"))

    for month in range(1, 13):
        month_text = calendar.month(fetch_year, month)
        start_index = text_area.index(END)
        text_area.insert(END, month_text + "\n")
        end_index = text_area.index(END)

        for m, d, name in HOLIDAYS:
            if m != month:
                continue
            search_text = f"{d:2d}"
            pos = text_area.search(search_text, start_index, stopindex=end_index)
            while pos:
                text_area.tag_add("holiday", pos, f"{pos}+2c")
                pos = text_area.search(search_text, f"{pos}+2c", stopindex=end_index)

    text_area.config(state="disabled")

root = Tk()
root.title("Calendar Application")
root.geometry("500x350")
root.config(background="white")

main_title = ttk.Label(root, text="Calendar Application", font=("Arial", 20, "bold"))
main_title.pack(pady=20)

input_frame = Frame(root, bg="white")
input_frame.pack(pady=10)

year_label = ttk.Label(input_frame, text="Enter Year:", font=("Arial", 12))
year_label.grid(row=0, column=0, padx=10, pady=10)

year_field = ttk.Entry(input_frame, width=15)
year_field.grid(row=0, column=1, padx=10, pady=10)

btn_frame = Frame(root, bg="white")
btn_frame.pack(pady=20)

show_btn = ttk.Button(btn_frame, text="Show Calendar", command=showCal)
show_btn.grid(row=0, column=0, padx=15)

clear_btn = ttk.Button(btn_frame, text="Clear", command=lambda: year_field.delete(0, END))
clear_btn.grid(row=0, column=1, padx=15)

exit_btn = ttk.Button(btn_frame, text="Exit", command=root.destroy)
exit_btn.grid(row=0, column=2, padx=15)

root.mainloop()
