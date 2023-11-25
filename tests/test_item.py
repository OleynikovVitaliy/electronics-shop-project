"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def first_item():
    return Item("Лампа", 100, 10)


def test_apply_discount(first_item):
    first_item.apply_discount()
    assert first_item.price == 100


def test_calculate_total_price(first_item):
    assert first_item.calculate_total_price() == 1000
