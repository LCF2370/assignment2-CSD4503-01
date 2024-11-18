# The base image
# Images developer can import thru hub.docker.com
FROM python:3.11-alpine

# To define the working directory
# i.e. root of the base image
WORKDIR /

# To copy the files to the working directory
# First dot copy everything
COPY requirements.txt .

# To install the dependency
RUN pip install -r requirements.txt

# To open the port 5000 in the container
EXPOSE  5000

# To run the app in the container
CMD  ["python", "main.py"]