import tkinter as tk
from tkinter import messagebox
import random

# Fonction pour quitter l'application
def quitter():
    root.quit()

# Fonction pour simuler une pause dans les jeux
def pause():
    messagebox.showinfo("Pause", "Le jeu est en pause.")

# Fenêtre principale de Tkinter
root = tk.Tk()
root.title("Menu de Jeux")
root.geometry("400x400")

# --- Jeu du Morpion ---
def jouer_morpion():
    def verifier_victoire():
        for i in range(3):
            if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
                messagebox.showinfo("Victoire", f"Le joueur {buttons[i][0]['text']} a gagné!")
                return True
            if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
                messagebox.showinfo("Victoire", f"Le joueur {buttons[0][i]['text']} a gagné!")
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            messagebox.showinfo("Victoire", f"Le joueur {buttons[0][0]['text']} a gagné!")
            return True
        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            messagebox.showinfo("Victoire", f"Le joueur {buttons[0][2]['text']} a gagné!")
            return True
        return False

    def clic_case(row, col):
        if buttons[row][col]['text'] == "":
            buttons[row][col]['text'] = current_player.get()
            if verifier_victoire():
                for row in range(3):
                    for col in range(3):
                        buttons[row][col].config(state="disabled")
            else:
                current_player.set("O" if current_player.get() == "X" else "X")

    current_player = tk.StringVar(value="X")
    fenetre_morpion = tk.Toplevel(root)
    fenetre_morpion.title("Jeu du Morpion")
    
    buttons = [[tk.Button(fenetre_morpion, text="", width=10, height=3, command=lambda r=i, c=j: clic_case(r, c)) for j in range(3)] for i in range(3)]
    
    for i in range(3):
        for j in range(3):
            buttons[i][j].grid(row=i, column=j)

# --- Jeu du Motus ---
def jouer_motus():
    # Mot à deviner
    word_to_guess = "python"
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    
    def compare_guess(guess):
        """Compare la tentative avec le mot et retourne le résultat."""
        result = []
        word_list = list(word_to_guess)
        
        # Vérification des lettres bien placées
        for i in range(len(guess)):
            if guess[i] == word_to_guess[i]:
                result.append((guess[i], "correct"))
                word_list[i] = None  # Marquer la lettre comme trouvée
            else:
                result.append((guess[i], "wrong"))
        
        # Vérification des lettres mal placées
        for i in range(len(guess)):
            if result[i][1] == "wrong" and guess[i] in word_list:
                result[i] = (guess[i], "misplaced")
                word_list[word_list.index(guess[i])] = None  # Marquer cette lettre comme traitée
        return result

    def guess_word():
        """Effectue une tentative de deviner le mot."""
        nonlocal attempts
        guess = entry_guess.get().lower()
        if len(guess) != len(word_to_guess):
            messagebox.showinfo("Erreur", f"Le mot doit avoir {len(word_to_guess)} lettres.")
            return
        
        if guess == word_to_guess:
            messagebox.showinfo("Victoire", "Félicitations ! Vous avez trouvé le mot.")
            return

        result = compare_guess(guess)
        guessed_word_display = ""
        for i, (char, status) in enumerate(result):
            if status == "correct":
                guessed_word_display += f"{char.upper()} "  # Lettres bien placées en majuscule
            elif status == "misplaced":
                guessed_word_display += f"{char.lower()} "  # Lettres mal placées en minuscule
            else:
                guessed_word_display += "_ "
        
        label_word.config(text=guessed_word_display.strip())
        attempts -= 1
        label_attempts.config(text=f"Essais restants: {attempts}")
        
        if attempts == 0:
            messagebox.showinfo("Perdu", f"Vous avez perdu ! Le mot était : {word_to_guess}")
            return

    # Création de la fenêtre de jeu Motus
    fenetre_motus = tk.Toplevel(root)
    fenetre_motus.title("Jeu du Motus")

    # Label pour afficher le mot avec les indices
    label_word = tk.Label(fenetre_motus, text=" ".join(guessed_word), font=("Helvetica", 16))
    label_word.pack(pady=20)

    # Label pour afficher le nombre d'essais restants
    label_attempts = tk.Label(fenetre_motus, text=f"Essais restants: {attempts}", font=("Helvetica", 14))
    label_attempts.pack(pady=10)

    # Entrée pour que l'utilisateur devine une lettre
    entry_guess = tk.Entry(fenetre_motus, font=("Helvetica", 16))
    entry_guess.pack(pady=20)

    # Bouton pour valider la tentative
    btn_guess = tk.Button(fenetre_motus, text="Deviner", command=guess_word)
    btn_guess.pack(pady=20)

# --- Jeu du Pendu ---
def jouer_pendu():
    word_to_guess = "python"
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6

    def guess_letter():
        nonlocal attempts
        letter = entry_letter.get()
        if letter in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == letter:
                    guessed_word[i] = letter
            label_word.config(text=" ".join(guessed_word))
            if "".join(guessed_word) == word_to_guess:
                messagebox.showinfo("Victoire", "Vous avez trouvé le mot !")
        else:
            attempts -= 1
            label_attempts.config(text=f"Essais restants: {attempts}")
            if attempts == 0:
                messagebox.showinfo("Perdu", "Vous avez perdu ! Le mot était : " + word_to_guess)
    
    fenetre_pendu = tk.Toplevel(root)
    fenetre_pendu.title("Jeu du Pendu")
    
    label_word = tk.Label(fenetre_pendu, text=" ".join(guessed_word), font=("Helvetica", 16))
    label_word.pack(pady=20)
    
    label_attempts = tk.Label(fenetre_pendu, text=f"Essais restants: {attempts}", font=("Helvetica", 14))
    label_attempts.pack(pady=10)
    
    entry_letter = tk.Entry(fenetre_pendu, font=("Helvetica", 16))
    entry_letter.pack(pady=20)
    
    btn_guess = tk.Button(fenetre_pendu, text="Deviner", command=guess_letter)
    btn_guess.pack(pady=20)

