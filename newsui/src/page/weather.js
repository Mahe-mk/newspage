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

import React, { useEffect, useState } from 'react';

function Weather() {
  const [WeatherData, setWeatherData] = useState(null);

  useEffect(() => {
    fetch('/weather')
      .then(response => response.json())
      .then(data => setWeatherData(data))
      .catch(error => console.log(error));
  }, []);
console.log("WeatherData",WeatherData);
  return (
    <div>
      {WeatherData && (
        <div>
          <h1>Weather in {WeatherData.name}</h1>
          <p>Temperature: {WeatherData.main.temp}</p>
          <p>Humidity: {WeatherData.main.humidity}</p>
          <p>Weather: {WeatherData.weather[0].main}</p>
        </div>
      )}
    </div>
  );
}
export default Weather;
