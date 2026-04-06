# GitHub Activity CLI

GitHub Activity CLI is a command-line interface (CLI) application designed to fetch and display the recent public activity of any GitHub user directly in your terminal. It provides a simple way to view actions like pushes, issues, stars, and more using the GitHub API.

## Installation

To get started with the GitHub Activity CLI:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/github-activity-cli.git
   cd github-activity-cli
   ```

2. (Optional) Install or make the script executable depending on your language:

   ```bash
   chmod +x github-activity
   ```

   Or if using Python:

   ```bash
   pip install .
   ```

   If you encounter a warning that the script is installed in a directory that’s not in your PATH, follow the instructions below.

### Add `github-activity` to your PATH (if needed)

If you see a warning about the script not being in your `PATH`, add the following to your shell's configuration file:

- For **Bash**:

  ```bash
  echo 'export PATH=$PATH:/home/username/.local/bin' >> ~/.bashrc
  source ~/.bashrc
  ```

- For **Zsh**:

  ```bash
  echo 'export PATH=$PATH:/home/username/.local/bin' >> ~/.zshrc
  source ~/.zshrc
  ```

## Usage

### Fetch User Activity

To fetch and display recent activity for a GitHub user:

```bash
github-activity <username>
```

Example:

```bash
github-activity kamranahmedse
```

Sample Output:

```bash
- Closed a pull request in kamranahmedse/claude-statusline.
- Commits pushed in kamranahmedse/claude-statusline.
- Opened a new issue comment in kamranahmedse/slim.
- Commits pushed in kamranahmedse/diffity.
```

## How It Works
- Accepts a GitHub username as a command-line argument
- Sends a request to the GitHub API:
```bash
https://api.github.com/users/<username>/events
```
- Parses the returned JSON response
- Formats and displays the activity in a readable format

## Contributing

We welcome contributions to improve the Task Tracker CLI! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit and push your changes (`git push origin feature-name`).
5. Submit a pull request.

## Useful Links

- Project URL: [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/github-user-activity)
- CLI application with Python: https://dev.to/kanakos01/create-a-cli-application-with-python-1j37

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
