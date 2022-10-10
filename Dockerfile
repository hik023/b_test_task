# syntax=docker/dockerfile:1
FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt update -y && apt upgrade -y
RUN apt-get install build-essential python3-dev python-dev gcc -y
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN cd /app/
# RUN chmod +x docker-entrypoint.sh
COPY docker-entrypoint.sh /app/
RUN ["chmod", "+x", "/app/docker-entrypoint.sh"]
# ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
