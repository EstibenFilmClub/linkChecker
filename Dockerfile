FROM python:slim-bullseye

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip

WORKDIR /usr/src/applink
COPY . .

RUN pip install -r requirements.txt
RUN playwright install
RUN echo "---- Instalacion finalizada ----"

# EXPOSE 5000

# ENTRYPOINT [ "python main.py" ]
# CMD [ "python", "main.py" ]