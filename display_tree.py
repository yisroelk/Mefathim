import random 


def create_random_binary_tree(length):
    if length == 0:
        return None

    key = random.randint(1, 1000) 
    # First You should implement the class "TreeNode"
    node = Node(key)

    if length > 1:
        left_length = random.randint(0, length - 1)
        right_length = length - 1 - left_length
        node.left = create_random_binary_tree(left_length)
        node.right = create_random_binary_tree(right_length)

    return node

def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if node.right is None and node.left is None:
        line = '%s' % node.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = '%s' % node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = '%s' % node.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = '%s' % node.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def display_tree(node):
    lines, *_ = _display_aux(node)
    for line in lines:
        print(line)