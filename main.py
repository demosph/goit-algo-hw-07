from avl_node import AVLNode

def get_height(node):
    if not node:
       return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    if node is None:
        return 0
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    return node.height

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def find_max_value_avl(root):
    # Якщо дерево порожнє, повертаємо None
    if root is None:
        return None

    # Йдемо по дереву вправо до кінця, оскільки найбільше значення буде знаходитися в останньому вузлі
    while root.right is not None:
        root = root.right

    return root.key

def find_min_value_avl(root):
    # Якщо дерево порожнє, повертаємо None
    if root is None:
        return None

    # Йдемо по дереву вліво до кінця, оскільки найменше значення буде знаходитися в останньому вузлі
    while root.left is not None:
        root = root.left
    return root.key

def sum_of_values_avl(root):
    # Якщо дерево порожнє, повертаємо 0
    if root is None:
        return 0

    # Рекурсивно обчислюємо суму для лівого та правого піддерев
    left_sum = sum_of_values_avl(root.left)
    right_sum = sum_of_values_avl(root.right)

    # Сума значень в поточному вузлі та його дочірніх вузлах
    return root.key + left_sum + right_sum

def main():
    root = AVLNode(10)
    keys = [5, 15, 3, 7, 12, 18, 4, 6, 8, 9, 11, 13, 14, 16, 17, 19, 20]
    for key in keys:
        root = insert(root, key)

    print("AVL-Tree:\n", root)

    # Максимальне значення в AVL-дереві
    max_value = find_max_value_avl(root)
    print("Max value in AVL-tree:", max_value)
    # Мінімальне значення в AVL-дереві
    min_value = find_min_value_avl(root)
    print("Min value in AVL-tree:", min_value)
    # Сума значень в AVL-дереві
    total_sum = sum_of_values_avl(root)
    print("Total sum of values in AVL-tree:", total_sum)

if __name__ == "__main__":
    main()