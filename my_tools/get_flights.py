from agents import function_tool

@function_tool
def get_mflights(date: str, city: str, to_city: str, from_city:str) -> list:
    """Mock tool to get flights data."""
    
    return [
        {
            "name": "air baltic",
            "city": city,
            "date": date,
            "ticket price" :"4399 PKR",
            "from": from_city,
            "to": to_city
        },
        {
            "name": "air blue",
            "city": city,
            "date": date,
            "ticket price" :"4999 PKR",
            "from": from_city,
            "to": to_city
        },
        {
            "name": "air bus",
            "city": city,
            "date": date,
            "ticket price" :"5999 PKR",
            "from": from_city,
            "to": to_city
        }
    ]
    
  