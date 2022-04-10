FROM python:3.6
EXPOSE 8000

COPY ./app /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
