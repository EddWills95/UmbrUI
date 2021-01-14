FROM aarondewes/pygame-grpc-base:main
WORKDIR /app

COPY . .
# RUN ["python3", "--version"]
CMD ["python3", "-u", "ui.py"]
