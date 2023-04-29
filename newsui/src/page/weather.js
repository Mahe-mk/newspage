// import React from 'react'

// function Weather() {
//   return (
//     <div>
//     <main className="container mt-3 mb-5">
//         <h3 className="border-bottom pb-1 my-4">Weather Report</h3>
//         <p>Temperature:weather_data.main.temp °C</p>
//         <p>Humidity:weather_data.main.humidity %</p>
//         <p>Wind Speed:weather_data.wind.speed m/s</p>
//     </main>
//     </div>
//   )
// }
// export default Weather

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Weather = () => {
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchWeatherData = async () => {
      const city = "Madurai";
      const apiKey = "333a8faa57184ef5534e17ed15f5d342";
      // const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;
      const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

      try {
        const response = await axios.get(apiUrl);
        setWeatherData(response.data);
        setLoading(false);
      } catch (error) {
        console.error(error);
      }
    };

    fetchWeatherData();
  }, []);
  if (loading) {
    return <div>Loading weather data...</div>;
  }
  return (
    <div>
      <h3>Weather Report</h3>
      <p>Temperature: {weatherData.main.temp}°C</p>
      <p>Humidity: {weatherData.main.humidity}%</p>
      <p>Wind Speed: {weatherData.wind.speed}m/s</p>
    </div>
  );
};

export default Weather;
