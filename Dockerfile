FROM alpine

RUN apk add python3

RUN apk add py-pip

RUN pip install flask

COPY main.py .

CMD ["python3","main.py"]
