import subprocess
import sys
import os


def run_alumnium():
    print("Running Alumnium Tests via Pytest + Allure...")

    # Run pytest with Allure output
    subprocess.run([
        r'alumnium_runner\venv\Scripts\python.exe',
        '-m', 'pytest',
        'alumnium_runner/alumnium_code.py',
        '--alluredir=alumnium_runner/allure-results',
        '-s'
    ], check=True)

    # Generate the Allure report
    subprocess.run([
        r'C:\Users\dakot\Desktop\PyLearn\allure-2.34.1\bin\allure.bat',
        'generate', 'alumnium_runner/allure-results', '-o', 'alumnium_runner/allure-report', '--clean'
    ], check=True)

    # Optionally open it in browser
    subprocess.Popen([
        r'C:\Users\dakot\Desktop\PyLearn\allure-2.34.1\bin\allure.bat',
        'open', 'alumnium_runner/allure-report'
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_browser_use():
    print("\nRunning Browser Use Code...")
    subprocess.run([
        r'browser_use_runner\venv\Scripts\python.exe',
        'browser_use_runner/browser_use_code.py'
    ], check=True)


if __name__ == "__main__":
    run_alumnium()
    run_browser_use()
