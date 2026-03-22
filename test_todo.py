import pytest
from todo import Task, TodoList

def test_add_category():
    todo = TodoList()
    todo.add_category("work")
    assert "work" in todo.categories

def test_add_category_duplicate():
    todo = TodoList()
    todo.add_category("work")
    with pytest.raises(ValueError):
        todo.add_category("work")

def test_delete_category():
    todo = TodoList()
    todo.add_category("work")
    todo.delete_category("work")
    assert "work" not in todo.categories

def test_delete_category_missing():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.delete_category("work")

def test_add_task():
    todo = TodoList()
    todo.add_category("work")
    todo.add_task("work", "Finish report")
    assert todo.categories["work"][0].title == "Finish report"

def test_add_task_duplicate():
    todo = TodoList()
    todo.add_category("work")
    todo.add_task("work", "Finish report")
    with pytest.raises(ValueError):
        todo.add_task("work", "Finish report")

def test_add_task_missing_category():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.add_task("work", "Finish report")

def test_delete_task():
    todo = TodoList()
    todo.add_category("work")
    todo.add_task("work", "Finish report")
    todo.delete_task("work", 1)
    assert len(todo.categories["work"]) == 0

def test_complete_task():
    todo = TodoList()
    todo.add_category("work")
    todo.add_task("work", "Finish report")
    todo.complete_task("work", 1)
    assert todo.categories["work"][0].done == True