FROM python:3.6
EXPOSE 5000
ADD . /app
WORKDIR /app


ENV FLASK_APP app.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

RUN pip install -r requirements.txt
CMD python app.py