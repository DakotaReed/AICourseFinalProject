# 📘 AI Course Final Project

This project demonstrates an integration of two AI agents — one using [Alumnium](https://github.com/langchain-ai/alumnium) and the other using `browser_use` — 
to automate and test a web page. The agents run in sequence, simulating human interaction with a **TodoMVC** app using natural language instructions.

---

## 🚀 Project Structure

```
AICourseFinalProject-master/
│
├── main.py                       # Entry point that runs both agents
│
├── alumnium_runner/
│   ├── alumnium_code.py         # Alumnium-based automation agent
│   └── requirements.txt         # Dependencies for Alumnium agent
│
├── browser_use_runner/
│   ├── browser_use_code.py      # browser_use agent that types and interacts
│   └── requirements.txt         # Dependencies for browser_use agent
```

---

## 🤖 What Each Agent Does

### 🟪 Alumnium Agent (`alumnium_code.py`)
- Uses LangChain with the Alumnium tool to:
  - Navigate to a website
  - Understand tasks in natural language
  - Execute browser actions using headless automation
- Powered by OpenAI LLMs and agent-style execution

### 🟦 Browser Use Agent (`browser_use_code.py`)
- Uses the `browser_use` package to:
  - Go to `https://todomvc.com/examples/vue/dist/`
  - Find the input field with placeholder "What needs to be done?"
  - Type “Buy Milk”, press Enter, and mark the task as complete

---

## 🧪 How to Run the Project

1. **Clone the repo** (or extract the ZIP you downloaded):

```bash
git clone https://github.com/YOUR_USERNAME/AICourseFinalProject.git
cd AICourseFinalProject
```

2. **Set up Python environments** for each agent (or use virtual environments):

### Alumnium Agent
```bash
cd alumnium_runner
pip install -r requirements.txt
```

### Browser Use Agent
```bash
cd ../browser_use_runner
pip install -r requirements.txt
```

3. **Run the main script**
```bash
cd ..
python main.py
```

This will first run the Alumnium agent and then the browser_use agent, one after the other.

---

🧪 This project also includes automated tests written with Pytest, and test reporting using Allure for detailed, user-friendly reports.


## 📦 Dependencies

Each agent has its own `requirements.txt`.  
Some key libraries used:

- alumnium

- browser-use

- pytest (for testing)

- allure-report (for test reporting)
---

## 🙏 Acknowledgments

Thanks to Yoni for the inspiring AI course.  
This project is a hands-on application of multi-agent browser automation, demonstrating the power of language-driven UI testing and interaction.
