FROM python:3.7-alpine

RUN  pip install tweepy

COPY upload_frame_of_the_day.py /root/

RUN mkdir /root/index/ && chown 999:999 /root/index/

RUN echo '0  4  *  *  *    python /root/upload_frame_of_the_day.py' > /etc/crontabs/root

#CMD ["python", "/root/upload_frame_of_the_day.py"]
CMD ["crond", "-l2", "-f"]
