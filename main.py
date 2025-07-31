from agents.destination_agent import get_destination
from agents.booking_agent import get_booking_info
from agents.explore_agent import get_exploration_info

def main():
    print("🌍 Welcome to AI Travel Designer Agent")

    # Step 1: Ask user for interest
    user_input = input("\n🧳 What kind of travel experience are you looking for?\n> ")
    destination = get_destination(user_input)

    print(f"\n📌 Suggested destination: {destination}")
    confirm = input("Do you want to proceed with this destination? (yes/no)\n> ")
    if confirm.lower() != "yes":
        print("Okay, maybe next time! Goodbye!")
        return

    # Step 2: Booking Agent
    print("\n✈️ BookingAgent:")
    print(get_booking_info(destination))

    # Step 3: Explore Agent
    print("\n🌄 ExploreAgent:")
    print(get_exploration_info(destination))

    print("\n✅ Your personalized travel plan is ready! Have a wonderful trip!")

if __name__ == "__main__":
    main()