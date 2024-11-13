# MBTA-Web-App-Project (Hatton Tong, Amy Meng)

## 1. Project Overview 

This project is a web application designed to help users locate the nearest MBTA (Massachusetts Bay Transportation Authority) stop based on a specified location within the Greater Boston area. Users can enter an address or place name, choose their preferred transportation type (e.g., subway, bus, or commuter rail), and receive information about the nearest stop, including whether it is wheelchair accessible. Additionally, we enhanced user engagement by integrating real-time weather data using the OpenWeatherMap API, displaying current weather conditions at the selected location. 

Key features: 
- **Geolocation Services**: Uses Mapbox’s Geocoding API to convert place names into latitude and longitude coordinates. 
- **Nearest MBTA Stop**: Retrieves MBTA stop data based on geolocation, filtered by transportation type, and displays accessibility status. 
- **Real-Time Weather Data**: Shows current weather information based on user location. 
- **User-Friendly Input and Output**: Interactive prompts that make the app easy to use and informative. 

## 2. Reflection

### Development Process 
The development process involved planning, scoping, and development with a strong emphasis on testing and debugging. Early on, we defined the project scope to meet the base requirements, then identified key enhancements like adding transportation options and real-time weather data. Developing with APIs presented some challenges, especially around handling different responses and debugging authorization errors, but consistent testing and logging helped us pinpoint and resolve issues. 

One major challenge was the integration of multiple APIs with varying formats and requirements. When Amy completed her section and Hatton began working on the app.py file, we found that Amy's saved APIs did not work on Hatton's computer. Therefore, we had to find a new set of all APIs for Hatton in order to move on.

### Teamwork Division
In this project, we divided the work into two main sections to maximize efficiency and play to our strengths. Amy focused on developing the MBTA_helper module, while Hatton concentrated on the app.py file, which serves as the main driver for the application. Once the initial HTML came to shape, we collaborated together to refine the website, adding background photos and making the website more visually pleasing. 

One major challenge of collaborating with a partner was ensuring that we always worked with the most updated code, as every change required creating and merging pull requests. This made clear communication essential to avoid conflicts or outdated code. Before starting new lines, we ensured we pulled the latest version and regularly checked in to stay aligned on progress. While this process occasionally slowed us down, it ultimately improved code quality and streamlined collaboration.

### Learning Perspective
This project taught us several valuable lessons, both technical and collaborative. We gained deeper insight into integrating multiple APIs, managing their responses, and handling potential issues like authorization errors and rate limits. Debugging and error handling became a core part of the process. We also found the experience with AI tools was particularly impactful. They significantly enhanced our efficiency and understanding by providing quick, targeted suggestions for specific problems, such as resolving the socket error with the code snippet on Hatton's app.py code: 

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

![Socket Error](Socket%20Error.jpg)

Moreover, Amy also utilized ChatGPT to solve the Index Error, highlighting both teammates' use of generative AI as a tool for debugging and error fixing. 

![Index Error](Index%20Error.png)
