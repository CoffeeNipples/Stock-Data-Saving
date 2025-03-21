
import subprocess

print("running updating yfinance script")

# Function to update yfinance automatically
try:
    print("Updating yfinance from GitHub...")
    subprocess.run(
            ["bash -c 'source /home/CoffeeNips/myenv/bin/activate'"], check=True, shell=True
            )
    subprocess.run(
            ["pip","install","--upgrade","yfinance"], check=True
            )
    print("yfinance updated successfully!")
except subprocess.CalledProcessError as e:
    print(f"Failed to update yfinance: {e}")


