# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airq(models.Model):
    matter = models.TextField(blank=True, null=True)
    geo_place = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    value_type = models.TextField(blank=True, null=True)
    latitude_ne = models.FloatField(blank=True, null=True)
    latitude_sw = models.FloatField(blank=True, null=True)
    longitude_ne = models.FloatField(blank=True, null=True)
    longitude_sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airq'


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


class Energy(models.Model):
    lng = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy'


class Greeninfra(models.Model):
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'greeninfra'


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


class Temp(models.Model):
    x1 = models.TextField(blank=True, null=True)
    x2 = models.TextField(blank=True, null=True)
    x3 = models.TextField(blank=True, null=True)
    x4 = models.TextField(blank=True, null=True)
    x5 = models.TextField(blank=True, null=True)
    x6 = models.TextField(blank=True, null=True)
    x7 = models.TextField(blank=True, null=True)
    x8 = models.TextField(blank=True, null=True)
    x9 = models.TextField(blank=True, null=True)
    x10 = models.TextField(blank=True, null=True)
    x11 = models.TextField(blank=True, null=True)
    x12 = models.TextField(blank=True, null=True)
    x13 = models.TextField(blank=True, null=True)
    x14 = models.TextField(blank=True, null=True)
    x15 = models.TextField(blank=True, null=True)
    x16 = models.TextField(blank=True, null=True)
    x17 = models.TextField(blank=True, null=True)
    x18 = models.TextField(blank=True, null=True)
    x19 = models.TextField(blank=True, null=True)
    x20 = models.TextField(blank=True, null=True)
    x21 = models.TextField(blank=True, null=True)
    x22 = models.TextField(blank=True, null=True)
    x23 = models.TextField(blank=True, null=True)
    x24 = models.TextField(blank=True, null=True)
    x25 = models.TextField(blank=True, null=True)
    x26 = models.TextField(blank=True, null=True)
    x27 = models.TextField(blank=True, null=True)
    x28 = models.TextField(blank=True, null=True)
    x29 = models.TextField(blank=True, null=True)
    x30 = models.TextField(blank=True, null=True)
    x31 = models.TextField(blank=True, null=True)
    x32 = models.TextField(blank=True, null=True)
    x33 = models.TextField(blank=True, null=True)
    x34 = models.TextField(blank=True, null=True)
    x35 = models.TextField(blank=True, null=True)
    x36 = models.TextField(blank=True, null=True)
    x37 = models.TextField(blank=True, null=True)
    x38 = models.TextField(blank=True, null=True)
    x39 = models.TextField(blank=True, null=True)
    x40 = models.TextField(blank=True, null=True)
    x41 = models.TextField(blank=True, null=True)
    x42 = models.TextField(blank=True, null=True)
    x43 = models.TextField(blank=True, null=True)
    x44 = models.TextField(blank=True, null=True)
    x45 = models.TextField(blank=True, null=True)
    x46 = models.TextField(blank=True, null=True)
    x47 = models.TextField(blank=True, null=True)
    x48 = models.TextField(blank=True, null=True)
    x49 = models.TextField(blank=True, null=True)
    x50 = models.TextField(blank=True, null=True)
    x51 = models.TextField(blank=True, null=True)
    x52 = models.TextField(blank=True, null=True)
    x53 = models.TextField(blank=True, null=True)
    x54 = models.TextField(blank=True, null=True)
    x55 = models.TextField(blank=True, null=True)
    x56 = models.TextField(blank=True, null=True)
    x57 = models.TextField(blank=True, null=True)
    x58 = models.TextField(blank=True, null=True)
    x59 = models.TextField(blank=True, null=True)
    x60 = models.TextField(blank=True, null=True)
    x61 = models.TextField(blank=True, null=True)
    x62 = models.TextField(blank=True, null=True)
    x63 = models.TextField(blank=True, null=True)
    x64 = models.TextField(blank=True, null=True)
    x65 = models.TextField(blank=True, null=True)
    x66 = models.TextField(blank=True, null=True)
    x67 = models.TextField(blank=True, null=True)
    x68 = models.TextField(blank=True, null=True)
    x69 = models.TextField(blank=True, null=True)
    x70 = models.TextField(blank=True, null=True)
    x71 = models.TextField(blank=True, null=True)
    x72 = models.TextField(blank=True, null=True)
    x73 = models.TextField(blank=True, null=True)
    x74 = models.TextField(blank=True, null=True)
    x75 = models.TextField(blank=True, null=True)
    x76 = models.TextField(blank=True, null=True)
    x77 = models.TextField(blank=True, null=True)
    x78 = models.TextField(blank=True, null=True)
    x79 = models.TextField(blank=True, null=True)
    x80 = models.TextField(blank=True, null=True)
    x81 = models.TextField(blank=True, null=True)
    x82 = models.TextField(blank=True, null=True)
    x83 = models.TextField(blank=True, null=True)
    x84 = models.TextField(blank=True, null=True)
    x85 = models.TextField(blank=True, null=True)
    x86 = models.TextField(blank=True, null=True)
    x87 = models.TextField(blank=True, null=True)
    x88 = models.TextField(blank=True, null=True)
    x89 = models.TextField(blank=True, null=True)
    x90 = models.TextField(blank=True, null=True)
    x91 = models.TextField(blank=True, null=True)
    x92 = models.TextField(blank=True, null=True)
    x93 = models.TextField(blank=True, null=True)
    x94 = models.TextField(blank=True, null=True)
    x95 = models.TextField(blank=True, null=True)
    x96 = models.TextField(blank=True, null=True)
    x97 = models.TextField(blank=True, null=True)
    x98 = models.TextField(blank=True, null=True)
    x99 = models.TextField(blank=True, null=True)
    x100 = models.TextField(blank=True, null=True)
    x101 = models.TextField(blank=True, null=True)
    x102 = models.TextField(blank=True, null=True)
    x103 = models.TextField(blank=True, null=True)
    x104 = models.TextField(blank=True, null=True)
    x105 = models.TextField(blank=True, null=True)
    x106 = models.TextField(blank=True, null=True)
    x107 = models.TextField(blank=True, null=True)
    x108 = models.TextField(blank=True, null=True)
    x109 = models.TextField(blank=True, null=True)
    x110 = models.TextField(blank=True, null=True)
    x111 = models.TextField(blank=True, null=True)
    x112 = models.TextField(blank=True, null=True)
    x113 = models.TextField(blank=True, null=True)
    x114 = models.TextField(blank=True, null=True)
    x115 = models.TextField(blank=True, null=True)
    x116 = models.TextField(blank=True, null=True)
    x117 = models.TextField(blank=True, null=True)
    x118 = models.TextField(blank=True, null=True)
    x119 = models.TextField(blank=True, null=True)
    x120 = models.TextField(blank=True, null=True)
    x121 = models.TextField(blank=True, null=True)
    x122 = models.TextField(blank=True, null=True)
    x123 = models.TextField(blank=True, null=True)
    x124 = models.TextField(blank=True, null=True)
    x125 = models.TextField(blank=True, null=True)
    x126 = models.TextField(blank=True, null=True)
    x127 = models.TextField(blank=True, null=True)
    x128 = models.TextField(blank=True, null=True)
    x129 = models.TextField(blank=True, null=True)
    x130 = models.TextField(blank=True, null=True)
    x131 = models.TextField(blank=True, null=True)
    x132 = models.TextField(blank=True, null=True)
    x133 = models.TextField(blank=True, null=True)
    x134 = models.TextField(blank=True, null=True)
    x135 = models.TextField(blank=True, null=True)
    x136 = models.TextField(blank=True, null=True)
    x137 = models.TextField(blank=True, null=True)
    x138 = models.TextField(blank=True, null=True)
    x139 = models.TextField(blank=True, null=True)
    x140 = models.TextField(blank=True, null=True)
    x141 = models.TextField(blank=True, null=True)
    x142 = models.TextField(blank=True, null=True)
    x143 = models.TextField(blank=True, null=True)
    x144 = models.TextField(blank=True, null=True)
    x145 = models.TextField(blank=True, null=True)
    x146 = models.TextField(blank=True, null=True)
    x147 = models.TextField(blank=True, null=True)
    x148 = models.TextField(blank=True, null=True)
    x149 = models.TextField(blank=True, null=True)
    x150 = models.TextField(blank=True, null=True)
    x151 = models.TextField(blank=True, null=True)
    x152 = models.TextField(blank=True, null=True)
    x153 = models.TextField(blank=True, null=True)
    x154 = models.TextField(blank=True, null=True)
    x155 = models.TextField(blank=True, null=True)
    x156 = models.TextField(blank=True, null=True)
    x157 = models.TextField(blank=True, null=True)
    x158 = models.TextField(blank=True, null=True)
    x159 = models.TextField(blank=True, null=True)
    x160 = models.TextField(blank=True, null=True)
    x161 = models.TextField(blank=True, null=True)
    x162 = models.TextField(blank=True, null=True)
    x163 = models.TextField(blank=True, null=True)
    x164 = models.TextField(blank=True, null=True)
    x165 = models.TextField(blank=True, null=True)
    x166 = models.TextField(blank=True, null=True)
    x167 = models.TextField(blank=True, null=True)
    x168 = models.TextField(blank=True, null=True)
    x169 = models.TextField(blank=True, null=True)
    x170 = models.TextField(blank=True, null=True)
    x171 = models.TextField(blank=True, null=True)
    x172 = models.TextField(blank=True, null=True)
    x173 = models.TextField(blank=True, null=True)
    x174 = models.TextField(blank=True, null=True)
    x175 = models.TextField(blank=True, null=True)
    x176 = models.TextField(blank=True, null=True)
    x177 = models.TextField(blank=True, null=True)
    x178 = models.TextField(blank=True, null=True)
    x179 = models.TextField(blank=True, null=True)
    x180 = models.TextField(blank=True, null=True)
    x181 = models.TextField(blank=True, null=True)
    x182 = models.TextField(blank=True, null=True)
    x183 = models.TextField(blank=True, null=True)
    x184 = models.TextField(blank=True, null=True)
    x185 = models.TextField(blank=True, null=True)
    x186 = models.TextField(blank=True, null=True)
    x187 = models.TextField(blank=True, null=True)
    x188 = models.TextField(blank=True, null=True)
    x189 = models.TextField(blank=True, null=True)
    x190 = models.TextField(blank=True, null=True)
    x191 = models.TextField(blank=True, null=True)
    x192 = models.TextField(blank=True, null=True)
    x193 = models.TextField(blank=True, null=True)
    x194 = models.TextField(blank=True, null=True)
    x195 = models.TextField(blank=True, null=True)
    x196 = models.TextField(blank=True, null=True)
    x197 = models.TextField(blank=True, null=True)
    x198 = models.TextField(blank=True, null=True)
    x199 = models.TextField(blank=True, null=True)
    x200 = models.TextField(blank=True, null=True)
    x201 = models.TextField(blank=True, null=True)
    x202 = models.TextField(blank=True, null=True)
    x203 = models.TextField(blank=True, null=True)
    x204 = models.TextField(blank=True, null=True)
    x205 = models.TextField(blank=True, null=True)
    x206 = models.TextField(blank=True, null=True)
    x207 = models.TextField(blank=True, null=True)
    x208 = models.TextField(blank=True, null=True)
    x209 = models.TextField(blank=True, null=True)
    x210 = models.TextField(blank=True, null=True)
    x211 = models.TextField(blank=True, null=True)
    x212 = models.TextField(blank=True, null=True)
    x213 = models.TextField(blank=True, null=True)
    x214 = models.TextField(blank=True, null=True)
    x215 = models.TextField(blank=True, null=True)
    x216 = models.TextField(blank=True, null=True)
    x217 = models.TextField(blank=True, null=True)
    x218 = models.TextField(blank=True, null=True)
    x219 = models.TextField(blank=True, null=True)
    x220 = models.TextField(blank=True, null=True)
    x221 = models.TextField(blank=True, null=True)
    x222 = models.TextField(blank=True, null=True)
    x223 = models.TextField(blank=True, null=True)
    x224 = models.TextField(blank=True, null=True)
    x225 = models.TextField(blank=True, null=True)
    x226 = models.TextField(blank=True, null=True)
    x227 = models.TextField(blank=True, null=True)
    x228 = models.TextField(blank=True, null=True)
    x229 = models.TextField(blank=True, null=True)
    x230 = models.TextField(blank=True, null=True)
    x231 = models.TextField(blank=True, null=True)
    x232 = models.TextField(blank=True, null=True)
    x233 = models.TextField(blank=True, null=True)
    x234 = models.TextField(blank=True, null=True)
    x235 = models.TextField(blank=True, null=True)
    x236 = models.TextField(blank=True, null=True)
    x237 = models.TextField(blank=True, null=True)
    x238 = models.TextField(blank=True, null=True)
    x239 = models.TextField(blank=True, null=True)
    x240 = models.TextField(blank=True, null=True)
    x241 = models.TextField(blank=True, null=True)
    x242 = models.TextField(blank=True, null=True)
    x243 = models.TextField(blank=True, null=True)
    x244 = models.TextField(blank=True, null=True)
    x245 = models.TextField(blank=True, null=True)
    x246 = models.TextField(blank=True, null=True)
    x247 = models.TextField(blank=True, null=True)
    x248 = models.TextField(blank=True, null=True)
    x249 = models.TextField(blank=True, null=True)
    x250 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'
