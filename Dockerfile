FROM python:3.10-alpine

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/BrunoRimbanoJunior/WebAppConversorPDF.git

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]