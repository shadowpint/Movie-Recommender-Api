from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from rest_framework import status

from users.models import Profile
from .serializers import  UserSerializer
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import make_password
from oauth2.token_verify import verify_token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from oauth2.Activation_Token_Generator import account_activation_token
from django.core.mail import EmailMessage


class Detail(APIView):
    def get(self, request, user_id):
        """
        To get the user information whose user_id specified in Url
        request type allowed : only GET
        
        :param request: 
        :param user_id: 
        :return: json object of either user info. or error message
        """
        data = request.GET.copy()
        data['signup'] = False
        r = verify_token(data)
        if r['message'] != 'valid':
            return Response({'message': r['message']})

        if user_id == r['user_id']:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'message': 'Access token not for the given User'})
                

'''
def web_signin(request):
    return render(request, 'users/google_signin.html', dict())
'''


class SignUp(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        """
        To sign up the user manually
        request type allowed : only POST
        
        :param request: 
        :return: either success message or user info if user already signed up
        """
        data = request.data.copy()
        print data
        data['signup'] = True
        r = verify_token(data)
        if r['message'] != 'valid':
            return Response({'message': r['message']})
        print r
        user_id = r.get('username')
        print user_id
        user = User()          # insert user info into database
        try:
            user = User.objects.get(username=user_id)

            serializer = UserSerializer(user)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            user.username = data['username']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']

            password = data['password']

            user.password = make_password(password=password, salt=None, hasher='unsalted_md5')

            user.save()
            #
            # # To send confirmation email
            # current_site = get_current_site(request)
            # subject = 'Activate your  account.'
            # message = render_to_string('users/acc_active_email.html', {
            #     'user': user, 'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # toemail = data['email']
            # email = EmailMessage(subject, message, to=[toemail])
            # email.send()
            return Response({'message': 'User successfully registered'})


class SignIn(APIView):

    def post(self, request):
        """
        To sign in a user.
        
        :param request: 
        :return: json object which contains user information
        """
        data = request.data.copy()
        data['signup'] = False
        r = verify_token(data)
        if r['message'] != 'valid':
            return Response({'message': r['message']})
        user_id = r['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)


class ProfileUpdate(APIView):
    def post(self, request):
        """
        To update profile info. of the user.
        
        :param request: 
        :return: Success or Failure message
        """
        data = request.data.copy()
        data['signup'] = False
        r = verify_token(data)
        if r['message'] != 'valid':
            return Response({'message': r['message']})
        user_id = r['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            if 'first_name' in data:
                user.first_name = data['first_name']
            if 'last_name' in data:
                user.last_name = data['last_name']
            if 'gender' in data:
                user.gender = data['gender']
            if 'email' in data:
                if not user.email:
                    user.email = data['email']
            if 'contact' in data:
                user.contact = data['contact']
            if 'pic_url' in data:
                user.pic_url = data['pic_url']
            if 'height' in data:
                user.height = data['height']
            if 'weight' in data:
                user.weight = data['weight']
            if 'dob' in data:
                user.dob = data['dob']                
            user.save()
            return Response({'message': 'Profile successfully updated'})


def activate(request,uidb64,token):
    """
    To activate the user account after email confirmation
    
    :param request: 
    :param uidb64: 
    :param token: 
    :return: Success or Failure message
    """
    try:

        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print user
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
       
    if user is not None and account_activation_token.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Your email is already confirmed. Thank You!')      
    else:
        return HttpResponse('Activation link is invalid! :(')      