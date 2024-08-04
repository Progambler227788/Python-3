import tweepy
import csv

# Set up Twitter API credentials
consumer_key = 'ieuWFmOa8WCZ1oIoIoAxi1rQJ'
consumer_secret = '0zBzejVg2hanTysCxRUQv4OGzvCHziDJNUiexL1pQRnyviTccg'
access_token = '1765135916010508288-04ozjLKn5KBO4tSlkpVui9GFzQuvsW'
access_token_secret = 'bP8mLpen3DX8hTwwk1il9siS2wTiMGiINVNVqllMi3htg'
# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_followers(username):
    try:
        # Get user object for the specified username
        user = api.get_user(screen_name=username)
        # Get followers' IDs
        followers_ids = api.followers_ids(screen_name=username)
        # Get user objects for each follower
        followers = [api.get_user(user_id) for user_id in followers_ids]
        return followers
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
username = 'Fra_Lanti'
followers = get_followers(username)
if followers:
    print(f"Followers of {username}:")
    with open('followers.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Screen Name', 'Name', 'Followers Count'])
        for follower in followers:
            writer.writerow([follower.screen_name, follower.name, follower.followers_count])
            print(follower.screen_name)