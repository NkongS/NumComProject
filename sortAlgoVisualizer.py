import tkinter as tk
from tkinter import ttk
import random
import time
from threading import Thread
"""
I have created a sorting algorithm visualizer. 
The program allows the user to visualize the sorting process of various sorting algorithms in real-time and see how long each algorithms takes.

- The generate_random_numbers function generates a list of random numbers within a specified range, which will be used for sorting.
- The sorting algorithms are implemented as generator functions that yield the current state of the list after each iteration.
- The is_sorted function checks if the list is sorted in ascending order.
- The visualize_sorting function creates a separate window to visualize the sorting animation using Tkinter canvas.

The main GUI allows the user to select the number of elements, sorting algorithms, and sorting speed.

The user can select a sorting algorithms from the drop down menu and use the "+" to add it to the list or 
select a sorting algorithms from the list and press the "X" to remove it from the list, and start the visualization of the selected algorithms.

The visualization is done using a canvas with rectangles representing the elements of the list, and the color of the rectangles changes during the sorting process.
The elapsed time is displayed during the sorting process so the sorting algorthms can be compared between each other.

There are 11 sorting algorithms implemented in this code: Bubble Sort, Selection Sort, Insertion Sort, Bogo Sort, Merge Sort, Quick Sort, Heap Sort, Shell Sort, Cocktail Shaker Sort, Comb Sort, and Gnome Sort.
"""


# generate random numbers for sorting
def generate_random_numbers(n):
    return random.sample(range(1, 1000), n)

# sorting algorithms
def bubble_sort(arr, start_time, speed):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, j, j + 1
    yield arr, None, None

def selection_sort(arr, start_time, speed):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, i, min_idx
    yield arr, None, None

def insertion_sort(arr, start_time, speed):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr, i, j + 1
    yield arr, None, None

def bogo_sort(arr, start_time, speed):
    while not is_sorted(arr):
        random.shuffle(arr)
        yield arr, None, None

def merge_sort(arr, start_time, speed):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        yield from merge_sort(L, start_time, speed)
        yield from merge_sort(R, start_time, speed)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            yield arr, k, k
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            yield arr, k, k

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            yield arr, k, k

    yield arr, None, None

def quick_sort(arr, start, end, start_time, speed):
    if start < end:
        pi, arr = partition(arr, start, end)
        yield arr, start, pi
        yield from quick_sort(arr, start, pi - 1, start_time, speed)
        yield from quick_sort(arr, pi + 1, end, start_time, speed)
    yield arr, None, None

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1, arr

def heap_sort(arr, start_time, speed):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        yield from heapify(arr, n, i, start_time, speed)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr, 0, i
        yield from heapify(arr, i, 0, start_time, speed)
    yield arr, None, None

def heapify(arr, n, i, start_time, speed):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr, i, largest
        yield from heapify(arr, n, largest, start_time, speed)

def shell_sort(arr, start_time, speed):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                yield arr, j, j-gap
                j -= gap
            arr[j] = temp
        gap //= 2
    yield arr, None, None

def cocktail_shaker_sort(arr, start_time, speed):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                yield arr, i, i+1
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                yield arr, i, i+1
                swapped = True
        start += 1
    yield arr, None, None

def comb_sort(arr, start_time, speed):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                yield arr, i, i+gap
                sorted = False
            i += 1
    yield arr, None, None

def gnome_sort(arr, start_time, speed):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            yield arr, index, index-1
            index -= 1
    yield arr, None, None

