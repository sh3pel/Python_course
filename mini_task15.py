import threading
import queue
import numpy as np
import time

task_queue = queue.Queue()
lock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self, num_tasks):
        super().__init__()
        self.num_tasks = num_tasks

    def run(self):
        for i in range(self.num_tasks):
            size = i + 1  
            value = 2  
            times = 3 
            task = (size, value, times)
            with lock:
                task_queue.put(task)
                print(f'Produced: {task}')
            time.sleep(0.1)  # Задержка для имитации работы

class Consumer(threading.Thread):
    def run(self):
        while True:
            try:
                task = task_queue.get(timeout=1) 
                if task is None: 
                    break
                size, value, times = task
                A = np.fromfunction(lambda i, j: value ** (i + j), (size, size), dtype=int)
                A = np.linalg.matrix_power(A, times)
                result = np.sum(A) 
                print(f'Consumed: {task}, Result: {result}')
                time.sleep(0.1)  # Задержка для имитации работы
            except queue.Empty:
                break

def main(num_consumers, num_tasks):
    producer = Producer(num_tasks)
    consumers = [Consumer() for _ in range(num_consumers)]

    producer.start()
    for consumer in consumers:
        consumer.start()

    producer.join() 

    for _ in consumers:
        task_queue.put(None)

    for consumer in consumers:
        consumer.join()

if __name__ == "__main__":
    num_consumers = 4
    num_tasks = 10
    start_time = time.time()
    main(num_consumers, num_tasks)
    end_time = time.time()
    print(f'Total time taken: {end_time - start_time:.2f} seconds')