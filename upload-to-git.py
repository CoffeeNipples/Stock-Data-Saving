
import subprocess

print("Running COMMIT script")

# Commits file to git 
try:
    subprocess.run(["cd","myenv/Stock-Data-Saving"], shell=True,check=True)

    subprocess.run(["git","add","."], check=True)

    subprocess.run(["git","commit","-m", "stock price saving"+datetime.now()], check=True)

    subprocess.run(["git","push"], check=True)

    print("Repository updated successfully!")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
