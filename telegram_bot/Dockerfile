FROM python:3.11-slim

RUN mkdir /bot

WORKDIR /bot
COPY requirements.txt /bot
RUN pip install --upgrade pip
RUN pip install -r /bot/requirements.txt --no-cache-dir

COPY . .

CMD [ "python", "main.py" ]