import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from health_app.health import Health  

def test_bmi_calculation():
   
    person = Health("Test", 70.0, 1.75)
    assert person.bmi == 22.86

def test_bmi_category():
    assert Health("Under", 50, 1.80).get_category() == "Underweight"
    assert Health("Normal", 70, 1.75).get_category() == "Normal"
    assert Health("Over", 85, 1.75).get_category() == "Overweight"
    assert Health("Obese", 110, 1.75).get_category() == "Obese"

def test_ideal_weight():
    
    person = Health("Test", 70, 1.75)
    assert person.get_ideal_weight() == 67.4

def test_invalid_input():
    with pytest.raises(ValueError):
        Health("", 70, 1.75) 
    with pytest.raises(ValueError):
        Health("Test", -5, 1.75) 
