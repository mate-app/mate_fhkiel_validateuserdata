import unittest
from requests import Session
from unittest.mock import Mock, patch

from validateuserdata.validate_user_data import *


def test_get_post_parameter_with_valid_json_input():
    """
    Should return valid post-parameter.
    """
    data = {'email' : 'email@example.com'}
    mock_request = Mock(get_json=Mock(return_value=data), args=data)

    post_parameter = get_post_parameter(mock_request, 'email')

    assert post_parameter == 'email@example.com'


def test_get_post_parameter_with_valid_arg_input():
    """
    Should return valid post-parameter.
    """
    data = {'email' : 'email@example.com'}
    mock_request = Mock(get_json=Mock(return_value={}), args=data)

    post_parameter = get_post_parameter(mock_request, 'email')

    assert post_parameter == 'email@example.com'


def test_get_post_parameter_with_invalid_input():
    """
    Should return False.
    """
    data = {}
    mock_request = Mock(get_json=Mock(return_value={}), args=data)

    post_parameter = get_post_parameter(mock_request, 'email')

    assert not(post_parameter)


def test_set_payload():
    """
    Should return valid dict.
    """
    email = 'email@example.com'
    password = '12345678'

    payload = set_payload(email, password)

    assert payload == {
        "user": email, 
        "pass": password, 
        "permalogin": "1", 
        "submit": "Anmelden",
        "logintype": "login",
        "pid": "4723,20705",
        "redirect_url": "",
        "tx_felogin_pi1[noredirect]": "0"
    }


@patch.object(Session, 'post')
def test_post_request(mock_post):
    """
    Should return valid dict of headers.
    """
    mock_post.return_value.request.headers = {'cookies' : 'cookie'}

    headers = post_request({})

    assert headers == {'cookies' : 'cookie'}


@patch.object(Session, 'post')
def test_validate_user_data_with_valid_data(mock_post):
    """
    Should return 'true'.
    """
    data = {'email' : 'email@example.com', 'password' : 'password'}
    mock_request = Mock(get_json=Mock(return_value=data), args=data)
    mock_post.return_value.request.headers = {'Cookie' : 'cookie'}

    result = validate_user_data(mock_request)

    assert result == 'true'


@patch.object(Session, 'post')
def test_validate_user_data_with_invalid_request(mock_post):
    """
    Should return 'false'.
    """
    data = {}
    mock_request = Mock(get_json=Mock(return_value=data), args=data)
    mock_post.return_value.request.headers = {'Cookie' : 'cookie'}

    result = validate_user_data(mock_request)

    assert result == 'false'


@patch.object(Session, 'post')
def test_validate_user_data_with_invalid_data(mock_post):
    """
    Should return 'false'.
    """
    data = {'email' : 'email@example.com', 'password' : 'password'}
    mock_request = Mock(get_json=Mock(return_value=data), args=data)
    mock_post.return_value.request.headers = {'noCookie' : 'no cookie'}

    result = validate_user_data(mock_request)

    assert result == 'false'