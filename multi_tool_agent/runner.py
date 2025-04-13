from google.adk import Runner
from google.adk.sessions import InMemorySessionService

from multi_tool_agent.agent import root_agent

APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"  # Using a fixed ID for simplicity

session_service = InMemorySessionService()
session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)
runner = Runner(
    agent=root_agent,  # The agent we want to run
    app_name=APP_NAME,  # Associates runs with our app
    session_service=session_service  # Uses our session manager
)

print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")
print(f"Runner created for agent '{runner.agent.name}'.")
