import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.create_board_buttons()

    def create_board_buttons(self):
        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", width=10, height=5,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)

            if self.check_winner(i, j):
                messagebox.showinfo("Vitória", f"Jogador {self.current_player} ganhou!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Empate", "O jogo terminou em empate!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, i, j):
        # Verifica se houve uma vitória na linha, coluna ou diagonal
        symbol = self.board[i][j]
        return (all(self.board[i][c] == symbol for c in range(3)) or    # Linha
                all(self.board[r][j] == symbol for r in range(3)) or    # Coluna
                all(self.board[d][d] == symbol for d in range(3)) or    # Diagonal
                all(self.board[d][2-d] == symbol for d in range(3)))    # Diagonal inversa

    def check_draw(self):
        # Verifica se o jogo terminou em empate
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        # Reinicia o jogo
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()