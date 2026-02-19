import random
import time

# Matriz as a plan for apple and snake
matriz = [['.' for j in range(10)] for i in range(10)]
# Direction: Right, Left, Up, Down
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def generate_position(item: str):
    """Generate apple position or starting position of the snake"""
    row = random.randint(0, len(matriz) - 1)
    col = random.randint(0, len(matriz[0]) - 1)
    matriz[row][col] = item
    return (row, col)


# Start snake and apple
snake = [generate_position('@')]
apple = generate_position('*')

# start direction
start_direction = random.choice(direction)
game_should_continue = True

while game_should_continue:

    for i, (r, c) in enumerate(snake):
        d_r, d_c = start_direction
        new_r = r + d_r
        new_c = c + d_c
        try:
            matriz[new_r][new_c] = '@'

        except IndexError:
            r_last_item = len(matriz[r]) - 1
            new_r = 0 if new_r >= r_last_item else new_r
            new_r = r_last_item if new_r < 0 else new_r

            c_last_item = len(matriz) - 1
            new_c = 0 if new_c >= c_last_item else new_c
            new_c = c_last_item if new_c < 0 else new_c

        finally:
            matriz[new_r][new_c] = '@'
            matriz[r][c] = '.'
            snake[i] = (new_r, new_c)

    # Formated and print Matrix
    for i in matriz:
        formated_list = ""
        for j in i:
            formated_list += j + " "
        print(formated_list)

    if game_should_continue:
        time.sleep(0.8)
        print("\n" * 10)
