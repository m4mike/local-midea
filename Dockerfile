# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
ADD app.py .
EXPOSE 443
CMD [ "python", "app.py"]
