FROM python:3.8-alpine
LABEL maintainer 'Rodrigo Mendes <rcmendes80@gmail.com>'

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py ./

CMD [ "python", "app.py" ]

# ENTRYPOINT [ "/usr/local/bin/python" ]