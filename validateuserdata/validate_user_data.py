import requests
import flask


def validate_user_data(request: flask.Request) -> str:
    """
    Checks if incoming credentials are valid at the FH Kiel.

    Parameters
    ----------
    request : flask.Request
        The request object.
    
    Returns
    -------
    str
       'true' if credentials are legit and 'false' if they are not.
    """
    email = get_post_parameter(request, 'email')
    password = get_post_parameter(request, 'password')
    if(!(email and password)):
        return 'false'
    payload = set_payload(email, password)
    if 'Cookie' in post_request(payload):
        return 'true'
    return 'false'

def get_post_parameter(request: flask.Request, key: str) -> str or bool:
    """
    Extracts Parameters from a POST request.

    Parameters
    -----------
    request : flask.Request
        The request object.
    key : str
        The key to look for in the request.

    Returns
    -------
    str or bool
        Returns the value of the given key and False otherwise.

    """
    json = request.get_json(silent=True)
    args = request.args
    if json and key in json:
        return json[key]
    elif args and key in args:
        return args[key]
    else:
        return False


def post_request(payload: dict) -> dict:
    """
    Sends POST request to website of the FH Kiel.

    Parameters
    ----------
    payload : dict
        The body of request.
    
    Returns
    -------
    dict
        Returns headers of the response as a dictionary.
    """
    session = requests.Session()
    url = "https://www.fh-kiel.de/index.php?id=3690&L=186%25%2F"
    return session.post(url, data=PAYLOAD).request.headers


def set_payload(email: str, password: str) -> dict:
    """Defines payload for the request to the FH Kiel.

    Parameters
    ----------
    email : str
        email of the user
    password : str
        password of the user

    Returns
    -------
    dict
        Body with all key/value pairs for the request.
    
    """
    return {
        "user": email, 
        "pass": password, 
        "permalogin": "1", 
        "submit": "Anmelden",
        "logintype": "login",
        "pid": "4723,20705",
        "redirect_url": "",
        "tx_felogin_pi1[noredirect]": "0"
    }