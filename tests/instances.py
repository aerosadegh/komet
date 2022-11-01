import pytest

from comet import TailPrint


@pytest.fixture(scope="session")
def instance():
    return TailPrint()
