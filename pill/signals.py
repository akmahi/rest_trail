from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from pill.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Print **kwarg and instance not print anything
    Created denotes the post_save successfully saved or not
    **kwargs are signals send the all arguments in form kwargs, if it's not pass as parameter , ERROR will throw
    must specify the **Kwargs
    need configure(import) signal path imn apps.py under the ready class also configure the appconfig to app __init__.py
    or appname.app.custom_app_Config in INSTALLED_APPS on settings.py0
    """
    if created:
        creators, created = Group.objects.get_or_create(name='Creator')
        subscribers, created = Group.objects.get_or_create(name='Subscriber')
        if instance.role == 'CREATOR':
            creators.user_set.add(User.objects.get(email=instance.email))
        else:
            subscribers.user_set.add(User.objects.get(email=instance.email))


# @receiver(pre_init, sender=User)
# def create_group(sender, **kwargs):
#     print("pre_init")


# def create_profile(email, role):
#     creators, created = Group.objects.get_or_create(name='Creator')
#     subscribers, created = Group.objects.get_or_create(name='Subscriber')
    # ct = ContentType.objects.get_for_model(User)
    # p_add = Permission.objects.create(codename ='ppadd', name ='Can ppadd', content_type = ct)
    # p_edit = Permission.objects.create(codename ='pedit', name ='Can pedit', content_type = ct)
    # p_view = Permission.objects.create(codename ='pview', name ='Can pview', content_type = ct)
    # p_delete = Permission.objects.create(codename ='pdelete', name ='Can pdelete', content_type = ct)
    # creator_permissions = [
    #     p_add,
    #     p_edit,
    #     p_view,
    #     p_delete,
    # ]
    # creators.permissions.set(creator_permissions)
    # subscribers.permissions.add(p_view)
    # if role == 'CREATOR':
    #     creators.user_set.add(User.objects.get(email=email))
    # else:
    #     subscribers.user_set.add(User.objects.get(email=email))