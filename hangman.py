import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.word_to_guess = self.choose_word().upper()
        self.guess_word = ["_" for _ in self.word_to_guess]
        self.remaining_attempts = 6

        self.display_word = tk.StringVar()
        self.display_word.set(" ".join(self.guess_word))
        self.word_label = tk.Label(root, textvariable=self.display_word, font=("Helvetica", 24))
        self.word_label.pack()

        self.guess_label = tk.Label(root, text="Enter a letter:", font=("Helvetica", 14))
        self.guess_label.pack()
        self.guess_entry = tk.Entry(root, font=("Helvetica", 14))
        self.guess_entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.handle_guess, font=("Helvetica", 14))
        self.guess_button.pack()

        self.message_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.message_label.pack()

    def choose_word(self):
        words = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "RUBY", "PHP", "SWIFT"]
        return random.choice(words)

    def handle_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.word_to_guess:
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.guess_word[i] = guess
            self.display_word.set(" ".join(self.guess_word))
            if "_" not in self.guess_word:
                self.message_label.config(text="Congratulations! You won!")
                self.guess_button.config(state=tk.DISABLED)
        else:
            self.remaining_attempts -= 1
            self.draw_hangman(6 - self.remaining_attempts)
            if self.remaining_attempts == 0:
                self.message_label.config(text=f"Game over! The word was {self.word_to_guess}")
                self.guess_button.config(state=tk.DISABLED)

    def draw_hangman(self, attempts_left):
        if attempts_left == 5:
            self.canvas.create_line(50, 350, 200, 350)
        elif attempts_left == 4:
            self.canvas.create_line(125, 350, 125, 50)
        elif attempts_left == 3:
            self.canvas.create_line(125, 50, 275, 50)
        elif attempts_left == 2:
            self.canvas.create_line(275, 50, 275, 100)
        elif attempts_left == 1:
            self.canvas.create_oval(250, 100, 300, 150)
        elif attempts_left == 0:
            self.canvas.create_line(275, 150, 275, 250)
            self.canvas.create_line(275, 250, 250, 300)
            self.canvas.create_line(275, 250, 300, 300)

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
