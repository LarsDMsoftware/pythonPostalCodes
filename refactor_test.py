"""
Testing postal code functions from refactor.py

"""

from refactor import readFile, readInput, compareListAndInput, formatOutput, writeOutput


def test_readFile() -> None:
    file = readFile()

    assert(type(file) is dict)
    assert(file["2970"] == "'S Gravenwezel,SCHILDE")