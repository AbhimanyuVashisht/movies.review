# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import rest_framework.status as status
from movies.models import Movies
# from rest_framework.authentication import SessionAuthentication, BaseAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.throttling import UserRateThrottle
# from ..notification.helpers import notify
# from django.shortcuts import render
from .serializer import *
# from movies.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Reverse function is used to return fully qualified URLs(to determine the host and port)
        'users': reverse('user-list', request=request, format=format),
        'movies': reverse('movies-list', request=request, format=format)
    })


@api_view(['GET', 'POST'])
def movies(request):
    """
    API for movies to 'GET' and 'POST' 
    To the Database
    :param request: To get the User Request 
    :return Response, status: JSON Return, status corresponding to the request 
    """
    movies_db = Movies.objects.all()
    if request.method == 'GET':
        serializer = MoviesSerializer(movies_db, many=True)
        # pagination_class = LargeResultsSetPagination
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            movies = serializer.save()
            serializer = MoviesSerializer(movies)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def movies_by_name(request, uuid):
    """
    API for movies to 'GET', 'PATCH' and 'DELETE' 
    To the Database
    To Get Movies by ID
    Setting the generic_type = 'MV'
    :param uuid:
    :param request: To get the User Request
    :return Response, status: JSON Return, status corresponding to the request
    """
    try:
        movies_db = Movies.objects.filter(title__search=uuid, generic_type='MV')
        # need to check permission  with some other better way : movies.can_be_viewed()
        if False:
            raise movies_db.DoesNotExist
    except Movies.DoesNotExist:
        return Response({'details': 'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MoviesSerializer(movies_db)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = MoviesSerializer(movies_db, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movies.is_deleted = True
        movies.save()
        return Response(MoviesSerializer(movies).data, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def tvshows_by_id(request, uuid):
    """
    API for movies to 'GET', 'PATCH' and 'DELETE' 
    To the Database
    To Get TVshows by ID
    Setting the generic_type = 'MV'
    :param request: To get the User Request
    :param uuid: Primary key value for Model Movies (represent movie ID)
    :return Response, status: JSON Return, status corresponding to the request
    """
    try:
        tvshows_db = Movies.objects.get(uuid=uuid, generic_type='TV')
        # need to check permission with some other better way : movies.can_be_viewed()
        if False:
            raise tvshows_db.DoesNotExist
    except Movies.DoesNotExist:
        return Response({'details': 'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MoviesSerializer(tvshows_db)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = MoviesSerializer(tvshows_db, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        tvshows_db.is_deleted = True
        tvshows_db.save()
        return Response(MoviesSerializer(tvshows_db).data, status=status.HTTP_200_OK)
