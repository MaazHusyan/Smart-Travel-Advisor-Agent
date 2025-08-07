from agents import function_tool

  
@function_tool
def get_mhotels(date: str, city: str) -> list:
    """Mock tool to get hotels data."""
    
    return [
        {
            "name": "Sikandar",
            "city": city,
            "date": date,
            "price" :"10000 PKR"
        },
        {
            "name": "Sanam",
            "city": city,
            "date": date,
            "price" :"12000 PKR"
        },
        {
            "name": "Avari",
            "city": city,
            "date": date,
            "price" :"15000 PKR"
        }
    ]