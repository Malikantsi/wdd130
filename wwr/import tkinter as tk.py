import tkinter as tk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.question_index = 0
        
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 5 + 3?", "options": ["5", "8", "12", "15"], "answer": "8"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"}
        ]
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.buttons = []
        for _ in range(4):
            btn = tk.Button(root, text="", width=20, command=lambda b=_: self.check_answer(b))
            btn.pack(pady=5)
            self.buttons.append(btn)
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=20)
        
        self.load_question()
        
    def load_question(self):
        if self.question_index < len(self.questions):
            q = self.questions[self.question_index]
            self.question_label.config(text=q["question"])
            
            for i, option in enumerate(q["options"]):
                self.buttons[i].config(text=option)
        else:
            self.question_label.config(text="Quiz Over!")
            for btn in self.buttons:
                btn.config(state=tk.DISABLED)
        
    def check_answer(self, index):
        selected_option = self.buttons[index].cget("text")
        correct_answer = self.questions[self.question_index]["answer"]
        
        if selected_option == correct_answer:
            self.score += 1
        
        self.score_label.config(text=f"Score: {self.score}")
        self.question_index += 1
        self.load_question()
        
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
