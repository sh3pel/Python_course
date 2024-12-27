import numpy as np
import time
import threading

class CustomQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            self.queue.append(item)

    def get(self):
        with self.lock:
            if self.queue:
                return self.queue.pop(0)
            raise IndexError("get from empty queue")

    def empty(self):
        with self.lock:
            return len(self.queue) == 0

tc, size, value, times = 50, 20, 3, 5
tasks_queue = CustomQueue()

def matrix_multiply(A, B):
    return np.dot(A, B)

class Producer(threading.Thread):
    def __init__(self, consumers_count):
        super().__init__()
        self.consumers_count = consumers_count

    def run(self):
        for task_id in range(tc):
            tasks_queue.put((size + task_id, value, times))
        
        for _ in range(self.consumers_count):
            tasks_queue.put((None, None, None))

class Consumer(threading.Thread):
    def run(self):
        while True:
            try:
                size, value, times = tasks_queue.get()
                if (size, value, times) == (None, None, None):
                    break
            except IndexError:
                continue
            
            matrix = np.fromfunction(lambda i, j: value ** (i + j), (size, size), dtype=int)
            buf = matrix.copy()
            for _ in range(times):
                matrix = matrix_multiply(matrix, buf)

def main(consumers_count):
    producer = Producer(consumers_count)
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
    for threads in range(1, 51):
        print(f"{main(threads)} seconds, {threads} threads")