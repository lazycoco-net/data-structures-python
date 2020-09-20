from typing import NoReturn

import pytest

from lazycoco.stack import MyStack, EmptyStackException


def test_int_push_three_and_pop_one() -> NoReturn:
    # Given
    stack: MyStack[int] = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # When
    element: int = stack.pop()

    # Then
    assert element == 3
    assert stack.peek() == 2
    assert stack.peek() == 2
    assert not stack.empty()


def test_integer_push_three_and_pop_three() -> NoReturn:
    # Given
    stack: MyStack[int] = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # When
    first_empty_check: bool = stack.empty()
    first_peek: int = stack.peek()
    second_empty_check: bool = stack.empty()
    first_popped_element: int = stack.pop()
    third_empty_check: bool = stack.empty()
    second_peek: int = stack.peek()
    fourth_empty_check: bool = stack.empty()
    second_popped_element: int = stack.pop()
    fifth_empty_check: bool = stack.empty()
    third_peek: int = stack.peek()
    sixth_empty_check: bool = stack.empty()
    third_popped_element: int = stack.pop()
    seventh_empty_check = stack.empty()

    # Then
    assert first_peek == 3
    assert first_popped_element == 3
    assert second_peek == 2
    assert second_popped_element == 2
    assert third_peek == 1
    assert third_popped_element == 1
    assert not first_empty_check
    assert not second_empty_check
    assert not third_empty_check
    assert not fourth_empty_check
    assert not fifth_empty_check
    assert not sixth_empty_check
    assert seventh_empty_check


def test_str_push_one_and_pop_one() -> NoReturn:
    # Given
    stack: MyStack[str] = MyStack()
    stack.push('one')

    # When
    element: str = stack.pop()

    # Then
    assert element == 'one'
    assert stack.empty()


def test_pop_throws_exception_when_empty() -> NoReturn:
    # Given
    stack: MyStack[int] = MyStack()

    # When # Then
    with pytest.raises(EmptyStackException):
        stack.pop()


def test_peek_throws_exception_when_empty() -> NoReturn:
    # Given
    stack: MyStack[int] = MyStack()

    # When # Then
    with pytest.raises(EmptyStackException):
        stack.peek()
