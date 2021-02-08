#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    des: 任务消费类，测试多线程
    author: leslieyuan
    time: 2021-02-08 16:11
    version:
"""
import threading
import time


class TaskQueue(object):
    def __init__(self, nSizeTaskQueue):
        self._maxSize = nSizeTaskQueue
        self._taskQueue = []
        self._lock = threading.Lock()

    def isFull(self):
        return len(self._taskQueue) >= self._maxSize

    def isEmpty(self):
        return len(self._taskQueue) == 0

    def addTask(self, obj):
        if self.isFull():
            return False
        else:
            self._lock.acquire()
            self._taskQueue.append(obj)
            self._lock.release()
        return True

    def getTask(self):
        if not self.isEmpty():
            self._lock.acquire()
            task = self._taskQueue.pop()
            self._lock.release()
            return task
        else:
            print "Task queue is empty"


class ConsumerTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            if self._queue.isEmpty():
                print "Waiting task in..."
                time.sleep(4)
            else:
                task = self._queue.getTask()
                if isinstance(task, str):
                    print "consumer task " ,task


class ProducerTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            if self._queue.isFull():
                print "Queue is full..."
                time.sleep(2)
            else:
                nowtime = str(time.time())
                self._queue.addTask("A task in time " + nowtime)
                time.sleep(1)


if __name__ == '__main__':
    queue = TaskQueue(10)
    c = ConsumerTask(queue)
    p = ProducerTask(queue)
    p.start()
    time.sleep(1)
    c.start()