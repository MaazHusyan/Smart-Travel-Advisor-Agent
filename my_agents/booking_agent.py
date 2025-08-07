from agents import Agent

from _instructions import get_booking_agent_instruction
from gemini_model import geminiModel
from my_tools.get_flights import get_mflights
from my_tools.suggest_hotels import get_mhotels


def bookingAgent() -> Agent:
    """
    Create and return the Booking Agent with its tools and instructions.
    """
    print("Initializing Booking Agent...")
    
    agent = Agent(
        name= "Booking Agent",
        instructions= get_booking_agent_instruction(),
        model= geminiModel,
        tools=[
            get_mflights,
            get_mhotels
        ],
        
    )
    
    return agent