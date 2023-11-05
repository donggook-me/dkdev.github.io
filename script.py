import requests
from datetime import datetime, timedelta
import sys

# Set up authentication or use a Personal Access Token if needed
headers = {
    'Authorization': 'Bearer YOUR_GITHUB_TOKEN'
}

# GitHub repository information
owner = 'your-username'
repo = 'your-repo'

# Get the date a week ago
date_a_week_ago = (datetime.now() - timedelta(days=7)).isoformat()

# GitHub API endpoint to fetch commits
url = f'https://api.github.com/repos/{owner}/{repo}/commits'

# Parameters to filter commits within the last week
params = {
    'since': date_a_week_ago
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    commits_count = len(response.json())
    print(f"Number of commits in the last week: {commits_count}")
    sys.exit(commits_count)  # Return the value as the exit status
else:
    print(f"Failed to fetch commits. Status code: {response.status_code}")
    sys.exit(1)  # Return an error exit status

