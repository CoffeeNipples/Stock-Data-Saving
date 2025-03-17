
import subprocess

print("running updating yfinance script")

# Function to update yfinance automatically
try:
    print("Updating yfinance from GitHub...")
    subprocess.run(
            ["sudo","pip","install","--upgrade","git+https://github.com/ranaroussi/yfinance.git"], check=True
            )
    print("yfinance updated successfully!")
except subprocess.CalledProcessError as e:
    print(f"Failed to update yfinance: {e}")


