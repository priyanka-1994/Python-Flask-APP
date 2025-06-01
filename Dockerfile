# base image
FROM python
# set the working directory
WORKDIR /app
# copy applicaton files
COPY . /app 
# Install dependencies
RUN pip install -r requirements.txt
# expose the Flask port
EXPOSE 5000
# run the flask app
CMD ["python","run.py"]

