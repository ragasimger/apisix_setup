FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Python script
CMD ["python", "route_register.py"]
