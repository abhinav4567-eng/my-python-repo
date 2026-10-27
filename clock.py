import tkinter as tk
from datetime import datetime


def main() -> None:
    root = tk.Tk()
    root.title("Digital Clock")
    root.geometry("420x200")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    time_label = tk.Label(
        root,
        font=("Segoe UI", 48, "bold"),
        fg="#cdd6f4",
        bg="#1e1e2e",
    )
    time_label.pack(expand=True, pady=(20, 0))

    date_label = tk.Label(
        root,
        font=("Segoe UI", 16),
        fg="#a6adc8",
        bg="#1e1e2e",
    )
    date_label.pack(pady=(0, 20))

    def update_clock() -> None:
        now = datetime.now()
        time_label.config(text=now.strftime("%I:%M:%S %p"))
        date_label.config(text=now.strftime("%A, %B %d, %Y"))
        root.after(1000, update_clock)

    update_clock()
    root.mainloop()


if __name__ == "__main__":
    main()