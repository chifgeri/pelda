from django.db import models

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Hallgato(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    neptun = models.SlugField(blank = False, primary_key = True)
    sex = models.CharField(blank=True, max_length=20, choices = SEX_CHOICES)
    age = models.IntegerField(blank = False)
    email = models.EmailField(blank = True)

    class Meta:
        ordering = ['age']

    def __str__(self):
        return self.name


class Kor(models.Model):
    name = models.CharField(max_length = 50)
    leader = models.OneToOneField('Hallgato', on_delete = models.CASCADE, related_name = 'leader')
    members = models.ManyToManyField('Hallgato')

    def __str__(self):
        return self.name

    @property
    def get_member_count(self):
        return self.members.count()

# Create your models here.
