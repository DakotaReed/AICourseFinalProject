import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")

class AsyncLLMAdapter:
    def __init__(self, sync_llm):
        self.sync_llm = sync_llm
        self.model = getattr(sync_llm, "model", "llama3-90b-8192")
        self.model_name = self.model
        self.provider = "groq"

    async def ainvoke(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: self.sync_llm.invoke(*args, **kwargs))

async def main():
    todo_task = (
        "Open the page https://todomvc.com/examples/vue/dist/ and wait until it fully loads. "
        "Then find the input with placeholder 'What needs to be done?'. "
        "Type 'Buy Milk' and press Enter. "
        "Then mark the new todo item as completed. "
        "Finally, confirm that 'Buy Milk' is marked as completed."
    )

    sync_llm = ChatGroq(model="llama3-90b-8192", groq_api_key=groq_api_key)
    llm = AsyncLLMAdapter(sync_llm)

    print("🚧 Starting task:", todo_task)

    agent = Agent(task=todo_task, llm=llm)

    logs = await agent.run()
    print(f"\nFinal Result: {logs.final_result()}")

if __name__ == "__main__":
    asyncio.run(main())
