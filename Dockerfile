# Use a slim version of Python 3.11 as the base image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    autoconf \
    automake \
    curl \
    libtool \
    libyaml-dev \
    make \
    pkg-config \
    texinfo \
    python3-louis \
    liblouis-dev \
    liblouis20 \
    python3-pip \
    python3-distutils \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*

# Add the liblouis directory from the host to /usr/src/liblouis in the container
ADD liblouis /usr/src/liblouis

# Set the working directory to /usr/src/liblouis
WORKDIR /usr/src/liblouis

# Run the setup commands for liblouis
RUN ./autogen.sh && ./configure --enable-ucs4 && make && make install && ldconfig

# Change to the python bindings directory
WORKDIR /usr/src/liblouis/python

# Install the python bindings for liblouis
RUN python3 setup.py install

# Change back to the /app directory
WORKDIR /app

# Copy the requirements.txt file into the /app directory
COPY requirements.txt /app/

# Install the Python dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend application into the /app directory
COPY . /app

# Set environment variables
ENV MONGODB_CLIENT="mongodb+srv://tactales-admin:MZb07PhygCinMLPl@tactales-v3.hq8hdjn.mongodb.net/?retryWrites=true&w.majority&appName=tactales-v3"
ENV SECRET_KEY="fh_55a&s$cl$kx$b-6a7d1c&m0w)trxlb#58nhxtz9k82rp#6$"
ENV ALGORITHM="HS256"
ENV ACCESS_TOKEN_EXPIRY=30
ENV REFRESH_TOKEN_EXPIRY=24



# Expose port 8080 for the application
EXPOSE 8080

# The command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--app-dir", "/app/app"]


