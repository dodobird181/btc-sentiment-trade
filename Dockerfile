FROM python:3.11-alpine

WORKDIR /app

# Install Poetry globally
RUN pip install poetry

# Create a virtual environment
RUN python -m venv /app/venv

# Ensure the virtual environment's pip and setuptools are up to date
RUN /app/venv/bin/pip install --upgrade pip setuptools wheel

# Copy the project files into the container
COPY . /app/

# Use the globally installed Poetry to install dependencies into the virtual environment
RUN poetry install --no-root

# Use the virtual environment's Python interpreter to run the application
CMD ["/app/venv/bin/python", "app.py"]
