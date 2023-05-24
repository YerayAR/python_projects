import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
import pygame

pygame.init()
click_sound = pygame.mixer.Sound("C:/Users/yera2/VScode/python/click_sound.wav")
global algo_var

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, i, i


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield from ((arr, i, None) for i in range(low, high + 1))
        yield arr, pi, pi
        yield from quicksort(arr, low, pi - 1)
        yield from quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        yield from merge_sort(arr, l, m)
        yield from merge_sort(arr, m + 1, r)
        yield from merge(arr, l, m, r)
        yield arr, None, None


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l + n1]
    R = arr[m + 1:m + 1 + n2]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        yield arr, k, None

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        yield arr, k, None

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        yield arr, k, None


def update_fig(arr, rects, iteration):
    data, correct_idx, final_idx = arr

    if final_idx is not None:
        final_positions.add(final_idx)
    elif correct_idx in final_positions:
        final_positions.add(correct_idx)

    for idx, (rect, val) in enumerate(zip(rects, data)):
        rect.set_height(val)

        if final_idx is not None:
            if idx >= final_idx and idx <= correct_idx:
                rect.set_color("r")
                if idx not in played_sounds:
                    click_sound.play()
                    played_sounds.add(idx)
            elif idx == correct_idx:
                rect.set_color("b")
            else:
                rect.set_color("silver")
        elif idx == correct_idx:
            rect.set_color("b")
        else:
            rect.set_color("silver")

    plt.title("Iteraciones: {}".format(iteration))


def close_window():
    plt.close()

final_positions = set()
played_sounds = set()

def visualize_sort(algorithm):
    global final_positions
    global played_sounds

    # Limpiar los conjuntos de posiciones finales y sonidos reproducidos
    final_positions = set()
    played_sounds = set()

    # Crear la figura y los objetos de barra
    fig, ax = plt.subplots()
    arr = list(range(1, 22))  # ajustar el número de barras
    random.shuffle(arr)
    rects = plt.bar(range(len(arr)), arr, align="edge", color="silver")

    plt.xticks(range(len(arr)), range(1, len(arr) + 1))
    plt.xlabel("Índice de la barra")
    plt.ylabel("Valor de la barra")

    # Seleccionar el algoritmo correspondiente
    if algorithm == "SelectionSort":
        frames = selection_sort(arr)
    elif algorithm == "QuickSort":
        frames = quicksort(arr, 0, len(arr) - 1)
    elif algorithm == "MergeSort":
        frames = merge_sort(arr, 0, len(arr) - 1)

    # Crear la animación
    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(rects, plt.gcf().canvas.get_renderer()),
                                   frames=frames,
                                   interval=500, repeat=False, cache_frame_data=False)

    plt.show()


def create_window(root):
    root.title("Visualizador de Ordenamiento")
    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text="Selecciona un algoritmo de ordenamiento y presiona el botón para visualizarlo")
    label.pack(pady=10)

    algo_var = tk.StringVar()
    algo_var.set("SelectionSort")

    selection_button = tk.Radiobutton(frame, text="Selection Sort", variable=algo_var, value="SelectionSort")
    selection_button.pack()

    quicksort_button = tk.Radiobutton(frame, text="Quick Sort", variable=algo_var, value="QuickSort")
    quicksort_button.pack()

    merge_sort_button = tk.Radiobutton(frame, text="Merge Sort", variable=algo_var, value="MergeSort")
    merge_sort_button.pack()

    def on_button_click():
        algorithm = algo_var.get()
        visualize_sort(algorithm)

    button = tk.Button(frame, text="Visualizar", command=on_button_click)
    button.pack(pady=10)

if __name__ == '__main__':
  root = tk.Tk()
  create_window(root)
  root.mainloop()