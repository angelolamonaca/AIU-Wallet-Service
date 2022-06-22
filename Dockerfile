# set base image (host OS)
FROM python:latest

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 3030
# command to run on container start
CMD [ "python", "./app.py" ]
