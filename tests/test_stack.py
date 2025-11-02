from pilha import Stack


def test_push_pop():
    s = Stack[int]()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_pop_empty_raises():
    s = Stack()
    try:
        s.pop()
        assert False, "expected IndexError"
    except IndexError:
        assert True
