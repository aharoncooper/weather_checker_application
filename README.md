# weather_checker_application
Project Number 1

Introduction:
The main goal of this project is to provide a weather checker application that can retrieve the weather conditions and the date and time in said city. Weather conditions were gathered from an API key acquired from http://api.openweathermap.org.

Features:

User interface: The user can easily type in the city they are looking for and receive the current temperature, weather conditions, humidity, and current date and time.

Data management: The project makes use of the requests library to send HTTP requests and retrieve JSON data from external APIs.We use requests.get() to send a GET request to the specified URL with optional query parameters. We check the status code of the response to ensure the request was successful (status code 200). If the request is successful, we parse the JSON response using .json() method of the response object. We return the parsed JSON data for further processing.

Date and Time: The project includes functionality to work with dates and times using Python's datetime module. The application allows the user to convert between different timezones in order to receive the exact time and date in the timezone specified.

Installation:

1. Clone the github repository: open a terminal or command prompt and use the git clone command followed by the repository URL. 'git clone https://github.com/aharoncooper/weather_checker_application'
2. Navigate to the Project Directory: 'cd weather_checker_application'
3. Install Dependencies: Install poetry, initialize poetry, add dependencies, and install dependencies. All dependencies can be found in pyproject.toml
4. Install Streamlit
5. Run the Streamlit App: 'streamlit run weather_checker_application\main.py'

Contact:

email- shmuel5767@gmail.com