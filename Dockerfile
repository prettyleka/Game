# syntax=dockerfile/dockerfile:1
FROM moditamam/selenium:python3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
# Make port 5000 available to services on the same dockerfile network
EXPOSE 5000
ENV FLASK_APP=app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]