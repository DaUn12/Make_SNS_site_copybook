FROM python:3.9.0

WORKDIR /home/

RUN echo 'asdsdadsd'

RUN git clone https://github.com/DaUn12/goHome-first-.git
    # 깃 주소복붙하여 여기다 옮김

WORKDIR /home/goHome-first-/
    # 깃 이름을 따와야함

RUN echo "SECRET_KEY=django-insecure-6bldunix=$y%a35v0k8!l6&li$76tu8@sp##g3dz2urklk2039" > .env
    # .env 파일에서 따옴

RUN pip install -r requirements.txt
    # 얼린파일을 다시 설치함

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000
    # 사용할 포트

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=goHome.settings.deploy && python manage.py migrate --settings=goHome.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=goHome.settings.deploy goHome.wsgi --bind 0.0.0.0:8000"]
# 구니콘, 메인파일이름.wsgi, 어떤ip에요청을받을지