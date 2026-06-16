# app/mcp/github_agent.py

from github import Github

class GithubAgent:

    def __init__(self, token):

        self.client = Github(token)

    def find_recent_fixes(
        self,
        repo_name
    ):

        repo = self.client.get_repo(
            repo_name
        )

        commits = repo.get_commits()

        fixes = []

        for commit in commits[:10]:

            message = (
                commit.commit.message
            )

            if (
                "fix" in message.lower()
            ):
                fixes.append(message)

        return fixes