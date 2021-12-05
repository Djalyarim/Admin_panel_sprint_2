from django.contrib import admin

from .models import Filmwork, FilmworkGenre, Person, PersonRole, Genre


class GenreInline(admin.TabularInline):
    model = FilmworkGenre
    extra = 0
    verbose_name = 'Жанр'
    autocomplete_fields = ('genre',)


class PersonRoleInline(admin.TabularInline):
    model = PersonRole
    extra = 0
    verbose_name = 'Роль'
    autocomplete_fields = ('person',)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    search_fields = ('id', 'title', 'description')
    list_display = ('title', 'type', 'creation_date', 'rating')
    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating'
    )
    empty_value_display = '-пусто-'
    inlines = [
        GenreInline,
        PersonRoleInline,
    ]
    ordering = ('title',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'birth_date', 'id')
    list_display = (
        'full_name', 'birth_date', 'created_at', 'updated_at'
    )
    empty_value_display = '-пусто-'
    ordering = ('full_name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'name', 'description', 'created_at', 'updated_at'
    )
    empty_value_display = '-пусто-'
    ordering = ('name',)
