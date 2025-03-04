import random
import time

def get_me_random_list(n):
    return [random.randint(1, 1000000) for _ in range(n)]

def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = current_value
    end_time = time.time()
    return end_time - start_time

def shell_sort(a_list):
    start_time = time.time()
    gap = len(a_list) // 2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(a_list, start, gap)
        gap //= 2
    end_time = time.time()
    return end_time - start_time

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap
        a_list[position] = current_value

def python_sort(a_list):
    start_time = time.time()
    a_list.sort()
    end_time = time.time()
    return end_time - start_time

def benchmark_sort(size, num_tests=100):
    insertion_times = []
    shell_times = []
    python_sort_times = []
    for _ in range(num_tests):
        lst = get_me_random_list(size)
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
