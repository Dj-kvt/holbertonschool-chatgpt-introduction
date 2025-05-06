#!/usr/bin/python3

def print_board(board):
    """
    Affiche le tableau de jeu
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné
    """
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Exécute le jeu de Tic-Tac-Toe
    """
    board = [[" "]*3 for _ in range(3)]  # Crée un tableau 3x3 vide
    player = "X"
    while True:
        print_board(board)
        row = col = -1

        # Validation de l'entrée de la ligne et de la colonne
        while row not in range(3):
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in range(3):
                    print("Invalid row! Please choose a number between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        while col not in range(3):
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in range(3):
                    print("Invalid column! Please choose a number between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Vérifie si la case est vide
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            # Change de joueur
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()
