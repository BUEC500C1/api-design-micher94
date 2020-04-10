from UsingWeatherAPI import weatherdata
import pytest

def test_values():
	weatherdata('IAD') == "Complete"
	weatherdata('BWI') == "Complete"
	weatherdata('DUB') == "Complete"


if __name__ == '__main__':
	main()
