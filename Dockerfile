#FROM python:3.10-slim-bullseye
FROM python:3.10

LABEL maintainer="someone@somewhere.smth"
ADD pipindex.py /app/
ADD requirements.txt /app/
ADD wheels/ /app/wheels/
WORKDIR /app/wheels

RUN pip download -r ../requirements.txt
RUN pip install --no-index --find-links=wheels/ -r requirements.txt

RUN rm -rf /app/wheels/
CMD ["python", "./pipindex.py"]
