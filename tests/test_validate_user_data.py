from unittest.mock import Mock

from ..lib.validateuserdata import validate_user_data

def test_validate_user_data():
    email = 'email'
    password = 'password'
    data = {'email' : email, 'password' : password}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert validate_user_data(req) == 'false'