import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='movies.Person')
def congratulatory(sender, instance, created, **kwargs):
    __import__('pdb').set_trace()
    if created and instance.birth_date == datetime.date.today():
        print(f'У {instance.full_name} сегодня день рождения! 🥳')


# post_save.connect(receiver=congratulatory, sender='movies.Person', weak=True, dispatch_uid='congratulatory_signal')
