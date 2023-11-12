FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD [ "uvicorn", "app.main:app" ]