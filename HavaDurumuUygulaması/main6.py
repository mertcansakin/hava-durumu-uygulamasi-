from tkinter import *
import requests
from PIL import ImageTk, Image

# OpenWeatherMap API URL
url = 'https://api.openweathermap.org/data/2.5/weather'

# OpenWeatherMap API Key
api_key = 'a83cc31247a3bd7e5a57f12d4eeb97b7'

# URL to get weather icon
icon_url = 'https://openweathermap.org/img/wn/{}@2x.png'

# Function to fetch and display weather information
def search_weather():
    # Get the user's input for city
    city = city_entry.get()

    # Parameters for API request
    params = {'q': city, 'appid': api_key, 'lang': 'tr'}

    # Send GET request to API
    response = requests.get(url, params=params)

    # Convert the response data to a JSON object
    data = response.json()

    # Get the weather icon ID
    icon_id = data['weather'][0]['icon']

    # Get the weather icon image from the URL and create an ImageTk object
    icon_image = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(icon_id), stream=True).raw))

    # Display the weather icon image
    icon_label.configure(image=icon_image)
    

    # Get the location name
    location_name = f"{data['name']}, {data['sys']['country']}"

    # Display the location name
    location_label.configure(text=location_name)

    # Get the temperature in Celsius
    temp_celsius = f"{int(data['main']['temp'] - 273.15)}°C"

    # Display the temperature
    temp_label.configure(text=temp_celsius)

    # Get the weather condition
    condition = data['weather'][0]['description']

    # Display the weather condition
    condition_label.configure(text=condition)


# Create the GUI window
app = Tk()
app.geometry('300x450')
app.title('Mert Can Hava Durumu')

# Create a text box for the user to enter a city name
city_entry = Entry(app, justify='center')
city_entry.grid(row=0, column=0, padx=18, pady=5, ipady=10)
city_entry.focus()

# Create a button to search for weather information
search_button = Button(app, text='Arama', font=('Arial', 15), command=search_weather)
search_button.grid(row=0, column=1, padx=20, ipady=10)

# Create a label to display the weather icon
icon_label = Label(app)
icon_label.grid(row=1, column=0, columnspan=2)

# Create a label to display the location name
location_label = Label(app, font=('Arial', 40))
location_label.grid(row=2, column=0, columnspan=2)

# Create a label to display the temperature
temp_label = Label(app, font=('Arial', 50, 'bold'))
temp_label.grid(row=3, column=0, columnspan=2)

# Create a label to display the weather condition
condition_label = Label(app, font=('Arial', 20))
condition_label.grid(row=4, column=0, columnspan=2)

# Start the main event loop
app.mainloop()