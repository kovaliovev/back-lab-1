# Backend Lab #1

You can check deployed project using the link: https://back-lab-1-z5wo.onrender.com/healthcheck   
Or run it locally by following instructions

## Install
- Docker
- Docker-compose (optional)

## Clone the Repository
```bash
git clone https://github.com/kovaliovev/back-lab-1.git
```
```bash
cd back-lab-1
```

## Build and Run with Docker
```docker
docker build . -t healthcheck:latest
```
```docker
docker run -it --rm -e PORT=8080 -p 8080:8080 healthcheck:latest
```

## Using Docker Compose (Optional)
```docker
docker-compose build
```
```docker
docker-compose up
```