# --- Jeu du Puissance 4 ---
def jouer_puissance4():
    def clic_case(col):
        for row in range(5, -1, -1):
            if grid[row][col]['text'] == "":
                grid[row][col].config(text=current_player.get(), bg="yellow" if current_player.get() == "O" else "red")
                if check_victory(row, col):
                    messagebox.showinfo("Victoire", f"Le joueur {current_player.get()} a gagné !")
                    return
                current_player.set("O" if current_player.get() == "X" else "X")
                break
    
    def check_victory(row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 4):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < 6 and 0 <= c < 7 and grid[r][c]['text'] == current_player.get():
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r, c = row - dr * i, col - dc * i
                if 0 <= r < 6 and 0 <= c < 7 and grid[r][c]['text'] == current_player.get():
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False
    
    current_player = tk.StringVar(value="X")
    fenetre_puissance4 = tk.Toplevel(root)
    fenetre_puissance4.title("Puissance 4")
    
    grid = [[tk.Button(fenetre_puissance4, text="", width=6, height=3, command=lambda c=j: clic_case(c)) for j in range(7)] for i in range(6)]
    
    for i in range(6):
        for j in range(7):
            grid[i][j].grid(row=i, column=j)

# --- Jeu de la Bataille Navale Simplifié ---
def jouer_bataille_navale():
    # Définir la taille de la grille et les navires
    grid_size = 5
    player_board = [["O"] * grid_size for _ in range(grid_size)]
    computer_board = [["O"] * grid_size for _ in range(grid_size)]
    player_ships = 3
    computer_ships = 3

    # Placement aléatoire des navires de l'ordinateur
    def place_computer_ships():
        ships_placed = 0
        while ships_placed < computer_ships:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if computer_board[row][col] == "O":
                computer_board[row][col] = "X"  # X représente un navire
                ships_placed += 1

    place_computer_ships()

    # Vérifier si un navire a été coulé
    def check_victory():
        nonlocal player_ships, computer_ships
        if player_ships == 0:
            messagebox.showinfo("Perdu", "Vous avez perdu ! Les navires de l'ordinateur sont tous coulés.")
            return True
        elif computer_ships == 0:
            messagebox.showinfo("Gagné", "Félicitations ! Vous avez coulé tous les navires de l'ordinateur.")
            return True
        return False

    # Fonction pour tirer une case
    def player_turn(row, col):
        nonlocal computer_ships
        if computer_board[row][col] == "X":
            computer_board[row][col] = "C"  # C représente un navire coulé
            computer_ships -= 1
            messagebox.showinfo("Touché", "Vous avez touché un navire !")
        else:
            messagebox.showinfo("Manqué", "Vous avez manqué.")
        if check_victory():
            return

        computer_turn()

    # Fonction pour le tour de l'ordinateur
    def computer_turn():
        nonlocal player_ships
        while True:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if player_board[row][col] == "O":
                if random.choice([True, False]):  # 50% de chance de toucher
                    player_board[row][col] = "C"
                    player_ships -= 1
                    messagebox.showinfo("L'ordinateur tire", "L'ordinateur a touché un de vos navires !")
                else:
                    player_board[row][col] = "M"  # M pour manqué
                    messagebox.showinfo("L'ordinateur tire", "L'ordinateur a manqué.")
                if check_victory():
                    return
                break

    # Fenêtre de jeu de Bataille Navale
    fenetre_bataille_navale = tk.Toplevel(root)
    fenetre_bataille_navale.title("Jeu de la Bataille Navale")

    # Création de la grille de jeu pour le joueur
    def create_board(board, is_player):
        buttons = []
        for i in range(grid_size):
            row_buttons = []
            for j in range(grid_size):
                if is_player:
                    btn = tk.Button(fenetre_bataille_navale, text="O", width=4, height=2,
                                    command=lambda i=i, j=j: player_turn(i, j))
                else:
                    btn = tk.Button(fenetre_bataille_navale, text="O", width=4, height=2, state="disabled")
                btn.grid(row=i, column=j)
                row_buttons.append(btn)
            buttons.append(row_buttons)
        return buttons

    player_board_buttons = create_board(player_board, is_player=True)
    computer_board_buttons = create_board(computer_board, is_player=False)

    # Message de début
    messagebox.showinfo("Bataille Navale", "Placez vos navires et commencez à jouer !")



# Boutons supplémentaires
btn_pause = tk.Button(root, text="Pause", width=20, command=pause)
btn_pause.pack(pady=10)

btn_quitter = tk.Button(root, text="Quitter", width=20, command=quitter)
btn_quitter.pack(pady=10)

# Lancement de la boucle principale de Tkinter
root.mainloop()
