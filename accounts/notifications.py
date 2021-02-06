import admin_notifications
from .models import Requsest
def notification():
    broken_links = Requsest.objects.filter(status=False).count()
    if broken_links:
        return "You have %s broken link%s.<br>You can view or fix them using the <a href='/admin/linkcheck/'>Link Manager</a>." % (broken_links, "s" if broken_links>1 else "")
    else:
        return ''

admin_notifications.register(notification)