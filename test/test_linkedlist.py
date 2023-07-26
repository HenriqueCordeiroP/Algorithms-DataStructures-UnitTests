import pytest
from src.NativeStructures import LinkedList, Node_LinkedList
from src.NativeStructures import DoublyLinked, Node_DoublyLinked

@pytest.mark.parametrize('expected, parameters', [("1 -> None", [1]), ( "1 -> 2 -> 3 -> None", [1, 2, 3]),
("3 -> 2 -> 1 -> None", [3, 2, 1])])
def test_add_node_to_linked_list(expected, parameters):
    ll = LinkedList()
    for i in parameters:
        ll.add_node(Node_LinkedList(i))
    output = ll.get_list()
    assert output == expected

@pytest.mark.parametrize('expected, removed, added_numbers', [("None", 1, [1]), ("1 -> 2 -> None", 3, [1, 2, 3]),
("1 -> 3 -> None", 2, [1, 2, 3]), ("1 -> 2 -> 3 -> None", 4, [1, 2, 3]), ("2 -> 3 -> None", 1, [1, 2, 3])])
def test_remove_node_from_linked_list(expected, removed, added_numbers):
    ll = LinkedList()
    for i in added_numbers:
        ll.add_node(Node_LinkedList(i))
    ll.remove_node(removed)
    output = ll.get_list()
    assert output == expected

@pytest.mark.parametrize('expected, parameters', [("1 <-> None", [1]), ("1 <-> 2 <-> 3 <-> None", [1, 2, 3]),
("1 <-> 2 <-> None", [1, 2])])
def test_add_node_to_doubly_linked_list_ordered(expected, parameters):
    dll = DoublyLinked()
    for i in parameters:
        dll.add_node(Node_DoublyLinked(i))
    output = dll.get_list_in_order()
    assert output == expected

@pytest.mark.parametrize('expected, parameters', [("None <-> 1", [1]), ("None <-> 3 <-> 2 <-> 1", [1, 2, 3]),
("None <-> 2 <-> 1", [1, 2])])
def test_add_node_to_doubly_linked_list_reversed(expected, parameters):
    dll = DoublyLinked()
    for i in parameters:
        dll.add_node(Node_DoublyLinked(i))
    output = dll.get_list_in_reverse()
    assert output == expected

@pytest.mark.parametrize('expected, removed, added_numbers', [("None", 1, [1]), ("1 <-> 3 <-> None", 2, [1, 2, 3]),
("1 <-> 2 <-> None", 3, [1, 2, 3])])
def test_remove_node_from_doubly_linked_list_ordered(expected, removed, added_numbers):
    dll = DoublyLinked()
    for i in added_numbers:
        dll.add_node(Node_DoublyLinked(i))
    dll.remove_node(removed)
    output = dll.get_list_in_order()
    assert output == expected