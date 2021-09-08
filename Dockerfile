FROM python:3.9.5-slim-buster

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py", "0.0.0.0:5000"]
