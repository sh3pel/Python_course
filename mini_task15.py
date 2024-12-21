import numpy as np
import time
import threading
import queue

tc, size, value, times = 50, 20, 3, 5
tasks_queue = queue.Queue()

def matrix_multiply(A, B):
    return np.dot(A, B)

class Producer(threading.Thread):
    def run(self):
        for _ in range(tc):
            tasks_queue.put((size + _, value, times))

class Consumer(threading.Thread):
    def run(self):
        while True:
            try:
                size, value, times = tasks_queue.get(timeout=1)
            except queue.Empty:
                break

            matrix = np.fromfunction(lambda i, j: value ** (i + j), (size, size), dtype=int)
            buf = matrix.copy()
            for _ in range(times):
                matrix = matrix_multiply(matrix, buf)
            tasks_queue.task_done()

def main(consumers_count):
    producer = Producer()
    consumers = [Consumer() for _ in range(consumers_count)]

    start_time = time.time()
    producer.start()
    for consumer in consumers:
        consumer.start()

    producer.join()
    for consumer in consumers:
        consumer.join()

    return round(time.time() - start_time, 3)

if __name__ == '__main__':
    for threads in range(50):
        print(f"{main(threads)} seconds, {threads} threads")
