import os
import datetime
import re

README_PATH = os.path.join(os.getcwd(), "README.md")

def update_readme():
    today = datetime.datetime.now().strftime("%d %B %Y")
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

if __name__ == "__main__":
    update_readme()
