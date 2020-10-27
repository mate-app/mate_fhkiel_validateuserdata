import requests
import flask

def extract_parameter(request_json, request_args, name):
    if request_json and name in request_json:
        return request_json[name]
    elif request_args and name in request_args:
        return request_args[name]
    else:
        return False

def validate_user_data(request):
    """Returns JSON body which indicates whether or not the given credential are legit."""
    request_json = request.get_json(silent=True)
    request_args = request.args

    email = extract_parameter(request_json, request_args, 'email')
    password = extract_parameter(request_json, request_args, 'password')

    if (email and password):
        PAYLOAD = {
            "user": email, 
            "pass": password, 
            "permalogin": "1", 
            "submit": "Anmelden",
            "logintype": "login",
            "pid": "4723,20705",
            "redirect_url": "",
            "tx_felogin_pi1[noredirect]": "0"
        }
    else:
        return 'false'
    
    session = requests.Session()
    url = "https://www.fh-kiel.de/index.php?id=3690&L=186%25%2F"
    response = session.post(url, data=PAYLOAD)
    if 'Cookie' in response.request.headers:
        return 'true'
    return 'false'