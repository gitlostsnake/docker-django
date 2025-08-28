# Docker Django Setup

This repository provides a quick way to set up a Django project using Docker.

---

## Getting Started

### 1. Clone the repository
```bash
cd /path/to/your/projects
git clone https://github.com/gitlostsnake/docker-django.git
cd docker-django
```

### 2. Run Docker
Make sure you have **Docker** installed and running.  
Then build and start the containers:
```bash
docker compose up --build
```

### - Then in a seperate terminal
cd /path/to/your/projects/docker-django

### 3. Apply migrations
Run database migrations inside the container:
```bash
docker compose exec web python manage.py migrate
```

### 4. Create a superuser
Set up an admin account for your project:
```bash
docker compose exec web python manage.py createsuperuser
```

---

## Start Building

- Begin with your **home page**.  
- **Account signup and login** are already implemented with the required backend functionality.  
- Only minimal frontend work is provided — extend and customize it as needed.  

---

## Notes

- Ensure Docker Desktop (or Docker Engine + Compose) is running before starting.  
- To stop the containers when done:
  ```bash
  docker compose down
  ```
