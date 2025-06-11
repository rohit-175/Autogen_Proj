import tkinter as tk
import threading
from agents.user_agent import user_proxy
from manager.chat_manager import chat_manager

# Function to submit query
def submit_query():
    user_input = entry.get().strip()
    if not user_input:
        return

    # Keep user's question visible
    entry.delete(0, tk.END)
    entry.insert(0, user_input)

    output_text.delete("1.0", tk.END)
    submit_btn.config(state=tk.DISABLED)

    threading.Thread(target=run_chat, args=(user_input,)).start()

# Background chat execution
def run_chat(user_input):
    chat_result = user_proxy.initiate_chat(
        chat_manager,
        message=user_input,
        summary_method="last_msg",
        silent=True
    )

    final_answer = ""
    for msg in reversed(chat_result.chat_history):
        if msg.get("name") == "Reviewer":
            continue
        if msg.get("role") in ["user", "assistant"]:
            final_answer = msg.get("content")
            break

    if not final_answer:
        final_answer = "[No valid answer found]"

    output_text.after(0, lambda: output_text.insert(tk.END, final_answer))
    submit_btn.after(0, lambda: submit_btn.config(state=tk.NORMAL))


# ---------------------- GUI SETUP ----------------------

root = tk.Tk()
root.title("AutoGen Subject Expert")
root.geometry("700x500")
root.configure(bg="#0d1b2a")

FONT = ("Segoe UI", 12)
FG_COLOR = "#ffffff"
BG_COLOR = "#0d1b2a"
ENTRY_BG = "#1b263b"
TEXT_BG = "#1b263b"
BTN_BG = "#415a77"
BTN_FG = "#ffffff"

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title = tk.Label(frame, text="Ask a Subject Expert", bg=BG_COLOR, fg=FG_COLOR, font=("Segoe UI", 16, "bold"))
title.pack(pady=(0, 10))

entry = tk.Entry(frame, font=FONT, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR, width=60, relief="flat")
entry.pack(pady=(10, 20))

submit_btn = tk.Button(frame, text="Submit", command=submit_query,
                       bg=BTN_BG, fg=BTN_FG, activebackground="#3a506b", relief="flat", font=FONT)
submit_btn.pack()

output_text = tk.Text(frame, height=15, font=FONT, bg=TEXT_BG, fg=FG_COLOR, wrap="word", relief="flat")
output_text.pack(pady=(20, 0), fill="both", expand=True)
output_text.config(state=tk.NORMAL)

root.mainloop()

# Set up GUI
root = tk.Tk()
root.title("AutoGen Subject Expert")
root.geometry("700x500")
root.configure(bg="#0d1b2a")  # Dark background

# Fonts and colors
FONT = ("Segoe UI", 12)
FG_COLOR = "#ffffff"
BG_COLOR = "#0d1b2a"
ENTRY_BG = "#1b263b"
TEXT_BG = "#1b263b"
BTN_BG = "#415a77"
BTN_FG = "#ffffff"

# Frame
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Title
title = tk.Label(frame, text="Ask a Subject Expert", bg=BG_COLOR, fg=FG_COLOR, font=("Segoe UI", 16, "bold"))
title.pack(pady=(0, 10))

# Entry field
entry = tk.Entry(frame, font=FONT, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR, width=60, relief="flat")
entry.pack(pady=(10, 20))

# Submit button
submit_button = tk.Button(frame, text="Submit", command=submit_query,
                          bg=BTN_BG, fg=BTN_FG, activebackground="#3a506b", relief="flat", font=FONT)
submit_button.pack()

# Output Text area
output_text = tk.Text(frame, height=15, font=FONT, bg=TEXT_BG, fg=FG_COLOR, wrap="word", relief="flat")
output_text.pack(pady=(20, 0), fill="both", expand=True)
output_text.config(state=tk.DISABLED)

# Start the app
root.mainloop()