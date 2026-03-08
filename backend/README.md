# Backend Setup Instructions

## Environment Variables
To run the backend, you will need to configure the following environment variables:
- `PORT`: The port on which the server will run (default is 3000).
- `DB_URI`: Connection string for your MongoDB database.
- `JWT_SECRET`: Secret key for JWT authentication.

## Running the Server
1. Clone the repository:
   ```bash
   git clone https://github.com/Linuxnapratica/esp32-dht22-iot-monitor.git
   cd esp32-dht22-iot-monitor
   ```
2. Install the dependencies:
   ```bash
   npm install
   ```
3. Start the server:
   ```bash
   npm start
   ```
   The server will be running on the configured port.

## API Documentation
- **GET /api/data**: Retrieve the latest sensor data.
- **POST /api/data**: Submit new sensor data.
- **GET /api/status**: Check the server status.

Make sure to check the respective route documentation for required parameters and response formats.