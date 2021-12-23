#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Default configuration for the Airflow webserver"""
import os

from flask_appbuilder.security.manager import AUTH_DB, AUTH_LDAP

# from flask_appbuilder.security.manager import AUTH_LDAP
# from flask_appbuilder.security.manager import AUTH_OAUTH
# from flask_appbuilder.security.manager import AUTH_OID
# from flask_appbuilder.security.manager import AUTH_REMOTE_USER


basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# For details on how to set up each of the following authentication, see
# http://flask-appbuilder.readthedocs.io/en/latest/security.html# authentication-methods
# for details.

# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
# AUTH_OAUTH : Is for OAuth

AUTH_TYPE = AUTH_DB
# AUTH_TYPE = AUTH_LDAP
# AUTH_LDAP_SERVER = "ldap://ldaplookups.xuhl-tr.nhs.uk"
# AUTH_LDAP_USE_TLS = False

# # registration configs
# AUTH_USER_REGISTRATION = True  # allow users who are not already in the FAB DB
# AUTH_USER_REGISTRATION_ROLE = "Admin"  # this role will be given in addition to any AUTH_ROLES_MAPPING
# AUTH_LDAP_FIRSTNAME_FIELD = "givenName"
# AUTH_LDAP_LASTNAME_FIELD = "sn"
# AUTH_LDAP_EMAIL_FIELD = "mail"  # if null in LDAP, email is set to: "{username}@email.notfound"

# AUTH_LDAP_USERNAME_FORMAT = "XUHL-TR\\%s"

# # search configs
# AUTH_LDAP_SEARCH = "OU=UHLUsers,DC=xuhl-tr,DC=nhs,DC=uk"  # the LDAP search base
# AUTH_LDAP_UID_FIELD = "sAMAccountName"  # the username field
# # AUTH_LDAP_BIND_USER = "Briccs.LDAP"  # the special bind username for search
# # AUTH_LDAP_BIND_PASSWORD = "Br1cc5Uks"  # the special bind password for search
# print("*"*1000)