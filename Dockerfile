#Dockerfile
FROM python:3.8
WORKDIR /app
RUN apt-get -y update  && apt-get install -y \
  python-dev-is-python3 \
  apt-utils \
  build-essential \
  python3-pip \
  uvicorn \
  nginx \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip \
  && pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]
