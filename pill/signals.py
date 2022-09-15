from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from pill.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         print(**kwargs)
#         print("hii this is signal")


def create_profile(email, role):
    creators, created = Group.objects.get_or_create(name='Creator')
    subscribers, created = Group.objects.get_or_create(name='Subscriber')
    ct = ContentType.objects.get_for_model(User)
    p_add = Permission.objects.create(codename ='ppadd', name ='Can ppadd', content_type = ct)
    p_edit = Permission.objects.create(codename ='pedit', name ='Can pedit', content_type = ct)
    p_view = Permission.objects.create(codename ='pview', name ='Can pview', content_type = ct)
    p_delete = Permission.objects.create(codename ='pdelete', name ='Can pdelete', content_type = ct)
    creator_permissions = [
        p_add,
        p_edit,
        p_view,
        p_delete,
    ]
    creators.permissions.set(creator_permissions)
    subscribers.permissions.add(p_view)
    if role == 'CREATOR':
        creators.user_set.add(User.objects.get(email=email))
    else:
        creators.user_set.add(User.objects.get(email=email))