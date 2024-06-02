import pytest
import GUI_finished

@pytest.mark.parametrize("input",["A","B","C"])
def test_AdresseIP(input:chr):
    a = "3"
    assert type(a) == str

@pytest.mark.parametrize("input",["A","B","C"])
def Prt_valide(input:int):
    a = "3"
    assert type(a) == str