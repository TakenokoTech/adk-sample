import asyncio
import re

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from wiki_agent.agent import root_agent

APP_NAME = "wiki_agent_app"
USER_ID = "user_1"
SESSION_ID = "session_001"

session_service = InMemorySessionService()
# session_service = DatabaseSessionService(db_url="sqlite:///./output/agent_data.db")
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)

print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")
print(f"Runner created for agent '{runner.agent.name}'.")

try:
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
except Exception as e:
    print(f"Session already exists: {e}")


async def main(text: str):
    with open("output/history.md", "w", encoding="utf-8") as f:
        f.write("# Wiki Agent History\n\n")

    content = types.Content(role='user', parts=[types.Part(text=text)])
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
        try:
            if event.author == "output_markdown_agent" or event.author == "update_markdown_agent":
                with open("output/output.md", "w", encoding="utf-8") as f:
                    f.write(re.sub("^```markdown\n", "", event.content.parts[0].text))
            if event.content and event.content.parts and event.content.parts[0].text:
                with open("output/history.md", "a", encoding="utf-8") as f:
                    f.write(f"## {event.author}\n\n")
                    f.write(event.content.parts[0].text)
                    f.write("\n\n")
        except Exception as e:
            print(f"Error processing event: {e}")
            continue


if __name__ == "__main__":
    content = "ルートパス"
    asyncio.run(main(content))
