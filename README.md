# 🚀 Smart Travel Designer Agent 
📖 **Description**

The Gemini Travel Agent Project is a Python-based project that aims to create a conversational AI-powered travel booking system. This system is designed to assist users in planning and booking their travel smoothly, providing them with personalized recommendations for flights, hotels, and destinations. The project utilizes OpenAI's ChatCompletionsModel to generate human-like responses and provide users with relevant information.

The project is structured around multiple agents, each responsible for a specific task, such as booking flights, suggesting hotels, or providing destination information. These agents work together to provide users with a seamless travel planning experience. The project also includes tools for handling handoffs between agents, ensuring a smooth transition between tasks.

**✨ Features**

1. **Conversational Interface**: The project provides a conversational interface that allows users to interact with the system in a natural language.
2. **OpenAI Integration**: The project utilizes OpenAI's ChatCompletionsModel to generate human-like responses and provide users with relevant information.
3. **Multi-Agent Architecture**: The project is structured around multiple agents, each responsible for a specific task, allowing for a more efficient and effective travel planning experience.
4. **Handoff Mechanism**: The project includes a handoff mechanism that allows agents to seamlessly transfer control to other agents, ensuring a smooth transition between tasks.
5. **Personalized Recommendations**: The project provides users with personalized recommendations for flights, hotels, and destinations based on their preferences and travel history.
6. **Mock Data Generation**: The project includes tools for generating mock data for flights and hotels, allowing for testing and development of the system.
7. **SQLite Database**: The project utilizes a SQLite database to store user information and travel preferences.
8. **AsyncIO Support**: The project is designed to support asynchronous programming, allowing for efficient handling of multiple tasks and requests.

**🧰 Tech Stack Table**

| Tech Stack | Description |
| --- | --- |
| Python | Programming language used for the project |
| OpenAI | ChatCompletionsModel used for natural language processing |
| SQLite | Database used for storing user information and travel preferences |
| AsyncIO | Library used for asynchronous programming |
| Dotenv | Library used for loading environment variables from a .env file |

**📁 Project Structure**

* `agents/`: Contains the agent classes, each responsible for a specific task.
* `_instructions/`: Contains the instruction files for each agent.
* `gemini_model.py`: Contains the Gemini model class.
* `get_flights.py`: Contains the function for getting flights data.
* `suggest_hotels.py`: Contains the function for getting hotels data.
* `main_agent.py`: Contains the main agent class.
* `destination_agent.py`: Contains the destination agent class.
* `booking_agent.py`: Contains the booking agent class.
* `explore_agent.py`: Contains the explore agent class.
* `environment variables`: Contains the .env file used for loading environment variables.
* `requirements.txt`: Contains the project dependencies.

**⚙️ How to Run**

1. **Setup**: Install the project dependencies by running `pip install -r requirements.txt`.
2. **Environment**: Set the environment variables by creating a .env file and configuring the variables accordingly.
3. **Build**: Run the project by executing the `main_agent.py` file.
4. **Deploy**: The project can be deployed to a production environment by configuring the environment variables and deploying the application.

**👤 Author**

* [Maaz Husyan]

**📝 License**

* This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

I hope this README provides a comprehensive overview of the Gemini Travel Agent Project. If you have any questions or need further clarification, please don't hesitate to reach out! 😊
