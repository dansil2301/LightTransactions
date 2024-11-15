import threading
import random
import time


class ReadersWriters:
    def __init__(self, priority_policy="Readers-First", max_wait_time=5):
        self.reader_count = 0
        self.writers_waiting = 0
        self.readers_waiting = 0
        self.priority_policy = priority_policy
        self.max_wait_time = max_wait_time

        self.resource_lock = threading.Semaphore(1)
        self.lock = threading.Lock()
        self.reader_lock = threading.Lock()
        self.policy_lock = threading.Lock()

        self.writer_ready = 0
        self.reader_ready = False

    def reader_enter(self):
        start_wait_time = time.time()

        with self.policy_lock:
            self.readers_waiting += 1

        while (self.priority_policy == "Writers-First" and self.writers_waiting > 0 and
               time.time() - start_wait_time < self.max_wait_time) or self.writer_ready > 0:
            pass

        with self.reader_lock:
            self.readers_waiting -= 1
            self.reader_count += 1
            if self.reader_count == 1:
                if self.priority_policy == "Writers-First":
                    self.writer_ready = True
                self.resource_lock.acquire()

    def reader_exit(self):
        with self.reader_lock:
            self.reader_count -= 1
            if self.reader_count == 0:
                if self.priority_policy == "Writers-First":
                    self.writer_ready = False
                self.resource_lock.release()

    def writer_enter(self):
        start_wait_time = time.time()

        with self.policy_lock:
            self.writers_waiting += 1

        while (self.priority_policy == "Readers-First" and (self.reader_count > 0 or self.readers_waiting > 0) and
               time.time() - start_wait_time < self.max_wait_time) or self.reader_ready:
            pass

        with self.policy_lock:
            if self.priority_policy == "Readers-First":
                self.writer_ready += 1
        self.resource_lock.acquire()
        with self.policy_lock:
            if self.priority_policy == "Readers-First":
                self.writer_ready -= 1
            self.writers_waiting -= 1

    def writer_exit(self):
        self.resource_lock.release()
