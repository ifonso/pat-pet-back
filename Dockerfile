FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV PSQL_HOST=$PSQL_HOST
ENV PSQL_PORT=$PSQL_PORT
ENV PSQL_DB=$PSQL_DB
ENV PSQL_USER=$PSQL_USER
ENV PSQL_PASS=$PSQL_PASS

# Run app.py when the container launches
CMD ["python", "main.py"]
