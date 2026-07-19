# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Reziser(models.Model):
    id_rezisera = models.SmallAutoField(primary_key=True)
    ime = models.CharField(max_length=20, verbose_name='First Name')
    priimek = models.CharField(max_length=20, verbose_name='Last Name')
    datum_zac_dela = models.DateField(blank=True, null=True, verbose_name='Career Start Date')
    biografija = models.TextField(unique=True, verbose_name='Biography')
    nagrade = models.TextField(unique=True, blank=True, null=True, verbose_name='Awards')
    foto_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Photo URL')
    datum_rojstva = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    rojstni_kraj = models.CharField(max_length=50, blank=True, null=True, verbose_name='Place of Birth')
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name='TMDB ID')

    def __str__(self):
        return f"{self.ime} {self.priimek}"

    class Meta:
        managed = False
        db_table = 'reziser'
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'


class Film(models.Model):
    id_film = models.SmallAutoField(primary_key=True)
    naziv = models.CharField(unique=True, max_length=100, verbose_name='Title')
    opis = models.TextField(unique=True, verbose_name='Description')
    id_rezisera = models.ForeignKey(Reziser, models.DO_NOTHING, db_column='id_rezisera', verbose_name='Director')
    datum_izdaje = models.DateField(verbose_name='Release Date')
    poster_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Poster URL')
    youtube_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='YouTube Trailer ID')
    ocena = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, verbose_name='Rating')
    trajanje = models.SmallIntegerField(blank=True, null=True, verbose_name='Duration (min)')
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name='TMDB ID')
    popularnost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Popularity')
    posodobljeno = models.DateTimeField(blank=True, null=True, verbose_name='Last Updated')
    iskanje = models.TextField(blank=True, null=True, verbose_name='Search Index')

    def __str__(self):
        return self.naziv

    class Meta:
        managed = False
        db_table = 'film'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Igralec(models.Model):
    id_igralca = models.SmallAutoField(primary_key=True)
    ime = models.CharField(max_length=20, verbose_name='First Name')
    priimek = models.CharField(max_length=20, verbose_name='Last Name')
    datum_rojstva = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    biografija = models.TextField(unique=True, verbose_name='Biography')
    nagrade = models.TextField(unique=True, blank=True, null=True, verbose_name='Awards')
    foto_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Photo URL')
    rojstni_kraj = models.CharField(max_length=50, blank=True, null=True, verbose_name='Place of Birth')
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name='TMDB ID')

    def __str__(self):
        return f"{self.ime} {self.priimek}"

    class Meta:
        managed = False
        db_table = 'igralec'
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'


class Jezik(models.Model):
    koda_jezika = models.CharField(primary_key=True, max_length=3, verbose_name='Language Code')
    naziv_jezik = models.CharField(unique=True, max_length=20, blank=True, null=True, verbose_name='Language Name')

    def __str__(self):
        return self.naziv_jezik or self.koda_jezika

    class Meta:
        managed = False
        db_table = 'jezik'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Zanr(models.Model):
    id_zanr = models.SmallAutoField(primary_key=True)
    naziv = models.CharField(unique=True, max_length=20, verbose_name='Genre Name')
    opis_zanra = models.TextField(unique=True, verbose_name='Description')

    def __str__(self):
        return self.naziv

    class Meta:
        managed = False
        db_table = 'zanr'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class FilmJezik(models.Model):
    pk = models.CompositePrimaryKey('id_film', 'koda_jezika')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film', verbose_name='Movie')
    koda_jezika = models.ForeignKey(Jezik, models.DO_NOTHING, db_column='koda_jezika', verbose_name='Language')

    class Meta:
        managed = False
        db_table = 'film_jezik'
        verbose_name = 'Movie Language'
        verbose_name_plural = 'Movie Languages'


class ZanrFilm(models.Model):
    pk = models.CompositePrimaryKey('id_film', 'id_zanr')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film', verbose_name='Movie')
    id_zanr = models.ForeignKey(Zanr, models.DO_NOTHING, db_column='id_zanr', verbose_name='Genre')

    class Meta:
        managed = False
        db_table = 'zanr_film'
        verbose_name = 'Movie Genre'
        verbose_name_plural = 'Movie Genres'


class Vloga(models.Model):
    id_vloga = models.SmallAutoField(primary_key=True)
    id_igralca = models.ForeignKey(Igralec, models.DO_NOTHING, db_column='id_igralca', verbose_name='Actor')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film', verbose_name='Movie')
    vrsta_vloge = models.TextField(verbose_name='Role Type')
    lik = models.CharField(unique=True, max_length=20, verbose_name='Character')

    def __str__(self):
        return f"{self.id_igralca} as {self.lik}"

    class Meta:
        managed = False
        db_table = 'vloga'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class Resoljucija(models.Model):
    id_resoljucija = models.SmallAutoField(primary_key=True)
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film', verbose_name='Movie')
    format = models.TextField(blank=True, null=True, verbose_name='Resolution')

    def __str__(self):
        return f"{self.id_film} - {self.format}p"

    class Meta:
        managed = False
        db_table = 'resoljucija'
        verbose_name = 'Resolution'
        verbose_name_plural = 'Resolutions'


class Narocnik(models.Model):
    emso = models.BigIntegerField(primary_key=True, verbose_name='ID Number')
    ime = models.CharField(max_length=20, verbose_name='First Name')
    priimek = models.CharField(max_length=20, verbose_name='Last Name')
    datum_rojstva = models.DateField(verbose_name='Date of Birth')
    e_naslov = models.CharField(unique=True, max_length=60, verbose_name='Email')
    telefonska_st = models.CharField(unique=True, max_length=9, verbose_name='Phone Number')

    def __str__(self):
        return f"{self.ime} {self.priimek}"

    class Meta:
        managed = False
        db_table = 'narocnik'
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'


class Racun(models.Model):
    id_racuna = models.SmallAutoField(primary_key=True)
    datum_zac_narocnine = models.DateField(verbose_name='Subscription Start Date')
    emso = models.ForeignKey(Narocnik, models.DO_NOTHING, db_column='emso', blank=True, null=True, verbose_name='Subscriber')

    def __str__(self):
        return f"Account #{self.id_racuna}"

    class Meta:
        managed = False
        db_table = 'racun'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class Ogled(models.Model):
    id_ogleda = models.SmallIntegerField(primary_key=True)
    id_racuna = models.ForeignKey(Racun, models.DO_NOTHING, db_column='id_racuna', verbose_name='Account')
    cas_ogleda = models.TimeField(verbose_name='Watch Time')
    status_ogleda = models.TextField(verbose_name='Watch Status')
    id_film = models.SmallIntegerField(verbose_name='Movie ID')
    datum_ogleda = models.DateField(blank=True, null=True, verbose_name='Watch Date')

    def __str__(self):
        return f"View #{self.id_ogleda}"

    class Meta:
        managed = False
        db_table = 'ogled'
        verbose_name = 'View'
        verbose_name_plural = 'Views'