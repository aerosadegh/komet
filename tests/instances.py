import pytest

from komet import TailPrint


@pytest.fixture(scope="session")
def instance():
    return TailPrint()
