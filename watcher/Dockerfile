# Use the official Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver", "--noreload", "0.0.0.0:8000"]

# Expose the port the app will run on
EXPOSE 8000