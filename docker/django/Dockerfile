# ./docker/django/Dockerfile
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /backend
COPY ./backend/requirements.txt requirements.txt
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

COPY ./backend .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fuadmin.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