# check if the array is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# visualize sorting algorithms
def visualize_sorting(algorithm, speed, data, algorithm_listbox):
    
    start_time = time.time()

    if algorithm == 'Bubble Sort':
        generator = bubble_sort(data.copy(), start_time, speed)
    elif algorithm == 'Selection Sort':
        generator = selection_sort(data.copy(), start_time, speed)
    elif algorithm == 'Insertion Sort':
        generator = insertion_sort(data.copy(), start_time, speed)
    elif algorithm == 'Bogo Sort':
        generator = bogo_sort(data.copy(), start_time, speed)
    elif algorithm == 'Merge Sort':
        generator = merge_sort(data.copy(), start_time, speed)
    elif algorithm == 'Quick Sort':
        generator = quick_sort(data.copy(), 0, len(data) - 1, start_time, speed)
    elif algorithm == 'Heap Sort':
        generator = heap_sort(data.copy(), start_time, speed)
    elif algorithm == 'Shell Sort':
        generator = shell_sort(data.copy(), start_time, speed)
    elif algorithm == 'Cocktail Shaker Sort':
        generator = cocktail_shaker_sort(data.copy(), start_time, speed)
    elif algorithm == 'Comb Sort':
        generator = comb_sort(data.copy(), start_time, speed)
    elif algorithm == 'Gnome Sort':
        generator = gnome_sort(data.copy(), start_time, speed)

    popup = tk.Toplevel()
    popup.title(f"{algorithm} Sorting Animation")

    algorithm_label = ttk.Label(popup, text=f"Sorting Algorithm: {algorithm}")
    algorithm_label.pack(padx=10, pady=5)

    elapsed_label = ttk.Label(popup, text="Elapsed Time: 0.00 seconds")
    elapsed_label.pack(padx=10, pady=5)

    canvas_width = 800
    canvas_height = 400
    bar_width = canvas_width / len(data)
    bar_spacing = 2
    bar_height_factor = canvas_height / max(data)

    canvas = tk.Canvas(popup, width=canvas_width, height=canvas_height)
    canvas.pack()

    bars = []
    for i, number in enumerate(data):
        x0 = i * bar_width + bar_spacing
        y0 = canvas_height - number * bar_height_factor
        x1 = (i + 1) * bar_width - bar_spacing
        y1 = canvas_height
        bar = canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        bars.append(bar)

    def update_bars(arr, idx1=None, idx2=None):
        for i, number in enumerate(arr):
            x0 = i * bar_width + bar_spacing
            y0 = canvas_height - number * bar_height_factor
            x1 = (i + 1) * bar_width - bar_spacing
            y1 = canvas_height
            if i == idx1 or i == idx2:
                canvas.itemconfig(bars[i], fill='orange')
            elif is_sorted(arr):
                canvas.itemconfig(bars[i], fill='green')
            else:
                canvas.itemconfig(bars[i], fill='red')
            canvas.coords(bars[i], x0, y0, x1, y1)

    def animate_sorting():
        nonlocal generator
        try:
            arr, idx1, idx2 = next(generator)
            update_bars(arr, idx1, idx2)
            elapsed_time = (time.time() - start_time) * (200 / speed) 
            elapsed_label.config(text=f"Elapsed Time: {elapsed_time:.2f} seconds")
            popup.after(int(speed), animate_sorting)
        except StopIteration:
            update_bars(arr)
            elapsed_time = (time.time() - start_time) * (200 / speed)  
            elapsed_label.config(text=f"Elapsed Time: {elapsed_time:.2f} seconds")
            print(f"{algorithm} Sorting completed.")

    animate_sorting()
    algorithm_listbox.insert(tk.END, algorithm)

# create the main GUI
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

number_label = ttk.Label(root, text="Number of elements:")
number_label.grid(row=0, column=0, padx=10, pady=5)

number_entry = ttk.Entry(root, width=10)
number_entry.grid(row=0, column=1, padx=10, pady=5)
number_entry.insert(0, "50") # default number of elements

algorithm_label = ttk.Label(root, text="Select sorting algorithm(s):")
algorithm_label.grid(row=1, column=0, padx=10, pady=5)

algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Bogo Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Shell Sort", "Cocktail Shaker Sort", "Comb Sort", "Gnome Sort"]

algorithm_combo = ttk.Combobox(root, values=algorithms)
algorithm_combo.grid(row=1, column=1, padx=10, pady=5)

selected_algorithms = []
algorithm_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=20, height=4)
algorithm_listbox.grid(row=2, column=1, padx=10, pady=5)

def add_algorithm():
    selected_algorithm = algorithm_combo.get()
    if selected_algorithm not in selected_algorithms:
        selected_algorithms.append(selected_algorithm)
        algorithm_listbox.insert(tk.END, selected_algorithm)
        visualize_button.config(state=tk.NORMAL)

add_button = ttk.Button(root, text="+", width=3, command=add_algorithm)
add_button.grid(row=1, column=2, padx=5, pady=5)

def remove_algorithm():
    selected_index = algorithm_listbox.curselection()
    if selected_index:
        algorithm = algorithm_listbox.get(selected_index)
        selected_algorithms.remove(algorithm)
        algorithm_listbox.delete(selected_index)
        if not selected_algorithms:
            visualize_button.config(state=tk.DISABLED)

remove_button = ttk.Button(root, text="✕", width=3, style='Red.TButton', command=remove_algorithm)
remove_button.grid(row=2, column=2, padx=5, pady=5)

style = ttk.Style()
style.configure('Red.TButton', foreground='red')

speed_label = ttk.Label(root, text="Select sorting speed:")
speed_label.grid(row=3, column=0, padx=10, pady=5)

speed_scale = ttk.Scale(root, from_=200, to=1, orient=tk.HORIZONTAL, length=200)
speed_scale.set(50)  # default speed
speed_scale.grid(row=3, column=1, padx=10, pady=5)

def start_visualization():
    speed = speed_scale.get()
    data = generate_random_numbers(int(number_entry.get()))
    
    for algorithm in selected_algorithms:
        Thread(target=visualize_sorting, args=(algorithm, speed, data, algorithm_listbox)).start()

    algorithm_listbox.delete(0, tk.END)


visualize_button = ttk.Button(root, text="Visualize Sorting", command=start_visualization, state=tk.DISABLED)
visualize_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
