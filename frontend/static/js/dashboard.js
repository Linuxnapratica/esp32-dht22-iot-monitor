// dashboard.js

// Function to fetch sensor data from API
async function fetchSensorData() {
    try {
        const response = await fetch('https://api.example.com/sensor-data'); // Replace with your API endpoint
        const data = await response.json();

        // Update dashboard with the sensor data
        updateDashboard(data);
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }
}

// Function to update dashboard with new data
function updateDashboard(data) {
    // Assuming data has a structure for temperature and humidity
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');

    temperatureElement.textContent = `Temperature: ${data.temperature} °C`;
    humidityElement.textContent = `Humidity: ${data.humidity} %`;
}

// Refresh the data every 5 seconds
setInterval(fetchSensorData, 5000);

// Initial fetch when page loads
fetchSensorData();