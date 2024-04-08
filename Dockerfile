# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the files needed for pip install first
# This leverages Docker cache to speed up builds if dependencies don't change
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define any environment variable your application requires
# ENV DATABASE_URL postgresql://user:password@hostname:port/dbname
# ENV SECRET_KEY your_secret_key_here
# ENV FLASK_ENV production
# ENV PORT 5000

# Run app.py when the container launches
CMD ["python", "./app/main.py"]
