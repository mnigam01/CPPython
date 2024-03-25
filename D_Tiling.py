from itertools import combinations

def can_cover(grid, tiles):
    # Function to recursively cover the grid with tiles
    
    def can_place(tile, row, col):
        # Function to check if a tile can be placed at the given position
        
        # Check if the tile fits within the grid boundaries
        if row + tile[0] > len(grid) or col + tile[1] > len(grid[0]):
            return False
        
        # Check if any cell occupied by the tile is already covered
        for i in range(tile[0]):
            for j in range(tile[1]):
                if grid[row + i][col + j] == 1:
                    return False
        
        return True
    
    def place_tile(tile, row, col, val):
        # Function to place a tile on the grid
        
        for i in range(tile[0]):
            for j in range(tile[1]):
                grid[row + i][col + j] = val
    
    def backtrack(idx):
        # Recursive function to try placing tiles on the grid
        
        if idx == len(tiles):
            # All tiles have been successfully placed
            return True
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if can_place(tiles[idx], i, j):
                    # Try placing the tile at position (i, j)
                    place_tile(tiles[idx], i, j, 1)
                    
                    # Recursively try placing the next tile
                    if backtrack(idx + 1):
                        return True
                    
                    # Backtrack if placing the tile doesn't lead to a solution
                    place_tile(tiles[idx], i, j, 0)
        
        return False
    
    # Start the backtracking process
    return backtrack(0)


def main():
    N, H, W = map(int, input().split())
    tiles = [tuple(map(int, input().split())) for _ in range(N)]
    grid = [[0] * W for _ in range(H)]

    # Generate all possible combinations of tiles
    for r in range(1, N + 1):
        for combo in combinations(tiles, r):
            if can_cover(grid, combo):
                print("Yes")
                return

    print("No")

if __name__ == "__main__":
    main()
