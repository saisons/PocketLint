FROM gcr.io/distroless/python3:debug
SHELL ["/busybox/ash", "-c"]
COPY *.csv /app/
COPY *.py /app/
WORKDIR /app
ENTRYPOINT ["python3", "serve.py"]
