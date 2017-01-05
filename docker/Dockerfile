FROM python:2.7

MAINTAINER Ralph Brecheisen <ralph.brecheisen@gmail.com>

COPY ./sshd_config ./ssh_install.sh /root/

ARG AUTH_KEY

RUN /root/ssh_install.sh