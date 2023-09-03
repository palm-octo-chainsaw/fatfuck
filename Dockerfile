FROM python:3.11

ARG USERNAME
ARG PASSWORD

COPY bot.py .

RUN pip install --upgrade pip
RUN pip install instabot

ENTRYPOINT python bot.py "${USERNAME?UsernameNotSet}" "${PASSWORD?PasswordNotSet}"