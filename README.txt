python3 manage.py makemessages -l ka

# in *.po file:
	# before:
	msgid "English"
	msgstr ""

	# after:
	msgid "English"
	msgstr "ინგლისური"

python3 manage.py compilemessages

# in settings.py file:

'django.middleware.locale.LocaleMiddleware'

from django.utils.translation import ugettext_lazy as _

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
LANGUAGES = [
    ('en', _('English')),
    ('ka', _('Georgian')),
]





	