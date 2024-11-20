# https://contest.yandex.ru/contest/24810/run-report/124999514/

# алгоритм работает за О(h), h - высота дерева. дополнительной памяти 
# не тратит - O(1)
# 1. ищем ноду подлежащую удалению. если не находим - то не находим)
# 2. когда нашли - проверяем есть-ли левое и правое поддеревья, если 
# только одно существует, то вернём по стеку ссылку на существующее.
# в противном случае запускаем функцию hard_to_stbd которая пройдёт 
# в левом поддереве до самого правой ноды swap и:
#    2.1 вернёт левого ребёнка ноды swap - y и саму swap. функция вернёт
#        по стеку левого ребёнка y и привяжет его к родителю swap.right,
#        и, в конце вернёт корень изменённого левого поддерева
# 3. потом просто к swap.left вешаем корень левого поддерева, а к swap.right
# правое поддерево ноды которую удаляем

from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node

def hard_to_stbd(node):
    if not node.right:
        return node.left, node
    node.right, swap = hard_to_stbd(node.right)
    return node, swap

def remove(root, key) -> Optional[Node]:
    if not root:
        return root
    if root.value < key:
        root.right = remove(root.right, key)
    elif root.value > key:
        root.left = remove(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        y, swap = hard_to_stbd(root.left)
        swap.left, swap.right = y, root.right
        return swap
    return root



def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == '__main__':
    test()