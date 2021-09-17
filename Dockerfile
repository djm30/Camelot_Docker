FROM python:3.8


RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN apt install -y ghostscript

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app/


CMD ["python", "app/main.py"]