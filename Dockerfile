FROM nightling/buildpack

RUN pip install https://github.com/embolalia/willie/archive/5.4.1.tar.gz \
	&& useradd -rmd /data willie \
	&& rm -rf /usr/share/*/.git ~/.cache

COPY willie/ /data
RUN chmod 7777 -R /data
USER willie
ENTRYPOINT ["willie"]
