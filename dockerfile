# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /traders

# Set the working directory to /music_service
WORKDIR /traders

# Copy the current directory contents into the container at /music_service
ADD . /traders/

RUN ls
# Install any needed packages specified in requirements.txt
RUN pip install -r requirment.txt

EXPOSE 8080

RUN python manage.py collectstatic --noinput

RUN celery -A traders worker -l info --detach


CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT