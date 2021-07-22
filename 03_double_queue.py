class Queue():
    def __init__(self):
        self.__list = []
    def is_empty(self):
        return self.__list == []
    def add_front(self, item):
        return self.__list.insert(0, item)
    def add_rear(self, item):
        return self.__list.append(item)
    def pop_front(self):
        return self.__list.pop(0)
    def pop_rear(self):
        return self.__list.pop()
    def dequeue(self):
        return self.__list.pop(0)
        # return self.__list.pop()
    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    ll = Queue()
    print(ll.is_empty())
    ll.add_front(1)
    ll.add_rear(3)
    ll.add_rear(4)
    ll.add_front(1)
    print(ll.size())
    print(ll.pop_front())
    print(ll.pop_rear())
    print(ll.size())