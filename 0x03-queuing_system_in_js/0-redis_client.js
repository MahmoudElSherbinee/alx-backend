import { createClient } from 'redis';

const connectToRedis = async () => {
    const client = createClient();

    client.on('error', (err) => {
        console.log('Redis client not connected to the server:', err);
    });

    await client.connect();

    client.on('connect', () => {
        console.log('Redis client connected to the server');
    });
};

connectToRedis();
