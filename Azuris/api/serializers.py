from .models import Account, Spell
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)

    #ezek a kitoltendomezok
    class Meta:
        model = Account
        fields = ['email','username','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account

class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk','level','xp','spellA','spellB','spellC']


class SpellPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ['id','type_spell','name','description','power','evasion_rate','level_requirement','cooldown']


class SpellFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ['id','file','position']


