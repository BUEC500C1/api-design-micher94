from UsingWeatherAPI import weatherdata
import pytest

def test_values():
	weatherdata('IAD') == True
	weatherdata('BWI') == True
	weatherdata('DUB') == True
	weatherdata('ID') == False
	weatherdata('###') == False
	weatherdata('123') == False
