import os
import datetime
import subprocess
import re

# Path to your local GitHub repo
REPO_PATH = os.path.join(os.getcwd(), "aditya0yadav")
README_PATH = os.path.join(REPO_PATH, "README.md")

def update_readme():
    today = datetime.datetime.now().strftime("%d %B %Y")  # e.g., 24 October 2025

    with open(README_PATH, "r") as f:
        content = f.read()

    new_content = re.sub(
        r'self\.date\s*=\s*".*?"',
        f'self.date = "{today}"',
        content
    )

    with open(README_PATH, "w") as f:
        f.write(new_content)

    print(f"✅ Updated README with date: {today}")

def git_commit():
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "README.md"])
    subprocess.run([
        "git", "commit", "-m",
        f"Updated README: {datetime.datetime.now().strftime('%Y-%m-%d')}"
    ])
    subprocess.run(["git", "push", "origin", "main"])
    print("🚀 Changes pushed to GitHub successfully")

if __name__ == "__main__":
    update_readme()
    git_commit()
