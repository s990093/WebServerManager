/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'http',
                hostname: '127.0.0.1',
                port: '8000',
            },
            {
                protocol: 'http',
                hostname: '49.213.238.75',
                port: '8000',
            },
            {
                protocol: 'http',
                hostname: '192.168.0.135',
                port: '3000',
            },
        ],
    },
    output: "standalone"
};

export default nextConfig;
