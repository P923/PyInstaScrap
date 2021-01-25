import json
from datetime import datetime

from instagram_private_api import (Client, ClientError, ClientLoginError, ClientCookieExpiredError,
                                   ClientLoginRequiredError, __version__ as client_version)
import sys
import os.path
from utils.utils import *


def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json)
        print('SAVED: {0!s}'.format(new_settings_file))


def login(username, password, path_cookie):
    print('Client version: {0!s}'.format(client_version))
    device_id = None

    try:
        if not os.path.isfile(path_cookie):
            api = Client(username, password, on_login=lambda x: onlogin_callback(x, "insta_cookie"))

        else:
            with open(path_cookie) as file_data:
                cached_settings = json.load(file_data, object_hook=from_json)
            print('Reusing settings: {0!s}'.format(path_cookie))
            device_id = cached_settings.get('device_id')
            # reuse auth settings
            api = Client(username, password, settings=cached_settings)

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        print('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))
        api = Client(username, password, device_id=device_id, on_login=lambda x: onlogin_callback(x, "insta_cookie"))

    except ClientLoginError as e:
        print('ClientLoginError {0!s}'.format(e))
        sys.exit()
    except ClientError as e:
        print('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response))
        sys.exit()
    except Exception as e:
        print('Unexpected Exception: {0!s}'.format(e))
        sys.exit()

    # Show when login expires
    cookie_expiry = api.cookie_jar.auth_expires
    print('Cookie Expiry: {0!s}'.format(datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')))
    print("\n")

    return api
