from lib import validateuserdata

def main(request):
    return validateuserdata.validate_user_data(request)