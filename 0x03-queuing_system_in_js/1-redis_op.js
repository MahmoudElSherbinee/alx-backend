#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  
  // Now that we are connected, we can safely perform operations
  const schoolName = 'Holberton';
  
  displaySchoolValue(schoolName);
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');

  // Close the client after a short delay to ensure we get the outputs
  setTimeout(() => {
    client.quit(); // Close the Redis client
    console.log('Redis client closed.');
  }, 1000); // Adjust the delay as necessary
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply ? reply : 'No value found for:', schoolName);
  });
};
