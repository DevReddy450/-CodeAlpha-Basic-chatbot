import tkinter as tk

# Predefined Q&A
responses = {
  "hello": "hi there!",
  "how are you": "I'm doing well, thank you!",
  "what is python": "Python is a popular programming language.",
  "who are you": "I am a simple chatbot!",
  "what is ai": "AI stands for Artificial Intelligence.",
  "bye": "Goodbye!"
}

# Function to get response
def get_response():
    user_input = entry.get().lower()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = responses.get(user_input, "Sorry, I don't know the answer.")
    chat_log.insert(tk.END, "Bot: " + response + "\n")
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Simple Chatbot")

chat_log = tk.Text(window, height=15, width=50)
chat_log.pack()

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=5, pady=5)

# 🔥 This enables Enter key to trigger the send
entry.bind("<Return>", lambda event: get_response())

send_button = tk.Button(window, text="Send", command=get_response)
send_button.pack(side=tk.LEFT)

window.mainloop()
