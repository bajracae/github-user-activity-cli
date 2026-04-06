import argparse
from github_activity.githubuseractivity import GithubUserActivity

def main():
    githubuseractivity = GithubUserActivity()

    parser = argparse.ArgumentParser(description="A CLI Github User Activity Tool", epilog="Example: github-activity <username>")
    parser.add_argument("username", help="Github Username")
    
    args = parser.parse_args()

    if args.username:
        events = githubuseractivity.get_github_user_activity(args.username)
        for event in events:
            event_type = event["type"]
            event_repo_name = event['repo']['name']

            if event_type == "CommitCommentEvent":
                if payload_action == "created":
                    print(f"Created a new commit comment in {event_repo_name}.")
            
            elif event_type == "CreateEvent":
                ref_type = event[""]
                print(f"Created a new branch or tag in {event_repo_name}")
            
            elif event_type == "DeleteEvent":
                print(f"Deleted a branch or tag in {event_repo_name}")
            
            elif event_type == "DiscussionEvent":
                print(f"Created a discussion in {event_repo_name}")

            elif event_type == "GollumEvent":
                print(f"Created or updated some wiki page. Github documentation is really poor.")

            elif event_type == "ForkEvent":
                event_forkee = event["forkee"]
                print(f"Forked the repository {event_forkee}.")
            
            elif event_type == "IssueCommentEvent":
                payload_action = event["payload"]["action"]
                if payload_action == "created":
                    print(f"Opened a new issue comment in {event_repo_name}.")

            elif event_type == "IssuesEvent":
                payload_action = event["payload"]["action"]
                if payload_action == "opened":
                    print(f"Opened an issue in {event_repo_name}.")
                if payload_action == "closed":
                    print(f"Closed an issue in {event_repo_name}.")
                if payload_action == "reopened":
                    print(f"Reopened an issue in {event_repo_name}.")

            elif event_type == "Member":
                payload_action = event["payload"]["action"]
                payload_member = event["payload"]["member"]
                if payload_action == "added":
                    print(f"Added {payload_member} to a {event_repo_name}")

            elif event_type == "PullRequestEvent":
                payload_action = event["payload"]["action"]
                if payload_action == "opened":
                    print(f"Opened a pull request in {event_repo_name}.")
                if payload_action == "closed":
                    print(f"Closed a pull request in {event_repo_name}.")
                if payload_action == "merged":
                    print(f"Merged in a pull request in {event_repo_name}.")
                if payload_action == "reopened":
                    print(f"Reopened a pull request in {event_repo_name}.")
                if payload_action == "assigned":
                    print(f"Assigned to the pull request in {event_repo_name}.")
                if payload_action == "unassigned":
                    print(f"Unassigned from a pull request in {event_repo_name}.")
                if payload_action == "labeled":
                    print(f"Labeled a pull request in {event_repo_name}.")
                if payload_action == "unlabeled":
                    print(f"Unlabeled a pull request in {event_repo_name}.")

            elif event_type == "PullRequestReviewEvent":
                payload_action = event["payload"]["action"]
                if payload_action == "created":
                    print(f"Pull Request Review created in {event_repo_name}.")                
                if payload_action == "updated":
                    print(f"Pull Request Review updated in {event_repo_name}.")                
                if payload_action == "dismissed":
                    print(f"Pull Request Review dismissed in {event_repo_name}.")                

            elif event_type == "PullRequestReviewCommentEvent":
                print("Something was done with a Pull Request Review comment. Documentation is very vague...")

            elif event_type == "PushEvent":
                print(f"Commits pushed in {event_repo_name}.")

            elif event_type == "ReleaseEvent":
                payload_action = event["payload"]["action"]
                if payload_action == "published":
                    print(f"Published a release in {event_repo_name}.")
            
            elif event_type == "WatchEvent":
                payload_action = event["payload"]["action"]
                if payload_action == "started":
                    print(f"Starred {event_repo_name}.")
            
            else:
                print("Unknown event type found.")


if __name__ == "__main__":
    main()