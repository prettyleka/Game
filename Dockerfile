# Use an official Python runtime as a parent image
FROM moditamam/selenium:python3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
# Make port 5000 available to services on the same docker network
EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]