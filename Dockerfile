FROM python:3.11

ARG USERNAME
ARG PASSWORD

COPY bot.py .

RUN python bot.py $USERNAME $PASSWORD