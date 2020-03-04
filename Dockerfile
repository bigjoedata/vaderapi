#choose from https://hub.docker.com/_/python here. Alpine is slimmer, but is notoriously tricky for Python, so you probably want to use a buster or slim build to avoid headaches
FROM python:3.7.6-slim-buster

# Make directories as needed and set the workdir where the files will run.
RUN mkdir -p /home/vader/app
WORKDIR /home/vader

LABEL maintainer="jb"

# Copy and install requirements
#COPY requirements.txt /home/project/app

#freezing PIP to requirements.txt is best practices to prevent incompatibility later. I live dangerously and just install. no cache dir option keeps it slim
#RUN pip install --no-cache-dir -r requirements.txt

#This installs the latest from PIP
RUN pip install --no-cache-dir fastapi pydantic uvicorn gunicorn loguru vaderSentiment requests

# Copy contents from your local to your docker container
COPY ./app/main.py ./app

#EXPOSE 8001

#Run this if no web interaction required
#CMD ["python", "app/main.py"]

#Change the port here to reflect the Python code
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "24601"]
