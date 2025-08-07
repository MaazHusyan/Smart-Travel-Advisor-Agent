from agents import Agent

from _instructions import get_explore_agent_instruction
from gemini_model import geminiModel


def exploreAgent() -> Agent:
    """
    Create and return the Explore Agent with its tools and instructions.
    """
    print("Initializing Explore Agent...")
    
    agent = Agent(
        name="Explore Agent",
        instructions=get_explore_agent_instruction(),
        model=geminiModel,
        tools=[]  # No specific tools for this agent
    )
    
    return agent