# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from accounts.models import Account
from accounts.serializers import AccountSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AccountsList(APIView):
    """
    List all accounts, or create a new account.
    """
    def get(self, request, format=None):
        accounts = Account.objects.all()
        serializer = AccountSerializers(accounts, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AccountSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializers(account)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializers(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)