FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /commuters
WORKDIR /commuters

COPY requirements.txt /commuters/
RUN pip install -r requirements.txt
COPY . /commuters/
