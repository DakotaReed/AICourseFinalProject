import subprocess
import sys

# def run_alumnium():
#     subprocess.run([
#         r'alumnium_runner\venv\Scripts\python.exe',
#         'alumnium_runner/alumnium_code.py'
#     ], check=True)

def run_browser_use():
    subprocess.run([
        r'browser_use_runner\venv\Scripts\python.exe',
        'browser_use_runner/browser_use_code.py'
    ], check=True)

if __name__ == "__main__":
    print("Running Alumnium...")
    # run_alumnium()

    print("Running Browser Use...")
    run_browser_use()
