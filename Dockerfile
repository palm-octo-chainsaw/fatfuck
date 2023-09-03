FROM python:3.11

ARG USERNAME
ARG PASSWORD

COPY bot.py .

RUN pip install --upgrade pip
RUN pip install instabot
RUN echo "${USERNAME} and ${PASSWORD}"

ENTRYPOINT python bot.py "${USERNAME?UsernameNotSet}" "${PASSWORD?PasswordNotSet}"