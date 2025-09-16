import requests

response = requests.get('https://api.github.com/users/octocat')

if response.status_code == 200:
    user_data = response.json()

    print(f"Username:", user_data[0]['login'])
    print(f"Namme:", {user_data[0]['name']})
    print(f"Bio:", user_data[0]['bio'])
    print(f"Public Repos:", user_data[0]['public_repos'])
    print(f"Followers:", user_data[0]['followers'])
    print(f"Following:", user_data[0]['following'])
else:
    print("Failed to retrieve data")