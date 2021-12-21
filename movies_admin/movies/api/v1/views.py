from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic import DetailView

from movies.models import Filmwork, RoleType


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        genres = ArrayAgg(
            'filmworkgenre__genre__name',
            distinct=True
        )
        actors = ArrayAgg(
            'personrole__person__full_name',
            distinct=True,
            filter=Q(personrole__role=RoleType.ACTOR)
        )
        writers = ArrayAgg(
            'personrole__person__full_name',
            distinct=True,
            filter=Q(personrole__role=RoleType.WRITER)
        )
        directors = ArrayAgg(
            'personrole__person__full_name',
            distinct=True,
            filter=Q(personrole__role=RoleType.DIRECTOR)
        )
        queryset = Filmwork.objects.prefetch_related(
            'FilmworkGenre', 'PersonRole'
            ).values(
            'id', 'title', 'description', 'creation_date', 'rating', 'type'
            ).annotate(
            genres=genres, actors=actors, writers=writers, directors=directors
        )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):

    def get_context_data(self, **kwargs):
        query_list = list(self.get_queryset())
        paginator = self.get_paginator(query_list, 50)

        page_num = self.request.GET.get('page')
        if page_num == 'last':
            page = paginator.get_page(paginator.num_pages)
        else:
            page = paginator.get_page(page_num)

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev':
                page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': page.object_list
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesDetailsApi(MoviesApiMixin, DetailView):

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)['object']
