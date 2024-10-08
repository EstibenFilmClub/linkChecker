FROM python:slim-bullseye

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip

WORKDIR /usr/src/applink
COPY . .

RUN pip install -r requirements.txt
RUN playwright install
RUN apt-get install -y libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxcb1 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2

# RUN playwright install-deps
RUN echo "---- Instalacion finalizada ----"

# EXPOSE 5000

# ENTRYPOINT [ "python main.py" ]
# CMD [ "python", "main.py" ]