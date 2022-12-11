
def võitja(game_grid):
    o_count = game_grid.count(['O','O','O','O'])
    x_count = game_grid.count(['X','X','X','X'])

    for row_i in range(3):
        for col_i in range(2):
            if game_grid[row_i][col_i] == game_grid[row_i][col_i+1] == game_grid[row_i][col_i+2] == 'O':
                o_count += 1
            if game_grid[row_i][col_i] == game_grid[row_i][col_i+1] == game_grid[row_i][col_i+2] == 'X':
                x_count += 1

    for col_i in range(3):
        for row_i in range(2):
            if game_grid[row_i][col_i] == game_grid[row_i+1][col_i] == game_grid[row_i+2][col_i] == 'O':
                o_count += 1
            if game_grid[row_i][col_i] == game_grid[row_i+1][col_i] == game_grid[row_i+2][col_i] == 'X':
                x_count += 1

    for row_i in range(2):
        for col_i in range(3, 0, -1):
            if game_grid[row_i][col_i] == game_grid[row_i+1][col_i-1] == game_grid[row_i+2][col_i-2] == 'O':
                o_count += 1
            if game_grid[row_i][col_i] == game_grid[row_i+1][col_i-1] == game_grid[row_i+2][col_i-2] == 'X':
                x_count += 1


        if game_grid[row_i][row_i] == game_grid[row_i+1][row_i+1] == game_grid[row_i+2][row_i+2] == 'O':
            o_count += 1
        elif game_grid[row_i][row_i] == game_grid[row_i+1][row_i+1] == game_grid[row_i+2][row_i+2] == 'X':
            x_count += 1

    return {'O': o_count, 'X': x_count}
