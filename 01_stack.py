class Stack():
    def __init__(self):
        self.__list = []
    def append(self, item):
        self.__list.append(item)
    def pop(self):
        return self.__list.pop()
    def peak(self):
        if self.__list == []:
            return None
        else:
            return self.__list[-1]
    def is_empty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    ll = Stack()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    print(ll.pop())
    ll.is_empty()