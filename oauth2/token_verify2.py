from rest_framework.views import APIView
from oauth2client import client, crypt
from rest_framework.response import Response
from oauth2_provider.models import (
    AccessToken,
    RefreshToken,
    clear_expired
)
import requests
import json


def send_get_to_debug_token_fb(input_token, access_token):
    url = 'https://graph.facebook.com/debug_token'
    payload = {'input_token': input_token, 'access_token': access_token}
    r = requests.get(url, params=payload, )
    response = json.loads(r.content)
    user_id = response['data']['user_id']
    app_id = response['data']['app_id']
    is_valid = response['data']['is_valid']
    if is_valid:
        if app_id in ['',]:
            r = {'message': 'valid', 'user_id': user_id}
            return Response(r)
        else:
            user_id = ''
            r = {'message': 'app id not valid', 'user_id': user_id}
            return Response(r)
    else:
        user_id = ''
        r = {'message': 'Invalid', 'user_id': user_id}
        return Response(r)


class VerifyUser(APIView):
    CLIENT_ID = '563936792008-qsd946svnd2ptu5sdsrqi2q63dn37fvd.apps.googleusercontent.com'
    # client_secret = 'PkIP-kphbiRnXXwrgfmT9v-H'
    def post(self,request):
        verify_via = request.data['verify_via']
        client_id = request.data['client_id']
        if client_id not in ['Zpl31xbBNu7m7dayEoNYmJZImo65YqXTK5x4OYFF', ]:
            message = {'message': 'Invalid client id'}
            return message

        if verify_via == 'google':
            token = request.data['id_token']
            try:    # Code to verify the id token
                idinfo = client.verify_id_token(token, self.CLIENT_ID)

                # Or, if multiple clients access the backend server:
                # idinfo = client.verify_id_token(token, None)
                # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
                #    raise crypt.AppIdentityError("Unrecognized client.")

                if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                    raise crypt.AppIdentityError("Wrong issuer.")

                    # If auth request is from a G Suite domain:
                    # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
                    #    raise crypt.AppIdentityError("Wrong hosted domain.")
            except crypt.AppIdentityError:
                raise crypt.AppIdentityError("Invalid token")  # Invalid token

            user_id = idinfo['sub']
            r = {'message': 'valid', 'user_id': user_id}
            return Response(r)

        elif verify_via == 'facebook':
            token = request.data['access_token']
            app_access_token = request.data['app_access_token']
            user_id = send_get_to_debug_token_fb(token, app_access_token)
            if user_id:
                r = {'message': 'valid', 'user_id': user_id}
            else:
                r = {'message': 'Invalid', 'user_id': user_id}
            return Response(r)

        elif verify_via == 'manually':
            if request.data['signup'] == "True":
                user_id = ''
                r = {'message': 'valid', 'user_id': user_id}
                return Response(r)
            token = request.data['access_token']
            clear_expired()
            access_token = AccessToken.objects.get(token=token)
            if access_token:
                if not access_token.is_expired() and client_id == access_token.application.client_id:
                    user = access_token.user
                    user_id = user.id
                    r = {'message': 'valid', 'user_id': user_id}
                    return Response(r)
                else:
                    r = {'message': 'Token has been expired'}
                    return Response(r)

            else:
                r = {'message': 'Invalid'}
                return  Response(r)



