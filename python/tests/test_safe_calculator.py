import pytest
from unittest.mock import Mock
from safe_calculator import SafeCalculator

def test_divide_should_not_raise_any_error_when_authorized():
    
    fake_authorizer = Mock()
    fake_authorizer.authorize.return_value = True  

    calculator = SafeCalculator(fake_authorizer)

    result = calculator.add(2, 3)

    assert result == 5
