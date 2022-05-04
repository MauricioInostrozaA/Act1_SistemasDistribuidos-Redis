From python:3.10.4

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE 3000

CMD ["python", "src/app.py"]
