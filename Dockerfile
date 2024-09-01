# Dockerfile blueprint for building images
# Docker Image template for running containers
# Container running process where packed project is running

# Base image to be used for the build (python 3.12 in this case)
FROM python:3.12

# Add local main .py to the build
ADD main.py .

# Pip install necessary libraries
RUN pip install requests beautifulsoup4

# Run main.py when the container launches
CMD ["python", "./main.py"]