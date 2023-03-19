import lesson_13


def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовательности 
    из круглых и квадратных скобок () []

    >>> is_braces_sequence_correct("(([()]))[]"):
    True
    >>> is_braces_sequence_correct("([)]"):
    False
    >>> is_braces_sequence_correct("("):
    False
    >>> is_braces_sequence_correct("]"):
    False
    """
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            lesson_13.push(brace)
        else:
            assert brace in ")]", "Ожидалась закрывающая скобка" + str(brace)
            if lesson_13.is_empty():
                return False
            left = lesson_13.pop()
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return lesson_13.is_empty()
     
                