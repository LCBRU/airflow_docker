import os

from flask_appbuilder.security.manager import AUTH_LDAP

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

AUTH_TYPE = AUTH_LDAP 
AUTH_LDAP_SERVER = "ldap://ldaplookups.xuhl-tr.nhs.uk:389"
AUTH_LDAP_USE_TLS = False

# registration configs
AUTH_USER_REGISTRATION = True  # allow users who are not already in the FAB DB
AUTH_USER_REGISTRATION_ROLE = "Admin"  # this role will be given in addition to any AUTH_ROLES_MAPPING
AUTH_LDAP_FIRSTNAME_FIELD = "givenName"
AUTH_LDAP_LASTNAME_FIELD = "sn"
AUTH_LDAP_EMAIL_FIELD = "mail"  # if null in LDAP, email is set to: "{username}@email.notfound"
AUTH_LDAP_UID_FIELD = "sAMAccountName"

AUTH_LDAP_USERNAME_FORMAT = "XUHL-TR\\%s"

# search configs
AUTH_LDAP_SEARCH = "OU=UHLUsers,DC=xuhl-tr,DC=nhs,DC=uk"  # the LDAP search base
AUTH_LDAP_UID_FIELD = "sAMAccountName"  # the username field
