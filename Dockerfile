# getting base image python3 linux base image from docker
FROM python:3.8-slim-buster

# working directory is same as current/copied directory
WORKDIR /app

# copying all files from current directory
COPY . /app

#updating all the packages before doing deployment
RUN apt update -y && apt install awscli -y

# Install dependencies
RUN pip install -r requirements.txt

# Run the application:
CMD ["python3", "app.py"]