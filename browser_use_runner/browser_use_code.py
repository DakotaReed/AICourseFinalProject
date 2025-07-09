import asyncio
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm import ChatGoogle

load_dotenv()

async def main():
    todo_task = (
        "Open the page https://todomvc.com/examples/vue/dist/ and wait until it fully loads. "
        "Then find the input with placeholder 'What needs to be done?'. "
        "Type 'Buy Milk' and press Enter. "
        "Then mark the new todo item as completed. "
        "Finally, confirm that 'Buy Milk' is marked as completed."
    )

    print("🚧 Starting task:", todo_task)

    agent = Agent(task=todo_task,
                  llm=ChatGoogle(
                        model="gemini-2.5-pro",
                        temperature=0.3,
                                ),
                  verbose=True)

    logs = await agent.run()
    print(f"\nFinal Result: {logs.final_result()}")

if __name__ == "__main__":
    asyncio.run(main())
