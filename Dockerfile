# base image  
FROM python:3
WORKDIR /app
# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory.
COPY . ./
# run this command to install all dependencies  
RUN pip install django~=3.1.0
# port where the Django app runs  *.py
EXPOSE 8000  
# start server  
CMD python3 manage.py runserver 0:8000