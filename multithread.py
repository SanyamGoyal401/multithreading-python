from matrices import matrix_list
import time, threading, random as r
import matplotlib.pyplot as plt


def matrix_mul(X, Y):
    result = [[0 for j in range(len(X))] for k in range(len(Y))]
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]


def task(startIndex, endIndex, Y):
    for i in range(startIndex, endIndex+1):
        matrix_mul(matrix_list[i], Y)


def run_threads(num_threads):
    threads = []
    Y = [[r.randint(0, 1000) for j in range(100)] for k in range(100)]
    start_time = time.time()
    chunk_size = len(matrix_list) // num_threads
    active_threads = threading.active_count()
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size - 1 if i < num_threads - 1 else len(matrix_list) - 1
        t = threading.Thread(target=task, args=(start, end, Y.copy()))
        threads.append(t)
        t.start()

    while threading.active_count() != active_threads:
        pass

    return time.time() - start_time


if __name__ == "__main__":
    num_threads_list = list(range(1, 16))
    execution_times = []

    for num_threads in num_threads_list:
        execution_time = run_threads(num_threads)
        execution_times.append(execution_time)
        print(f"Number of threads: {num_threads}, Execution time: {execution_time} seconds")

    plt.plot(num_threads_list, execution_times)
    plt.xlabel('Number of Threads')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Number of Threads vs Execution Time')
    plt.show()