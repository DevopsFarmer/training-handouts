## Step-by-Step Guide: Creating and Running a Flask App

### Step 1: Set Up Your Flask Environment

#### 1.1 Install Python
- **Download and install Python** from [python.org](https://www.python.org/downloads/).

#### 1.2 Create a Virtual Environment
1. **Open your terminal or command prompt.**
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment**:
   ```bash
     source venv/bin/activate
     ```

#### 1.3 Install Flask
1. **Install Flask using pip**:
   ```bash
   pip install Flask
   ```

### Step 2: Create a Simple Flask App

#### 2.1 Create `app.py`
1. **Create a new directory for your project** and navigate into it:
   ```bash
   mkdir my_flask_app
   cd my_flask_app
   ```
2. **Create a file named `app.py`** with the following content:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

### Step 3: Run the Flask App Locally

#### 3.1 Run the Flask App
1. **Run the app**:
   ```bash
   python app.py
   ```
2. **Verify the app is running**:
   - Open a web browser and go to `http://localhost:5000`.
   - You should see the message "Hello, World!".



## Docker Training Handout: Basic Docker Commands

### Objective:
Learn fundamental Docker commands for managing containers, images, and more.

---

### Docker Installation
1. **Install Docker**:
   - Follow the instructions from the Docker documentation: [Get Docker](https://docs.docker.com/get-docker/).

---

### Basic Docker Commands

#### 1. Docker Version and Info
1. **Check Docker version**:
   ```bash
   docker --version
   ```
2. **Display system-wide information**:
   ```bash
   docker info
   ```

#### 2. Working with Docker Images
1. **List all Docker images**:
   ```bash
   docker images
   ```
2. **Pull an image from Docker Hub**:
   ```bash
   docker pull image_name
   ```
   - Example: Pull the latest Python image:
     ```bash
     docker pull python:latest
     ```
3. **Build an image from a Dockerfile**:
   ```bash
   docker build -t image_name:tag .
   ```
   - Example: Build an image named `flask-app`:
     ```bash
     docker build -t flask-app .
     ```
4. **Remove a Docker image**:
   ```bash
   docker rmi image_name:tag
   ```
   - Example: Remove the `flask-app` image:
     ```bash
     docker rmi flask-app
     ```

#### 3. Working with Docker Containers
1. **List all running containers**:
   ```bash
   docker ps
   ```
2. **List all containers (including stopped ones)**:
   ```bash
   docker ps -a
   ```
3. **Run a container from an image**:
   ```bash
   docker run -d -p host_port:container_port image_name
   ```
   - Example: Run the `flask-app` container:
     ```bash
     docker run -d -p 5000:5000 flask-app
     ```
4. **Stop a running container**:
   ```bash
   docker stop container_id
   ```
5. **Start a stopped container**:
   ```bash
   docker start container_id
   ```
6. **Remove a container**:
   ```bash
   docker rm container_id
   ```
7. **View logs from a container**:
   ```bash
   docker logs container_id
   ```

#### 4. Docker Networking
1. **List all networks**:
   ```bash
   docker network ls
   ```
2. **Inspect a network**:
   ```bash
   docker network inspect network_name
   ```
3. **Create a new network**:
   ```bash
   docker network create network_name
   ```
4. **Connect a container to a network**:
   ```bash
   docker network connect network_name container_id
   ```
5. **Disconnect a container from a network**:
   ```bash
   docker network disconnect network_name container_id
   ```

#### 5. Docker Volumes
1. **List all volumes**:
   ```bash
   docker volume ls
   ```
2. **Create a volume**:
   ```bash
   docker volume create volume_name
   ```
3. **Inspect a volume**:
   ```bash
   docker volume inspect volume_name
   ```
4. **Remove a volume**:
   ```bash
   docker volume rm volume_name
   ```

---

### Example Workflow: Dockerizing a Flask App

1. **Create and navigate to your project directory**:
   ```bash
   mkdir my_flask_app
   cd my_flask_app
   ```
2. **Create `app.py` with a simple Flask application**:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```
3. **Create a `Dockerfile`**:
   ```Dockerfile
   # Use the official Python image from the Docker Hub
   FROM python:3.9-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install any needed packages specified in requirements.txt
   RUN pip install flask

   # Make port 5000 available to the world outside this container
   EXPOSE 5000

   # Define environment variable
   ENV NAME World

   # Run app.py when the container launches
   CMD ["python", "app.py"]
   ```
4. **Build the Docker image**:
   ```bash
   docker build -t flask-app .
   ```
5. **Run the Docker container**:
   ```bash
   docker run -d -p 5000:5000 flask-app
   ```
6. **Verify the app is running** by accessing `http://localhost:5000`.
