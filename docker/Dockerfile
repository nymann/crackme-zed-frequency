FROM debian:bookworm AS base-image
RUN apt-get update && useradd -m --system crackme
RUN apt-get install --assume-yes --no-install-recommends python3

FROM base-image AS compile-image
RUN apt-get install -y --no-install-recommends make git python3-pip &&\
    pip install --upgrade pip

WORKDIR /usr/app
COPY . .
RUN make install

FROM base-image AS production-image
COPY crackme_bin/ZED-Frequency.bin /usr/local/bin/ZED-Frequency.bin
RUN chmod 751 /usr/local/bin/ZED-Frequency.bin
WORKDIR /home/crackme/
# RUN python3 -m site # if this ever breaks to get dist-packages folder.
COPY --from=compile-image /usr/local/lib/python3.9/dist-packages/ /usr/local/lib/python3.9/dist-packages/
COPY --from=compile-image /usr/local/bin/crackme_zed_frequency /usr/local/bin/
COPY scripts/generate_key_and_run_binary /usr/local/bin/

USER crackme
CMD generate_key_and_run_binary
