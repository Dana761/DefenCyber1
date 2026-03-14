import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            temp = counter
            time.sleep(0.000001)
            counter = temp + 1

threads = []

for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)
print("Expected value:", 100000 * 5)