import requests

def get_facebook_friends(access_token):
    # Make a request to the Facebook Graph API to get user's friends
    url = f'https://graph.facebook.com/v19.0/100072242415459/friends?access_token'
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        friends_data = response.json()

        # Extract friend information
        friends = friends_data.get('data', [])

        # Print friend names and IDs
        for friend in friends:
            print(f"Name: {friend.get('name')}, ID: {friend.get('id')}")
    else:
        print(f"Error: Unable to fetch friends. Status Code: {response.status_code}")
        print(response.text)

# Replace 'YOUR_ACCESS_TOKEN' with the actual access token
access_token = 'remove'
get_facebook_friends(access_token)
