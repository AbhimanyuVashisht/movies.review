from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
import rest_framework.status as status
from .serializer import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render


@api_view(['GET', 'PUT'])
def reviews(request):
    """
    To Update the Reviews data Model
    API for Reviews to 'GET' and 'POST' 
    To the Database
    :param request: To get the User Request 
    :return Response, status: JSON Return, status corresponding to the request 
    """
    review_db = Reviewers.objects.all()
    if request.method == 'GET':
        serializer = ReviewersSerializer(review_db, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = ReviewersSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            serializer = ReviewersSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def review_update(request, uuid):
    """
    To Update the Review Model
    API for Reviews to 'GET', 'PATCH' and 'DELETE' 
    To the Database
    To Get Movies by ID
    Setting the generic_type = 'MV'
    :param request: To get the User Request
    :param uuid: Primary key value for Model Movies (represent movie ID)
    :return Response, status: JSON Return, status corresponding to the request
    """
    try:
        review_db = Reviewers.objects.get(reviewer_id=uuid)
        # need to check permission with some other better way : movies.can_be_viewed()
        if False:
            raise review_db.DoesNotExist
    except Reviewers.DoesNotExist:
        return Response({'details': 'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewersSerializer(review_db)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = ReviewersSerializer(review_db, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        review_db.is_deleted = True
        review_db.save()
        return Response(ReviewersSerializer(review_db).data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def movie_reviews(request):
    """
    To Update the MovieReviews data Model
    API for MovieReviews to 'GET' and 'POST' 
    To the Database
    :param request: To get the User Request 
    :return Response, status: JSON Return, status corresponding to the request 
    """
    review_db = MovieReviews.objects.all()
    if request.method == 'GET':
        serializer = MovieReviewsSerializer(review_db, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = MovieReviewsSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            serializer = MovieReviewsSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def movie_reviews_name(request, mov_name):
    """
    To Search the Movie by Name
    API for MoviesReviews to 'GET', 'PATCH' and 'DELETE' 
    To the Database
    To Get Movies by ID
    Setting the generic_type = 'MV'
    :param mov_name: The Name of the movie to be searched
    :param request: To get the User Request
    :return Response, status: JSON Return, status corresponding to the request 
    """
    try:
        mr_db = MovieReviews.objects.filter(movies__title__icontains=mov_name)
        if False:
            raise mr_db.DoesNotExist
    except MovieReviews.DoesNotExist:
        return Response({'details': 'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieReviewsSerializer(mr_db)
        # filter_fields = ('star_rate_movie', 'fk_reviewer_id__review', 'fk_id__title',)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = MovieReviewsSerializer(mr_db, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        mr_db.is_deleted = True
        mr_db.save()
        return Response(MovieReviewsSerializer(mr_db).data, status=status.HTTP_200_OK)


