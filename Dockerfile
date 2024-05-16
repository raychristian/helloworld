# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables for unbuffered mode (useful for logs)
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container
COPY ./requirements.txt /requirements.txt

# Update the package list, install necessary dependencies, and Python packages
RUN apt-get update -y && \
    # Install PostgreSQL client development files and compiler
    apt-get install -y libpq-dev gcc && \
    # Upgrade all packages
    apt-get upgrade -y && \
    # Upgrade pip
    pip install --upgrade pip && \
    # Install Python dependencies from requirements.txt
    pip install -r requirements.txt && \
    # Install psycopg2 for PostgreSQL support
    pip install psycopg2==2.9.7

# Copy the current directory contents into the container at /app
COPY . /app 

# Set the working directory in the container
WORKDIR /app

# Expose the port that Flask will run on
EXPOSE 5000

# Define the default command to run when starting the container
CMD ["flask", "run", "--host=0.0.0.0"]
