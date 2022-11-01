import pytest

from comet import TailPrint

from .instances import instance


@pytest.fixture(scope="module")
def instance_one():
    return TailPrint()


@pytest.fixture(scope="module")
def instance_two():
    return TailPrint()


def test_singleton(instance_one, instance_two):
    assert id(instance_one) == id(instance_two)


def test_singleton_greedy(instance_one, instance_two, instance):
    assert id(instance_one) == id(instance_two) == id(instance)
