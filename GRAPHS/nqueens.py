N = 4
queens = [-1] * N

def is_safe(row, col):
    for prev_row in range(row):
        # Check same column or diagonal conflict
        if queens[prev_row] == col or abs(queens[prev_row] - col) == abs(prev_row - row):
            return False
    return True

def solve(row):
    if row == N:
        print_board()
        return
    for col in range(N):
        if is_safe(row, col):
            queens[row] = col
            print(queens)  # Debugging: current state
            solve(row + 1)
            queens[row] = -1  # Backtrack

def print_board():
    for r in range(N):
        row = ['.'] * N
        row[queens[r]] = 'Q'
        print("".join(row))
    print()

solve(0)