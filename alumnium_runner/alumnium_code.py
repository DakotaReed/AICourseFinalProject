import os
from dotenv import load_dotenv
from selenium.webdriver import Chrome
from alumnium import Alumni
from alumnium.models import Model, Provider  # כדי לשלוט ב-provider

load_dotenv()

# ודא שמפתח קיים
if not os.environ.get("GOOGLE_API_KEY"):
    print("❌ GOOGLE_API_KEY חסר בקובץ .env")
    exit(1)

# נכריח את המחלקה להשתמש ב-Google Gemini
Model.current = Model(
    provider=Provider.GOOGLE,
    name="gemini-2.5-flash-preview-04-17"  # או כל מודל נתמך אחר
)

def run_test():
    driver = Chrome()
    driver.get("https://todomvc.com/examples/vue/dist/#/")
    al = Alumni(driver)  # לא צריך להעביר llm ידנית
    try:
        al.do("in input 'What we need to do' Add a to do: 'pick up the kids' and press Enter and wait 2 seconds")
        al.do("in input 'What we need to do' Add a to do: 'buy milk' and press Enter and wait 2 seconds")
        al.do("mark all tasks in list complete and wait 2 seconds after it and stop this action when all tasks are marked")
        al.check("task 'buy milk' is completed")
        print("✅ הצלחה!")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
