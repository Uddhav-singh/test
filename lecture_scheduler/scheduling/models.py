from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group, AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext as _

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='instructor_user_set',  # You can choose any related name you prefer
        verbose_name=_('user permissions'),
        help_text=_('Specific permissions for this instructor.'),
    )

    # Define a related_name for groups
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='instructor_set',  # You can choose any related name you prefer
        verbose_name=_('groups'),
        help_text=_('The groups this instructor belongs to. A user will get all permissions granted to each of their groups.'),
    )

class Course(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=200, default='Lecture name')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return self.name


# scheduling/models.py creating admin/instructor and user

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class  MyAccountManager(BaseUserManager):
#creating a user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('user must have an email address')

        if not username:
            raise ValueError('user must have an username address')

        user = self.model(
        email = self.normalize_email(email),
        username = username,
        first_name = first_name,
        last_name = last_name,
        )

        user.set_password(password)
        user.save(using = self.db)
        return user
#creating super user
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
        email = self.normalize_email(email),
        username = username,
        password =password,
        first_name = first_name,
        last_name = last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length =100, unique = True)
    email  = models.EmailField(max_length = 100, unique = True)
    phone_number = models.CharField(max_length = 20)

    #required
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now_add = True)

    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superadmin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'


