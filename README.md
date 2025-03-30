YADTQ (Yet Another Distributed Task Queue)
A distributed task queue system built with Kafka and Redis, offering seamless scalability and robust fault tolerance.

Key Features
Distributed task processing with multiple workers
Real-time task status tracking
Built-in fault tolerance
Kafka-powered message queuing
Simple CLI interface
Supported Operations
ADD: Addition of two numbers
SUB: Subtraction of two numbers
MUL: Multiplication of two numbers
Prerequisites
Docker
Docker Compose
Steps to Run the System
1. Build and Start the Docker Environment
Navigate to the project directory and build the Docker containers:

cd /your-path/RR-Team-49-yadtq-yet-another-distributed-task-queue-/YADTQ
docker compose up --build
Verify that the containers are running:

docker ps
2. Scale Up the Worker Containers
To scale the worker containers, run the following:

cd /your-path/RR-Team-49-yadtq-yet-another-distributed-task-queue-/YADTQ
docker-compose up --scale worker=3
Re-check the status of running containers:

docker ps
3. Run the Task Queue Coordinator
To run the yadtq.py script that coordinates task processing inside the client container, run:

docker exec -it yadtq-client-1 python yadtq.py
4. Execute Scripts in Worker Containers
To run the yadtq.py script in each worker container:

docker exec -it yadtq-worker-1 python yadtq.py
docker exec -it yadtq-worker-2 python yadtq.py
docker exec -it yadtq-worker-3 python yadtq.py
5. Run the Client Script for Interactions
To execute client.py for interacting with the YADTQ system, run:

docker exec -it yadtq-client-1 python client.py
Notes
Modify docker-compose.yml as needed to change service configurations.
Troubleshooting
If any container fails to start, check the logs using:

docker logs <container_name>
To stop all running containers:

docker-compose down
Task Input Format
The client accepts mathematical operations using the following format:

OPERATION OPERAND1 OPERAND2

Example Inputs
Addition: ADD 2 3
Subtraction: SUB 5 2
Multiplication: MUL 4 5
Available Commands
Enter: Submit a new task to the queue
Show-Tasks: Display all submitted tasks and their current status
View [taskId]: Check the status of a specific task by ID
Reset: Clear all tasks from the queue
Exit: Terminate the client session
Task States
queued: Task awaiting processing.
in-progress: Task under processing.
completed: Task finished with result.
failed: Task failed.
Architecture Components
Client Service: Task submission interface
Worker Services: Task processors
Redis: Task state management
Kafka: Message distribution
Zookeeper: Cluster coordination
