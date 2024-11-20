# https://contest.yandex.ru/contest/24810/run-report/124744298/

# Сложность пирамидальной сортировки по времени O(n*logn), по памяти О(n),
# где n - к-во участников
# 1. Создание массива для кучи с одним фиктивным элементом и инициализация 
# указателя индекса крайнего элемента в куче
# Далее n итераций:
# 2. На i-той итерациии записываем данные участника в кортеж, (-баллы, штраф, имя)
# так для простоты сравнения участников по имени, по сути реализуется min-heap
# 3. Добавление участника в кучу
# 4. После создания кучи функция print_out выводит имя топа кучи, удаляет, 
# просеивает и повторяет так до 0-го элемента массива кучи

def sift_up(heap, last_idx):
    if last_idx == 1:
        return
    parent = last_idx // 2
    if heap[parent] > heap[last_idx]:
        heap[last_idx], heap[parent] = heap[parent], heap[last_idx]
        sift_up(heap, parent)

def add_to_heap(heap, last_idx, participant):
    heap.append(participant)
    sift_up(heap, last_idx)
    
def sift_down(heap, first, last_idx):
    left, right = first * 2, first * 2 + 1
    if left > last_idx:
        return
    smallest = right if right <= last_idx and heap[right] < heap[left] else left
    if heap[first] < heap[smallest]:
        return
    heap[first], heap[smallest] = heap[smallest], heap[first]
    sift_down(heap, smallest, last_idx)

def print_out(heap, last_idx):
    while last_idx > 0:
        print(heap[1][2])
        heap[1], heap[last_idx] = heap[last_idx], heap[1]
        heap.pop()
        last_idx -= 1
        sift_down(heap, 1, last_idx)
    
if __name__ == '__main__':
    heap = ['=)']
    last_idx = 0
    n = int(input())
    for _ in range(n):
        last_idx += 1
        name, scores, penalty = input().split()
        participant = (-int(scores), int(penalty), name)
        add_to_heap(heap, last_idx, participant)
    print_out(heap, last_idx)