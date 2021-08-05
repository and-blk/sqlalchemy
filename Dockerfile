FROM python:3.8-buster

WORKDIR /opt/
ADD . .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-u", "db.py" ]