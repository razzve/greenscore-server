from django.db import models


#air quality table
class Airq(models.Model):
    matter = models.TextField(blank=True, null=True)
    geo_place = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    value_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airq'

#green infrastructure table
class Greeninfra(models.Model):
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'greeninfra'



#authentication skeleton for django
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


#django db utils
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


#temporary
class T(models.Model):
    x1 = models.TextField(blank=True, null=True)
    x2 = models.IntegerField(blank=True, null=True)
    x3 = models.TextField(blank=True, null=True)
    x4 = models.TextField(blank=True, null=True)
    x5 = models.TextField(blank=True, null=True)
    x6 = models.TextField(blank=True, null=True)
    x7 = models.TextField(blank=True, null=True)
    x8 = models.TextField(blank=True, null=True)
    x9 = models.TextField(blank=True, null=True)
    x10 = models.TextField(blank=True, null=True)
    x11 = models.FloatField(blank=True, null=True)
    x12 = models.FloatField(blank=True, null=True)
    x13 = models.TextField(blank=True, null=True)
    x14 = models.TextField(blank=True, null=True)
    x15 = models.TextField(blank=True, null=True)
    x16 = models.TextField(blank=True, null=True)
    x17 = models.TextField(blank=True, null=True)
    x18 = models.TextField(blank=True, null=True)
    x19 = models.TextField(blank=True, null=True)
    x20 = models.TextField(blank=True, null=True)
    x21 = models.IntegerField(blank=True, null=True)
    x22 = models.IntegerField(blank=True, null=True)
    x23 = models.TextField(blank=True, null=True)
    x24 = models.FloatField(blank=True, null=True)
    x25 = models.FloatField(blank=True, null=True)
    x26 = models.FloatField(blank=True, null=True)
    x27 = models.TextField(blank=True, null=True)
    x28 = models.TextField(blank=True, null=True)
    x29 = models.TextField(blank=True, null=True)
    x30 = models.TextField(blank=True, null=True)
    x31 = models.TextField(blank=True, null=True)
    x32 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't'