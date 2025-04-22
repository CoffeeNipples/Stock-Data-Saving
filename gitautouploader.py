from datetime import datetime
import subprocess
import os

def gitautoupload():
    print("Running COMMIT script")

    # Set the working directory
    repo_dir = os.path.expanduser("~/myenv/Stock-Data-Saving")

    try:
        # Navigate to the repo directory and run the commands
        subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
        subprocess.run(["git", "commit", "-m", f"stock price saving {datetime.now()}"], cwd=repo_dir, check=True)
        subprocess.run(["git", "push"], cwd=repo_dir, check=True)

        print("Repository updated successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

