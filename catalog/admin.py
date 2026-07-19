from django.contrib import admin

from .models import Film, Narocnik, Igralec, Racun, Resoljucija, Reziser, Zanr, Jezik, Ogled, Vloga

class PopularnostFilter(admin.SimpleListFilter):
    title = 'Popularity'
    parameter_name = 'popularnost'

    def lookups(self, request, model_admin):
        return [
            ('low', 'Low (0-100)'),
            ('medium', 'Medium (100-500)'),
            ('high', 'High (500-1000)'),
            ('very_high', 'Very High (1000+)'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(popularnost__lt=100)
        if self.value() == 'medium':
            return queryset.filter(popularnost__gte=100, popularnost__lt=500)
        if self.value() == 'high':
            return queryset.filter(popularnost__gte=500, popularnost__lt=1000)
        if self.value() == 'very_high':
            return queryset.filter(popularnost__gte=1000)
        
class OcenaFilter(admin.SimpleListFilter):
    title = 'Rating'
    parameter_name = 'ocena'

    def lookups(self, request, model_admin):
        return [
            ('bad', '★ Below 5'),
            ('ok', '★★ 5-7'),
            ('good', '★★★ 7-8'),
            ('great', '★★★★ 8-9'),
            ('excellent', '★★★★★ 9+'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'bad':
            return queryset.filter(ocena__lt=5)
        if self.value() == 'ok':
            return queryset.filter(ocena__gte=5, ocena__lt=7)
        if self.value() == 'good':
            return queryset.filter(ocena__gte=7, ocena__lt=8)
        if self.value() == 'great':
            return queryset.filter(ocena__gte=8, ocena__lt=9)
        if self.value() == 'excellent':
            return queryset.filter(ocena__gte=9)
        
# ====== KATALOG ======
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id_film', 'naziv', 'datum_izdaje', 'popularnost', 'ocena', 'tmdb_id')
    search_fields = ('naziv', 'opis')
    list_filter = ('datum_izdaje', OcenaFilter, PopularnostFilter)

@admin.register(Zanr)
class ZanrAdmin(admin.ModelAdmin):
    list_display = ('id_zanr', 'naziv', 'opis_zanra')

@admin.register(Igralec)
class IgralecAdmin(admin.ModelAdmin):
    list_display = ('id_igralca', 'ime', 'priimek','tmdb_id', 'datum_rojstva')
    search_fields = ('ime', 'priimek')

@admin.register(Reziser)
class ReziserAdmin(admin.ModelAdmin):
    list_display = ('id_rezisera', 'ime', 'priimek', 'tmdb_id', 'datum_zac_dela', 'datum_rojstva')
    search_fields = ('ime', 'priimek')

@admin.register(Jezik)
class JezikAdmin(admin.ModelAdmin):
    list_display = ('koda_jezika', 'naziv_jezik')

# ====== NAROCNINE ======
@admin.register(Narocnik)
class NarocnikAdmin(admin.ModelAdmin):
    list_display = ('emso', 'ime', 'priimek', 'datum_rojstva', 'e_naslov', 'telefonska_st')
    search_fields = ('ime', 'priimek', 'e_naslov')

@admin.register(Racun)
class RacunAdmin(admin.ModelAdmin):
    list_display = ('id_racuna', 'datum_zac_narocnine', 'emso')
    
@admin.register(Ogled)
class OgledAdmin(admin.ModelAdmin):
    list_display = ('id_ogleda', 'id_racuna', 'id_film', 'cas_ogleda', 'status_ogleda', 'datum_ogleda')
    list_filter = ('status_ogleda','id_film')




"""
@admin.register(Vloga)
class VlogaAdmin(admin.ModelAdmin):
    list_display = ('id_vloga', 'id_igralca', 'id_film', 'vrsta_vloge', 'lik')

@admin.register(Resoljucija)
class ResoljucijaAdmin(admin.ModelAdmin):
    list_display = ('id_resoljucija', 'id_film', 'format')
"""