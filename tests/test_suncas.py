import pytest
import sys
sys.path.append('python-biomed') 
# Note that here we need to 
# append the path to the root folder of the project containing suncas in order to import it
import suncas
from suncas import Suncas

"""Test functions"""
def test_is_cute():
    suncas_inst = Suncas(cute = True, sound_volume = 50)
    assert suncas_inst.is_cute() == None

def test_speak():
    suncas_inst = Suncas(cute = True, sound_volume = 50)
    assert suncas_inst.speak() == None

def test_mea():
    suncas_inst = Suncas(cute = True, sound_volume = 50)
    assert suncas_inst.mea() == None

def test_sound_volume_limits():
    with pytest.raises(ValueError):
        suncas_inst = Suncas(cute = True, sound_volume = 1000)

"""The concept of pytest.fixture"""
@pytest.fixture
def typical_suncas():
    # this is not a test function
    # this function provides a context for the test
    suncas_inst1_ = Suncas(cute = True, sound_volume = 50)
    return suncas_inst1_

def test_suncas(typical_suncas):
    # Note that although typical_suncas is declared as a function, here it behaves like a suncas object
    # that is because of the fixture decorator
    # by default when pytest is running a test function, it 
    # searches for the arguments in the test function and 
    # check if it is a fixture function
    # if it is, then the function is executed, and the name of the function is now
    # referenced as the object returned by the function 
    assert typical_suncas.is_cute() == None
    assert typical_suncas.speak() == None
    assert typical_suncas.mea() == None
    with pytest.raises(ValueError):
        suncas_inst = Suncas(cute = True, sound_volume = 1000)
        
