class Queue():
    def __init__(self):
        self.__list = []
    def is_empty(self):
        return self.__list == []
    def enqueue(self, item):
        return self.__list.append(item)
        # return self.__list.insert(0, item)
    def dequeue(self):
        return self.__list.pop(0)
        # return self.__list.pop()
    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    ll = Queue()
    print(ll.is_empty())
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    print(ll.size())
    print(ll.dequeue())
    print(ll.dequeue())
    print(ll.dequeue())
    print(ll.dequeue())
    print(ll.size())