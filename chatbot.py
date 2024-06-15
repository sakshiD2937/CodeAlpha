import tkinter as tk
from tkinter import scrolledtext
import random

class Chatbot:
    def __init__(self):
        self.responses = {
            'greet': ['Hello! How can I help you today?', 'Hi there! What can I do for you?'],
            'bye': ['Goodbye! Have a nice day!', 'Bye! Take care!'],
            'thank': ['You\'re welcome!', 'No problem!'],
            'default': ['I\'m not sure I understand. Can you rephrase?']
        }
        self.patterns = {
            'greet': ['hello', 'hi', 'hey'],
            'bye': ['bye', 'goodbye', 'see you'],
            'thank': ['thank', 'thanks', 'thank you']
        }

    def generate_response(self, user_input):
        user_input = user_input.lower()
        for key, patterns in self.patterns.items():
            if any(pattern in user_input for pattern in patterns):
                return random.choice(self.responses[key])
        return random.choice(self.responses['default'])

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.configure(bg='#2c3e50')

        self.chat_frame = tk.Frame(root, bg='#2c3e50')
        self.chat_frame.pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=60, height=20, state='disabled', bg='#ecf0f1', fg='#2c3e50', font=('Arial', 12))
        self.chat_area.pack()

        self.entry_frame = tk.Frame(root, bg='#2c3e50')
        self.entry_frame.pack(pady=10)

        self.user_input = tk.StringVar()
        self.entry_box = tk.Entry(self.entry_frame, textvariable=self.user_input, width=40, font=('Arial', 12))
        self.entry_box.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message, bg='#3498db', fg='#ecf0f1', font=('Arial', 12))
        self.send_button.pack(side=tk.LEFT)

        self.chatbot = Chatbot()
    
    def send_message(self):
        user_message = self.user_input.get()
        if user_message.strip() == "":
            return

        self.user_input.set("")
        self.display_message("You", user_message)
        
        bot_response = self.chatbot.generate_response(user_message)
        self.display_message("Bot", bot_response)
    
    def display_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
