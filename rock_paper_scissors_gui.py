import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def get_computer_choice():
    """Randomly select between rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player, computer):
    """
    Determine the winner based on traditional rules:
      - Rock crushes Scissors
      - Scissors cuts Paper
      - Paper covers Rock
    If both choices are the same, it's a tie.
    """
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2C3E50')
        
        # Initialize scores
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.current_player_choice = None
        self.current_computer_choice = None

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Game.TButton', font=('Helvetica', 14, 'bold'), padding=10)
        self.style.configure('Title.TLabel', font=('Helvetica', 28, 'bold'), foreground='#ECF0F1')
        self.style.configure('Score.TLabel', font=('Helvetica', 16), foreground='#ECF0F1')
        self.style.configure('Result.TLabel', font=('Helvetica', 18, 'bold'), foreground='#ECF0F1')
        self.style.configure('Choice.TLabel', font=('Helvetica', 14), foreground='#ECF0F1')
        self.style.configure('ChoiceDisplay.TButton', font=('Helvetica', 20, 'bold'), padding=20)
        self.style.configure('Section.TLabel', font=('Helvetica', 20, 'bold'), foreground='#ECF0F1')
        self.style.configure('ScoreFrame.TFrame', background='#34495E')
        self.style.configure('ScoreValue.TLabel', font=('Helvetica', 36, 'bold'), foreground='#2ECC71')
        self.style.configure('ScoreDesc.TLabel', font=('Helvetica', 12), foreground='#BDC3C7')

        # Title
        title_label = ttk.Label(self.main_frame, text="Rock, Paper, Scissors", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Score display frame
        self.score_frame = ttk.Frame(self.main_frame, style='ScoreFrame.TFrame', padding="20")
        self.score_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky='ew')
        
        # Score values
        self.player_score_label = ttk.Label(self.score_frame, text="0", style='ScoreValue.TLabel')
        self.player_score_label.grid(row=0, column=0, padx=40, pady=10)
        
        self.tie_score_label = ttk.Label(self.score_frame, text="0", style='ScoreValue.TLabel')
        self.tie_score_label.grid(row=0, column=1, padx=40, pady=10)
        
        self.computer_score_label = ttk.Label(self.score_frame, text="0", style='ScoreValue.TLabel')
        self.computer_score_label.grid(row=0, column=2, padx=40, pady=10)

        # Score descriptions
        player_desc = ttk.Label(self.score_frame, text="Your wins", style='ScoreDesc.TLabel')
        player_desc.grid(row=1, column=0, padx=40)
        
        tie_desc = ttk.Label(self.score_frame, text="Draw games", style='ScoreDesc.TLabel')
        tie_desc.grid(row=1, column=1, padx=40)
        
        computer_desc = ttk.Label(self.score_frame, text="Computer wins", style='ScoreDesc.TLabel')
        computer_desc.grid(row=1, column=2, padx=40)

        # Choice display frame
        self.choice_display_frame = ttk.Frame(self.main_frame)
        self.choice_display_frame.grid(row=2, column=0, columnspan=3, pady=20)

        # Player choice display
        self.player_choice_label = ttk.Label(self.choice_display_frame, text="Your Choice:", style='Choice.TLabel')
        self.player_choice_label.grid(row=0, column=0, padx=20)
        self.player_choice_display = ttk.Button(
            self.choice_display_frame,
            text="?",
            style='ChoiceDisplay.TButton',
            state='disabled'
        )
        self.player_choice_display.grid(row=0, column=1, padx=20)

        # VS label
        vs_label = ttk.Label(self.choice_display_frame, text="VS", style='Title.TLabel')
        vs_label.grid(row=0, column=2, padx=40)

        # Computer choice display
        self.computer_choice_label = ttk.Label(self.choice_display_frame, text="Computer's Choice:", style='Choice.TLabel')
        self.computer_choice_label.grid(row=0, column=3, padx=20)
        self.computer_choice_display = ttk.Button(
            self.choice_display_frame,
            text="?",
            style='ChoiceDisplay.TButton',
            state='disabled'
        )
        self.computer_choice_display.grid(row=0, column=4, padx=20)

        # Player section label
        player_section_label = ttk.Label(self.main_frame, text="Player's Turn", style='Section.TLabel')
        player_section_label.grid(row=3, column=0, columnspan=3, pady=(20, 10))

        # Player choice buttons
        self.create_choice_buttons()

        # Result labels
        self.result_label = ttk.Label(self.main_frame, text="", style='Result.TLabel')
        self.result_label.grid(row=5, column=0, columnspan=3, pady=20)

        # Reset button
        self.reset_button = ttk.Button(
            self.main_frame,
            text="Reset Score",
            command=self.reset_score,
            style='Game.TButton'
        )
        self.reset_button.grid(row=6, column=0, columnspan=3, pady=20)

    def create_choice_buttons(self):
        # Create buttons for rock, paper, scissors
        choices = ['rock', 'paper', 'scissors']
        for i, choice in enumerate(choices):
            btn = ttk.Button(
                self.main_frame,
                text=choice.capitalize(),
                command=lambda c=choice: self.play_round(c),
                style='Game.TButton'
            )
            btn.grid(row=4, column=i, padx=20, pady=20)

    def update_choice_displays(self, player_choice, computer_choice):
        # Update player choice display
        self.player_choice_display.configure(text=player_choice.upper())
        
        # Update computer choice display
        self.computer_choice_display.configure(text=computer_choice.upper())

    def update_score(self, winner):
        if winner == "player":
            self.player_score += 1
            self.player_score_label.config(text=str(self.player_score))
        elif winner == "computer":
            self.computer_score += 1
            self.computer_score_label.config(text=str(self.computer_score))
        else:
            self.ties += 1
            self.tie_score_label.config(text=str(self.ties))

    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.player_score_label.config(text="0")
        self.computer_score_label.config(text="0")
        self.tie_score_label.config(text="0")
        self.result_label.config(text="")
        self.player_choice_display.configure(text="?")
        self.computer_choice_display.configure(text="?")

    def play_round(self, player_choice):
        computer_choice = get_computer_choice()
        winner = get_winner(player_choice, computer_choice)

        # Update choice displays
        self.update_choice_displays(player_choice, computer_choice)

        # Update result label
        if winner == "tie":
            result_text = "It's a tie! 🤝"
        elif winner == "player":
            result_text = "You win! 🎉"
        else:
            result_text = "Computer wins! 🤖"
        self.result_label.config(text=result_text)

        # Update score
        self.update_score(winner)

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main() 