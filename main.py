from utils import log, ig
from pprint import pprint
from datetime import date

# Get feeds from Instagram timeline
feeds = ig.get_timeline_feed()
# Filter feeds from following account only and not sponsor account
filtered_feeds = list(filter(lambda feed: feed.get('media_or_ad') and feed['media_or_ad']['user']['friendship_status']['following'] == True,
                             list(feeds['feed_items'])))
# Map each feed to expected dictionary
jobs = list(map(lambda item: dict({
    'source': f'Instagram | username  {item["media_or_ad"]["user"]["username"]}',
    'title': str(item['media_or_ad']['caption']['text']).splitlines()[0],
    'text': item['media_or_ad']['caption']['text'],
    'posted_at': date.fromtimestamp(item['media_or_ad']['taken_at']).isoformat()
}), filtered_feeds))

pprint(jobs)
