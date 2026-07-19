# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Film(models.Model):
    id_film = models.SmallAutoField(primary_key=True)
    naziv = models.CharField(unique=True, max_length=100)
    opis = models.TextField(unique=True)
    id_rezisera = models.ForeignKey('Reziser', models.DO_NOTHING, db_column='id_rezisera')
    datum_izdaje = models.DateField()
    poster_url = models.CharField(max_length=200, blank=True, null=True)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    ocena = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    trajanje = models.SmallIntegerField(blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True)
    popularnost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    posodobljeno = models.DateTimeField(blank=True, null=True)
    iskanje = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film'


class FilmJezik(models.Model):
    pk = models.CompositePrimaryKey('id_film', 'koda_jezika')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')
    koda_jezika = models.ForeignKey('Jezik', models.DO_NOTHING, db_column='koda_jezika')

    class Meta:
        managed = False
        db_table = 'film_jezik'


class Igralec(models.Model):
    id_igralca = models.SmallAutoField(primary_key=True)
    ime = models.CharField(max_length=20)
    priimek = models.CharField(max_length=20)
    datum_rojstva = models.DateField(blank=True, null=True)
    biografija = models.TextField(unique=True)
    nagrade = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    foto_url = models.CharField(max_length=200, blank=True, null=True)
    rojstni_kraj = models.CharField(max_length=50, blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'igralec'


class Jezik(models.Model):
    koda_jezika = models.CharField(primary_key=True, max_length=3)
    naziv_jezik = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jezik'


class Narocnik(models.Model):
    emso = models.BigIntegerField(primary_key=True)
    ime = models.CharField(max_length=20)
    priimek = models.CharField(max_length=20)
    datum_rojstva = models.DateField()
    e_naslov = models.CharField(unique=True, max_length=60)
    telefonska_st = models.CharField(unique=True, max_length=9)

    class Meta:
        managed = False
        db_table = 'narocnik'


class Ogled(models.Model):
    id_ogleda = models.SmallIntegerField(primary_key=True)
    id_racuna = models.ForeignKey('Racun', models.DO_NOTHING, db_column='id_racuna')
    cas_ogleda = models.TimeField()
    status_ogleda = models.TextField()  # This field type is a guess.
    id_film = models.SmallIntegerField()
    datum_ogleda = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ogled'


class Racun(models.Model):
    id_racuna = models.SmallAutoField(primary_key=True)
    datum_zac_narocnine = models.DateField()
    emso = models.ForeignKey(Narocnik, models.DO_NOTHING, db_column='emso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'racun'


class Resoljucija(models.Model):
    id_resoljucija = models.SmallAutoField(primary_key=True)
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')
    format = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'resoljucija'


class Reziser(models.Model):
    id_rezisera = models.SmallAutoField(primary_key=True)
    ime = models.CharField(max_length=20)
    priimek = models.CharField(max_length=20)
    datum_zac_dela = models.DateField(blank=True, null=True)
    biografija = models.TextField(unique=True)
    nagrade = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    foto_url = models.CharField(max_length=200, blank=True, null=True)
    datum_rojstva = models.DateField(blank=True, null=True)
    rojstni_kraj = models.CharField(max_length=50, blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reziser'


class Vloga(models.Model):
    id_vloga = models.SmallAutoField(primary_key=True)
    id_igralca = models.ForeignKey(Igralec, models.DO_NOTHING, db_column='id_igralca')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')
    vrsta_vloge = models.TextField()  # This field type is a guess.
    lik = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'vloga'


class Zanr(models.Model):
    id_zanr = models.SmallAutoField(primary_key=True)
    naziv = models.CharField(unique=True, max_length=20)
    opis_zanra = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'zanr'


class ZanrFilm(models.Model):
    pk = models.CompositePrimaryKey('id_film', 'id_zanr')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')
    id_zanr = models.ForeignKey(Zanr, models.DO_NOTHING, db_column='id_zanr')

    class Meta:
        managed = False
        db_table = 'zanr_film'
