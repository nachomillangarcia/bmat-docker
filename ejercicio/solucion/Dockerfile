FROM python:3.6-slim

WORKDIR /src

LABEL maintainer="nachomillangarcia@gmail.com" 

EXPOSE 5000

ENV PYTHONUNBUFFERED=1 PATH=$PATH:/home/python/.local/bin

HEALTHCHECK --interval=30s --timeout=1s --start-period=60s --retries=3 CMD [ "curl", "-q", "localhost:5000/" ]

RUN groupadd --gid 1000 python && useradd -ms /bin/bash -g python -u 1000 python

COPY docker-entrypoint.sh .

RUN apt update && \
    apt --no-install-recommends install -y \
      libpq-dev \
      curl && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge --auto-remove && \
    apt-get clean

USER python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["python", "app.py"]
