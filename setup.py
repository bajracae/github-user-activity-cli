from setuptools import setup

setup(
    name="github_activity",
    version="1.0",
    packages=["github_activity"],
    entry_points={
        "console_scripts": ["github-activity = github_activity.__main__:main"],
    },
    description="CLI app to track your tasks and manage your to-do list ",
    author="abajrach",
    url="https://github.com/bajracae/github-user-activity-cli",
    python_requires=">=3.6",
)