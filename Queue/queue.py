#Create Queue use empty List
class Queue:
    def __init__(self):
        self.queue = []

    def Enqueue(self, dataVal):
        #Append method to add element ->add last
        if dataVal not in self.queue:
            self.queue.append(dataVal)
            return True
        return False

    def Dequeue(self):
        #Pop method to remove element --> pop first
        if len(self.queue) <= 0:
            print('No elements in Queue')
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def queueprint(self):
        if (len(self.queue) <= 0):
            print('No elements in Queue')
        else:
            for elem in self.queue:
                print(elem)

queue = Queue()
queue.Enqueue('Mon')
queue.Enqueue('Tue')
queue.Enqueue('Wed')
queue.Enqueue('Thu')
queue.Enqueue('Fri')
queue.Enqueue('Sat')
queue.Enqueue('Sun')
queue.queueprint()
print(queue.size())
print('-------')

queue.Dequeue()
queue.queueprint()
print(queue.size())
print('-------')
queue.Dequeue()
queue.queueprint()
print(queue.size())
print('-------')
