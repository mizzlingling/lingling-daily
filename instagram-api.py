#!/usr/bin/env python3
"""
Instagram Photo Fetcher for @abearhug
Usage: python3 instagram-api.py
"""

import json
import urllib.request
import urllib.error

def fetch_instagram_photos(username='abearhug', count=5):
    """
    Fetch recent photos from Instagram username
    """
    try:
        # Instagram public API endpoint
        url = f'https://www.instagram.com/{username}/?__a=1&__d=dis'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))

                # Try to extract photos from different possible JSON structures
                try:
                    posts = data['graphql']['user']['edge_owner_to_timeline_media']['edges']
                except (KeyError, TypeError):
                    try:
                        posts = data['data']['user']['edge_owner_to_timeline_media']['edges']
                    except (KeyError, TypeError):
                        print("Could not find posts in response")
                        return None

                photos = []
                for post in posts[:count]:
                    node = post['node']
                    photos.append({
                        'url': node.get('display_url') or node.get('thumbnail_src'),
                        'shortcode': node.get('shortcode'),
                        'link': f"https://www.instagram.com/p/{node.get('shortcode')}/"
                    })

                return photos
            else:
                print(f"Error: Status code {response.status}")
                return None

    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        return None
    except Exception as e:
        print(f"Error fetching Instagram: {e}")
        return None

if __name__ == '__main__':
    print("🔄 Fetching Instagram photos from @abearhug...")
    photos = fetch_instagram_photos()

    if photos:
        print("✅ Successfully fetched Instagram photos:")
        print(json.dumps(photos, indent=2))

        # Save to JSON file
        with open('instagram-photos.json', 'w', encoding='utf-8') as f:
            json.dump(photos, f, indent=2, ensure_ascii=False)
        print("\n📁 Saved to instagram-photos.json")
    else:
        print("❌ Failed to fetch Instagram photos")
        print("Instagram may require login or has changed their API")
