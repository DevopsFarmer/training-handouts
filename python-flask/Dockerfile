# start from a base image
FROM python:3.12


# base location in container
WORKDIR /app


# copy code
COPY . /app

# install depencies
RUN pip install -r requirements.txt


# start the application

CMD ["python", "app.py"]
