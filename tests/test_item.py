"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from pytest import fixture

from src.item import Item


@fixture


def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000


@pytest.fixture
def item():
    Item.all = []
    item = Item(name="Смартфон", price=10000, quantity=20)
    return item


def test_all_items_list(item):
    assert len(Item.all) == 1
    assert Item.all[0] == item


def test_len_name1(item):
    with pytest.raises(Exception) as e:
        item.name = "Клавиатура1"
        assert str(e.value) == "Длина наименования товара превышает 10 символов"


def test_len_name2(item):
    item.name = "Смартфон"
    assert item.name == "Смартфон"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)

    # Создаем экземпляр класса для проверки магических методов
    item = Item("Смартфон", 10000, 20)

    # Проверяем магический метод __repr__
    assert repr(item) == "Item('Смартфон', 10000, 20)"

    # Проверяем магический метод __str__
    assert str(item) == 'Смартфон'




