# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt file first
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Change directory to IntelliPurchase
WORKDIR /app/IntelliPurchase

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME intellipurchase

# Run gunicorn when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:8000", "IntelliPurchase.wsgi:application"]
