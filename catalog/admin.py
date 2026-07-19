from django.contrib import admin

from .models import Film, Narocnik, Igralec, Racun, Resoljucija, Reziser, Zanr, Jezik, Ogled, Vloga

admin.site.register(Film)
admin.site.register(Zanr)
admin.site.register(Narocnik)
admin.site.register(Ogled)
admin.site.register(Igralec)
admin.site.register(Vloga)
admin.site.register(Racun)
admin.site.register(Resoljucija)
admin.site.register(Reziser)
admin.site.register(Jezik)
