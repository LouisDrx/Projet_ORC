import pytest
import GUI_finished

@pytest.mark.parametrize("input",["192.168.0.01","192.168.100.21"])
def test_AdresseIP(input:chr):
    
    assert len(input)>=11 , "L'IP attendu fait au moins 12 characteres"
    assert len(input)<=15 , "L'IP attendu fait au plus 15 characteres"
    assert int(input[0:3]) == 192 , "IP =192.168.X.X"
    assert int(input[4:7]) == 168 , "IP =192.168.X.X"


@pytest.mark.parametrize("input",["4","30"])
def Port_valide(input:chr):

    assert int(type(input)) >0 , "port >0"


