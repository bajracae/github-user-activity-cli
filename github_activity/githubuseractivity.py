import requests

class GithubUserActivity():
    def __init__(self):
        pass

    def get_github_user_activity(self, username):
        try:
            url = f"https://api.github.com/users/{username}/events"
            response = requests.get(url).json()
            return response
        except Exception as e:
            raise HTTPException(e)