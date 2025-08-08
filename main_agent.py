import asyncio

from agents import(
    Agent,
    Runner,
    handoff,
    SQLiteSession    
)

from _instructions import get_main_agent_instruction
from gemini_model import geminiModel, config
from my_agents.booking_agent import bookingAgent
from my_agents.destination_agent import destinationAgent
from my_agents.explore_agent import exploreAgent



def main_agent():
    """
    This function creates an orchestrator agent that manages the workflow of other agents.
    It can be used to coordinate tasks, manage dependencies, and ensure that the overall
    process runs smoothly.
    """
    
    print("Initializing Main Agent...")
    agent = Agent(
        name= "main_agent",
        instructions= get_main_agent_instruction(),
        model= geminiModel,
        tools= [],  # No specific tools for this agent
        handoffs= [
            handoff(bookingAgent()),
            handoff(destinationAgent()),
            handoff(exploreAgent())
            ]
    )
    return agent

async def run_main_agent():
    agent = main_agent()
    session = SQLiteSession("user_maaz", "chat_history.db")
   

    print("WELLCOME TO SMART TRAVEL ADVISOR AGENT")
    
    while True:
        query = input("🧑🏽: ").strip()
        
        if query.lower() in ["exit", "quit", "stop"]:
            print("Exiting the Career Mentor Agent. Goodbye!")
            break
        
      
        result = await Runner.run(
           starting_agent= agent,
           input= query,
           run_config= config,
           max_turns= 5,
           session=session
          
        )
        
        print(f"🤖: {result.final_output}\n")
        
if __name__ == "__main__":
    asyncio.run(run_main_agent())