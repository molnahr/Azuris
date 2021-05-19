from contextvars import Token

from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Account, Spell
from .serializers import RegistrationSerializer, AccountPropertiesSerializer, SpellPropertiesSerializer, \
    SpellFileSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# LIST OF SPELLS
@permission_classes([])
@authentication_classes([])
class SpellViewSet(APIView):
    def get(self, request):
        spell = Spell.objects.all()
        spell_serializer = SpellPropertiesSerializer(spell, many=True)
        return Response(spell_serializer.data)


# ONE SPELL
@permission_classes([])
@authentication_classes([])
class SpellDetailsViewSet(APIView):
    def get(self,request,id):
        try:
            spell = Spell.objects.get(id=id)
        except Spell.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        spell_serializer = SpellFileSerializer(spell)
        return Response(spell_serializer.data)



# REGISTRATION
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0')
        if validate_email(email) != None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        username = request.data.get('username', '0')
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data)

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['pk'] = account.pk
            token = Token.objects.get(user=account).key
            data['token'] = token
            data['xp'] = account.xp
            data['level'] = account.level

        else:
            data = serializer.errors
        return Response(data)


def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email


def validate_username(username):
    account = None
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username




@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)

@api_view(['PATCH',])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = AccountPropertiesSerializer(account,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Update success"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#LOGIN
class ObtainAuthTokenView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}

        email = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['token'] = token.key
            context['level'] = account.level
            context['xp'] = account.xp
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'

        return Response(context)