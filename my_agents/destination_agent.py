from agents import Agent

from _instructions import get_destination_agent_instruction
from gemini_model import geminiModel


def destinationAgent() -> Agent:
    """
    Create and return the Destination Agent with its tools and instructions.
    """
    print("Initializing Destination Agent...")
    
    agent = Agent(
        name="Destination Agent",
        instructions=get_destination_agent_instruction(),
        model=geminiModel,
        tools=[]  # No specific tools for this agent
    )
    
    return agent