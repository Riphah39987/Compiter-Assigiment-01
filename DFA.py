import tkinter as tk
from tkinter import messagebox, Canvas

# DFA Transitions
transitions = {
    "q0": {"a": "q1", "b": "q2"},
    "q1": {"a": "q0", "b": "q3"},
    "q2": {"a": "q3", "b": "q0"},
    "q3": {"a": "q2", "b": "q1"}
}

def simulate_dfa():
    state = "q0"
    for char in entry.get():
        if char not in "ab":
            messagebox.showerror("Error", "❌ Invalid character! Use only 'a' and 'b'.")
            return
        state = transitions[state][char]
        update_visual(state)
        root.update()
        root.after(500)

    if state == "q0":
        messagebox.showinfo("Result", "✅ Accepted")
    else:
        show_rejected_popup()  # Custom rejected message

def show_rejected_popup():
    reject_popup = tk.Toplevel(root)
    reject_popup.title("Result")
    reject_popup.geometry("250x100")
    reject_popup.configure(bg="#FF0000")  # Vibrant red background

    tk.Label(reject_popup, text="❌ Rejected", font=("Arial", 14, "bold"), fg="white", bg="#FF0000").pack(pady=20)
    tk.Button(reject_popup, text="OK", font=("Arial", 12), bg="black", fg="white", command=reject_popup.destroy).pack()

def update_visual(state):
    canvas.delete("highlight")
    x, y = state_positions[state]
    canvas.create_oval(x-30, y-30, x+30, y+30, outline="#FF5733", width=4, tags="highlight")

# GUI Setup
root = tk.Tk()
root.title("DFA Simulator")
root.geometry("420x450")
root.configure(bg="#1E1E1E")  # Dark background

tk.Label(root, text="Even-Even DFA Simulator", font=("Arial", 16, "bold"), fg="#FFD700", bg="#1E1E1E").pack(pady=10)
tk.Label(root, text="Enter a string (a, b):", font=("Arial", 12), fg="white", bg="#1E1E1E").pack()
entry = tk.Entry(root, font=("Arial", 14), width=15, bg="#333", fg="white", insertbackground="white")
entry.pack(pady=5)

tk.Button(root, text="Simulate", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=simulate_dfa).pack(pady=10)
canvas = Canvas(root, width=400, height=300, bg="#333")
canvas.pack()

# Draw DFA states
state_positions = {"q0": (100, 100), "q1": (300, 100), "q2": (100, 250), "q3": (300, 250)}
for state, (x, y) in state_positions.items():
    canvas.create_oval(x-25, y-25, x+25, y+25, fill="#007BFF", outline="white")
    canvas.create_text(x, y, text=state, font=("Arial", 12, "bold"), fill="white")

tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="#FF3B3B", fg="white", command=root.quit).pack(pady=10)

root.mainloop()
