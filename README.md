This is a sorting algorithm visualizer. 
The program allows the user to visualize the sorting process of various sorting algorithms in real-time and see how long each algorithms takes.

- The generate_random_numbers function generates a list of random numbers within a specified range, which will be used for sorting.
- The sorting algorithms are implemented as generator functions that yield the current state of the list after each iteration.
- The is_sorted function checks if the list is sorted in ascending order.
- The visualize_sorting function creates a separate window to visualize the sorting animation using Tkinter canvas.

**How to Use:** \
The main GUI allows the user to select the number of elements, sorting algorithms, and sorting speed.

The user can select a sorting algorithms from the drop down menu and use the "+" to add it to the list or 
select a sorting algorithms from the list and press the "X" to remove it from the list, and start the visualization of the selected algorithms.

The visualization is done using a canvas with rectangles representing the elements of the list, and the color of the rectangles changes during the sorting process.
The elapsed time is displayed during the sorting process so the sorting algorthms can be compared between each other.

There are 11 sorting algorithms implemented in this code: Bubble Sort, Selection Sort, Insertion Sort, Bogo Sort, Merge Sort, Quick Sort, Heap Sort, Shell Sort, Cocktail Shaker Sort, Comb Sort, and Gnome Sort.
