# Dockerfile

# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Step 5: Copy the current directory contents into the container
COPY . /app/

# Step 6: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 7: Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
