import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card } from 'react-bootstrap';

const Weather = () => {
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchWeatherData = async () => {
      const city = "Madurai";
      const apiKey = "333a8faa57184ef5534e17ed15f5d342";
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
    <Card>
      <Card.Title>Weather Report</Card.Title>
      <Card.Text>Temperature: {weatherData.main.temp}°C</Card.Text>
      <Card.Text>Humidity: {weatherData.main.humidity}%</Card.Text>
      <Card.Text>Wind Speed: {weatherData.wind.speed}m/s</Card.Text>
    </Card>
  );  
};

export default Weather;
