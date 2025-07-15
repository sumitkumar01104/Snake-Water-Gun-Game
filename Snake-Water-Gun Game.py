import tkinter as tk 
import random

# Global scores
user_score = 0
computer_score = 0

def S_W_G(value):
    global user_score, computer_score

    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, value)
    entry.config(state="readonly")

    You = entry.get()
    label_Entry.config(text=f"You chose: {You}")
    
    Computer = ["Snake", "Water", "Gun"]
    Player = random.choice(Computer)
    label_Player.config(text=f"Computer chose: {Player}")
    
    if You == Player:
        result = "Match Draw"
        color = "gray"
    elif (You == "Snake" and Player == "Water") or \
         (You == "Water" and Player == "Gun") or \
         (You == "Gun" and Player == "Snake"):
        result = "You Win!"
        color = "green"
        user_score += 1
    else:
        result = "You Lose!"
        color = "red"
        computer_score += 1

    label_Result.config(text=f"Result: {result}", fg=color)
    label_Score.config(text=f"Your Score: {user_score}   Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="readonly")
    label_Entry.config(text="")
    label_Player.config(text="")
    label_Result.config(text="")
    label_Score.config(text="Your Score: 0   Computer Score: 0")
# GUI
root = tk.Tk()
root.title("Snake Water Gun Game ")
root.geometry("400x550")

label = tk.Label(root, text="Snake Water Gun Game", font=("Georgia", 20, "bold"))
label.pack(pady=5, padx=5)

entry = tk.Entry(root, font=("Georgia", 16), state="readonly", justify="center",fg='green')
entry.pack(pady=5)

# Buttons
frame = tk.Frame(root)
frame.pack()

button_snake = tk.Button(frame, text="Snake", command=lambda: S_W_G("Snake"), font=("Georgia", 14, "bold"),fg="white",bg="black")
button_snake.pack(padx=2, side="left")

button_water = tk.Button(frame, text="Water", command=lambda: S_W_G("Water"), font=("Georgia", 14, "bold"),fg="white",bg="black")
button_water.pack(padx=2, side="left")

button_gun = tk.Button(frame, text="Gun", command=lambda: S_W_G("Gun"), font=("Georgia", 14, "bold"),fg="white",bg="black")
button_gun.pack(padx=2, side="left")

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Georgia", 14, "bold"),fg="red",bg="black")
reset_button.pack(pady=10)

# Labels
label_Entry = tk.Label(root, font=("Georgia", 16))
label_Entry.pack()

label_Player = tk.Label(root, font=("Georgia", 16))
label_Player.pack()

label_Result = tk.Label(root, font=("Georgia", 16))
label_Result.pack(pady=5)

label_Score = tk.Label(root, text="Your Score: 0   Computer Score: 0", font=("Georgia", 16, "bold"))
label_Score.pack(pady=10)

root.mainloop()
