FROM python:3.8.6-alpine3.12
LABEL maintainer="Sultanbek Beksultanov <sultanbek9899@gmail.com>"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache gcc postgresql-dev zlib-dev \
    libjpeg-turbo-dev gettext linux-headers m make \
    python3-dev   postgresql-client \
    && rm -rf /var/apt/list/*

WORKDIR /app

COPY requirements ./requirements/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/app/docker-entrypoint.sh"]
