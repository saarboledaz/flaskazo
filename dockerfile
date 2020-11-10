#Create a ubuntu base image with python 3 installed.
FROM python:3

#Set the working directory
WORKDIR /usr/src/flaskazo

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install flask
RUN pip3 install flask_cors
RUN mkdir /files/assets/
RUN mkdir /files/authors/
RUN mv /usr/src/flaskazo/image.jpg /files/assets/image.jpg

#Expose the required port
EXPOSE 5000

#Run the command
#CMD [“python3”, “./app.py”]
CMD ["flask run --host=0.0.0.0"]