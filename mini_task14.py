import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def generate_random_field(size):
    return np.random.choice([0, 1], size=(size, size), p=[0.5, 0.5])

def game_of_life_numpy(field):
    new_field = np.zeros_like(field)
    neighbors = (np.roll(field, 1, 0) + np.roll(field, -1, 0) +
                 np.roll(field, 1, 1) + np.roll(field, -1, 1) +
                 np.roll(np.roll(field, 1, 0), 1, 1) + np.roll(np.roll(field, 1, 0), -1, 1) +
                 np.roll(np.roll(field, -1, 0), 1, 1) + np.roll(np.roll(field, -1, 0), -1, 1))

    new_field[(field == 1) & (neighbors == 2)] = 1
    new_field[(field == 1) & (neighbors == 3)] = 1
    new_field[(field == 0) & (neighbors == 3)] = 1

    return new_field

def game_of_life_python(field):
    size = len(field)
    new_field = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            alive = sum(field[x][y] for x in range(max(0, i - 1), min(size, i + 2))
                        for y in range(max(0, j - 1), min(size, j + 2)) if (x != i or y != j))
            if field[i][j] == 1:
                new_field[i][j] = 1 if alive in (2, 3) else 0
            else:
                new_field[i][j] = 1 if alive == 3 else 0

    return new_field

def update(frame):
    global numpy_field, python_field
    numpy_field = game_of_life_numpy(numpy_field)
    python_field = game_of_life_python(python_field)
    
    ax1.clear()
    ax2.clear()
    
    ax1.set_title("Game of Life - NumPy")
    ax2.set_title("Game of Life - Python Lists")
    
    ax1.imshow(numpy_field, cmap='binary')
    ax2.imshow(python_field, cmap='binary')


size = 128
field_size = 128
iterations = 128

initial_field = generate_random_field(field_size)

#Считаем время для NumPy
start_time_numpy = time.time()
field_numpy = initial_field.copy()
for _ in range(iterations):
    field_numpy = game_of_life_numpy(field_numpy)
end_time_numpy = time.time()
numpy_time = end_time_numpy - start_time_numpy

#Считаем время для Python lists
start_time_python = time.time()
field_python = initial_field.tolist()
for _ in range(iterations):
    field_python = game_of_life_python(field_python)
end_time_python = time.time()
python_time = end_time_python - start_time_python

#анимация
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
numpy_field = initial_field.copy() 
python_field = initial_field.tolist()
animation = FuncAnimation(fig, update, interval=200, cache_frame_data=False)
plt.show()

print(f"Время выполнения NumPy: {numpy_time:.5f} секунд")
print(f"Время выполнения Python (списки): {python_time:.5f} секунд")
