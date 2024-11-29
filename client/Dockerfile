FROM python:3.8-slim

WORKDIR /app

COPY client.py /app/

RUN pip install requests

ENV PYTHONUNBUFFERED=1  

CMD ["python", "client.py"]
