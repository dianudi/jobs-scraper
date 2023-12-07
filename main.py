from utils import log, ig
from datetime import date
from dotenv import load_dotenv
from os import getenv
import schedule
from time import sleep

load_dotenv()


def get_job_posts():
    '''
    Get every post from instagram timeline and parse it.
    '''
    # Get feeds from Instagram timeline
    feeds = ig.get_timeline_feed()
    # Filter feeds from following account only and not sponsor account
    filtered_feeds = list(filter(lambda feed: feed.get('media_or_ad') and feed['media_or_ad']['user']['friendship_status']['following'] == True,
                                 list(feeds['feed_items'])))
    # Map each feed to expected dictionary
    jobs = list(map(lambda item: dict({
        'source': f'Instagram | Username  {item["media_or_ad"]["user"]["username"]}',
        'title': str(item['media_or_ad']['caption']['text']).splitlines()[0],
        'text': item['media_or_ad']['caption']['text'],
        'link_post': f'https://instagram.com/p/{item["media_or_ad"]["code"]}',
        'posted_at': date.fromtimestamp(item['media_or_ad']['taken_at']).isoformat()
    }), filtered_feeds))
    return jobs


def send_job_posts():
    '''Send jobs posts to server'''
    print(get_job_posts())
    pass


def main():
    schedule.every().minute.do(send_job_posts)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
