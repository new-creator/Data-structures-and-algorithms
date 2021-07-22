class paixu():
    def bubblesort(self, array):
        for i in range(len(array)-1, 0, -1):
            for j in range(i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def insert(self, array):
        for i in range(1, len(array)):
            for j in range(i):
                if array[j] > array[i]:
                    array[j], array[i] = array[i], array[j]
        return array

    def insert2(self, array):
        for i in range(1, len(array)):
            j = i
            while j > 0:
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break
                j -= 1
        return array

    def shell_sort(self, array):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                j = i
                while j >= gap:
                    if array[j] < array[j-gap]:
                        array[j], array[j-gap] = array[j-gap], array[j]
                    else:
                        break
                    j -= gap
            gap //= 2
        return array

    def choice(self, array):
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        return array

    # 快速排序，中间采用递归
    def quick_sort(self, array, first, last):
        while first >= last:
            return
        low = first
        high = last
        min_value = array[first]
        while low < high:
            while low < high and array[high] >= min_value:
                high -= 1
            array[low] = array[high]
            while low < high and array[low] < min_value:
                low += 1
            array[high] = array[low]
        array[low] = min_value

        self.quick_sort(array, first, low-1)
        self.quick_sort(array, low+1, last)
        return array

    def merge_sort(self, array):
        n = len(array)
        if n <= 1:
            return array
        middle = n // 2
        left = self.merge_sort(array[:middle])
        right = self.merge_sort(array[middle:])
        left_point = 0
        right_point = 0
        result = []
        while left_point < len(left) and right_point < len(right):
            if left[left_point] <= right[right_point]:
                result.append(left[left_point])
                left_point += 1
            else:
                result.append(right[right_point])
                right_point += 1
        result += left[left_point:]
        result += right[right_point:]
        return result

class heap_sort():
    def sift(self, li, low, high):
        # 大顶堆的调整
        i = low #堆顶元素位置
        j = 2*i+1 #左孩子位置
        tmp = li[low]
        while j <= high:
            if j+1 <= high and li[j] < li[j+1]:
                j += 1
            if li[j] > tmp:
                li[i] = li[j]
                i = j
                j = 2*i+1
            else:
                break
        li[i] = tmp

    def sort(self, li):
        n = len(li)
        # 向上调整
        for i in range((n-2)//2, -1, -1):
            self.sift(li, i, n-1)
        for j in range(n-1, -1, -1):
            li[j], li[0] = li[0], li[j]
            self.sift(li, 0, j-1)
        print(li)


if __name__ == '__main__':
    array = [3, 2, 5, 1, 6, 4, 7, 9, 1]
    # paixu = paixu()
    paixu = heap_sort()
    paixu.sort(array)
    # print(paixu.bubblesort(array))
    # print(paixu.insert(array))
    # print(paixu.insert2(array))
    # print(paixu.shell_sort(array))
    # print(paixu.choice(array))
    # print(paixu.quick_sort(array, 0, len(array)-1))
    # print(paixu.merge_sort(array))