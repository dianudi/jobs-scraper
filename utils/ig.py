from instagrapi import Client
from instagrapi.exceptions import LoginRequired, BadPassword, BadCredentials
from os.path import exists
from os import getenv
from utils import log
from dotenv import load_dotenv
load_dotenv()
ig = Client(delay_range=[1, 3])

if (not exists('storage/session.json')):
    try:
        ig.set_locale('id_ID')
        ig.set_country_code(62)
        ig.set_user_agent(
            "Instagram 309.1.0.41.113 Android (30/11.0.0; 300dpi; 1280x720; Xiaomi; Redmi 4x; santoni; qcom; id_ID; 314665256)")
        ig.set_device({
            "app_version": "309.1.0.41.113",
            "android_version": 30,
            "android_release": "11.0.0",
            "dpi": "300dpi",
            "resolution": "1280x720",
            "manufacturer": "Xiaomi",
            "device": "santoni",
            "model": "Redmi 4X",
            "cpu": "qcom",
            "version_code": "314665256"})
        ig.login(getenv('IG_USERNAME'), getenv('IG_PASSWORD'))
        ig.dump_settings('storage/session.json')
        # ig.get_reels_tray_feed()
        # ig.get_timeline_feed()
    except BadPassword:
        log.error('Wrong password')
    except BadCredentials:
        log.error('Username is invalid or wrong password')
    except Exception as e:
        log.error(f'Something went wrong {e}')
else:
    try:
        ig.load_settings('storage/session.json')
    except LoginRequired:
        log.error('Session is invalid, need relogin')
        ig.login(getenv('IG_USERNAME'), getenv('IG_PASSWORD'))
        ig.dump_settings('storage/session.json')
    except Exception as e:
        log.error(f'Something went wrong {e}')
