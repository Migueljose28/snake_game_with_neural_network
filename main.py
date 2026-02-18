import random

# Matriz as a plan for apple and snake
matriz = [['.' for j in range(10)] for i in range(10)]
# Direction: Right, Left, Up, Down
Direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def generate_position():
    """Generate apple position and starting position of the snake"""
    row = random.randint(0, len(matriz) - 1)
    col = random.randint(0, len(matriz[0]) - 1)
    return row, col


# Generate apple
row, col = generate_position()
matriz[row][col] = '*'

# Start snake
row, col = generate_position()
# list of position of management snake body
snake = [(row, col)]
matriz[row][col] = '@'

# Formated and print Matrix
for i in matriz:
    formated_list = ""
    for j in i:
        formated_list += j + " "
    print(formated_list)
