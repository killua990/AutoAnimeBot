FROM python

RUN apt update && apt install -y libsm6 libxext6 libfontconfig1 libxrender1 libgl1-mesa-glx ffmpeg

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD python3 -m main
