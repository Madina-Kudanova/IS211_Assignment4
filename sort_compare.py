import time
import random

def get_random_list(n):
    """Generate a randomized list containing n elements"""
    lst = list(range(n))
    random.shuffle(lst)
    return lst

def insertion_sort(lst):
    start_time = time.time()
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index
        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value
    end_time = time.time()
    return end_time - start_time

def shell_sort(lst):
    start_time = time.time()
    gap = len(lst) // 2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(lst, start, gap)
        gap //= 2
    end_time = time.time()
    return end_time - start_time

def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current_value = lst[i]
        position = i
        while position >= gap and lst[position - gap] > current_value:
            lst[position] = lst[position - gap]
            position -= gap
        lst[position] = current_value

def python_sort(lst):
    start_time = time.time()
    lst.sort()
    end_time = time.time()
    return end_time - start_time

def benchmark_sort(size, num_tests=100):
    insertion_times = []
    shell_times = []
    python_sort_times = []
    for _ in range(num_tests):
        lst = get_random_list(size)
        insertion_times.append(insertion_sort(lst[:]))
        shell_times.append(shell_sort(lst[:]))
        python_sort_times.append(python_sort(lst[:]))
    print(f"List Size: {size}")
    print(f"Insertion Sort took {sum(insertion_times) / num_tests:10.7f} seconds on average")
    print(f"Shell Sort took {sum(shell_times) / num_tests:10.7f} seconds on average")
    print(f"Python Built-in Sort took {sum(python_sort_times) / num_tests:10.7f} seconds on average")
    print("-" * 60)

def main():
    for size in [500, 1000, 5000]:
        benchmark_sort(size)

if __name__ == "__main__":
    main()
