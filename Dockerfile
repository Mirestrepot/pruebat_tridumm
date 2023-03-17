FROM python:3.9-alpine
ENV PYTHONUNBOFFERED 1

WORKDIR /pruebat_tridumm
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:80
# docker build -t pruebat_tridumm .