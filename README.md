# YADTQ (Yet Another Distributed Task Queue)

A distributed task queue system built with Kafka and Redis, offering seamless scalability and robust fault tolerance.

## Key Features
- Distributed task processing with multiple workers
- Real-time task status tracking
- Built-in fault tolerance
- Kafka-powered message queuing
- Simple CLI interface

---

## Prerequisites
Ensure you have the following installed before running the system:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Steps to Run the System

### 1. Build and Start the Docker Environment
Navigate to the project directory and build the Docker containers:
```sh
cd /your-path/YADTQ

docker compose up --build
```
Verify that the containers are running:
```sh
docker ps
```

### 2. Scale Up the Worker Containers
To scale the worker containers, run the following command:
```sh
cd /your-path/YADTQ

docker-compose up --scale worker=3
```
Re-check the status of running containers:
```sh
docker ps
```

### 3. Run the Task Queue Coordinator
To run the `yadtq.py` script that coordinates task processing inside the client container, run:
```sh
docker exec -it yadtq-client-1 python yadtq.py
```

### 4. Execute Scripts in Worker Containers
To run the `yadtq.py` script in each worker container:
```sh
docker exec -it yadtq-worker-1 python yadtq.py

docker exec -it yadtq-worker-2 python yadtq.py

docker exec -it yadtq-worker-3 python yadtq.py
```

### 5. Run the Client Script for Interactions
To execute `client.py` for interacting with the YADTQ system, run:
```sh
docker exec -it yadtq-client-1 python client.py
```

---

## Task Input Format
The client accepts mathematical operations using the following format:
```sh
OPERATION OPERAND1 OPERAND2
```

### Example Inputs
```sh
ADD 2 3      # Addition
SUB 5 2      # Subtraction
MUL 4 5      # Multiplication
```

---

## Available Commands
- `Enter` - Submit a new task to the queue
- `Show-Tasks` - Display all submitted tasks and their current status
- `View [taskId]` - Check the status of a specific task by ID
- `Reset` - Clear all tasks from the queue
- `Exit` - Terminate the client session

---

## Task States
- `queued` - Task awaiting processing.
- `in-progress` - Task under processing.
- `completed` - Task finished with result.
- `failed` - Task failed.

---

## Architecture Components
- **Client Service** - Task submission interface
- **Worker Services** - Task processors
- **Redis** - Task state management
- **Kafka** - Message distribution
- **Zookeeper** - Cluster coordination

---

## Troubleshooting
### Check logs if a container fails to start:
```sh
docker logs <container_name>
```
### Stop all running containers:
```sh
docker-compose down
```

---

## Notes
- Modify `docker-compose.yml` as needed to change service configurations.
- Ensure Kafka and Redis services are running correctly before processing tasks.

