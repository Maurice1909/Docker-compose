🐳 Multi-Container Web Application with Docker Compose
A demonstration of container orchestration, service networking, and data persistence using a simple Python Flask application and Redis database.

📝 Overview
This project simulates a basic web application environment requiring both an application layer and a data store. The entire stack is containerized and managed using Docker Compose, highlighting key concepts necessary for deploying real-world microservices.

✨ Features
Multi-Container Orchestration: Deploys two distinct services (web app and database) defined in a single docker-compose.yml.

Service Discovery: The Flask application successfully connects to the Redis container using the service name defined in the Compose file.

Data Persistence: Uses Docker Volumes to ensure the visit count data in Redis persists even after the containers are stopped and restarted.

Configuration Management: The Flask application reads critical connection details (Redis host) from environment variables passed through Docker Compose, ensuring portability and security.

Scalability Demonstration: The web service is configured to be easily scaled, demonstrating inherent load balancing and resilience within the Docker Compose network.
