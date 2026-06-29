def hanoi_solver(n):
    disks = [i + 1 for i in range(n)]   
    rods = {"A": disks[::-1], "B": [], "C": []}

    # Moves as a list so it can be modified inside a helper function
    moves = [f"{rods['A']} {rods['B']} {rods['C']}"]

    def disk_mover(n, source, target, aux):
        # Nothing to move
        if n == 0:
            return       
        # From Source to helper rod
        disk_mover(n-1, source, aux, target)
        target.append(source.pop())
        moves.append(f"{rods['A']} {rods['B']} {rods['C']}")
        # From Helper to target rod
        disk_mover(n-1, aux, target, source)

    disk_mover(n, rods['A'], rods['C'], rods['B'])
    return "\n".join(moves)

if __name__ == "__main__":
    print(hanoi_solver(3))