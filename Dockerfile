FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py

ENV PORT 80
EXPOSE 80

CMD ["python3", "main.py"]