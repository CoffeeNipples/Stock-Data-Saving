import subprocess

print("Beginning U finance update")

try:
    subprocess.run(["/home/CoffeeNips/myenv/bin/python", "-m", "pip", "install", "--upgrade", "yfinance"], check=True)
    print("yfinance upgrade successful.")
except subprocess.CalledProcessError as e:
    print(f"Failed to update yfinance: {e}")

