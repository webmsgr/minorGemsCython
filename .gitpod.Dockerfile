FROM gitpod/workspace-full

USER root

# install llvm/clang
RUN apt-get update \
    && apt-get install -y llvm-9-dev clang-9 llvm-9 libclang9-dev l\
    && git clone https://github.com/CastXML/CastXML \
    && cd CastXML \
    && cmake . \
    && make \
    && make install \
    && cd .. \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN apt-get update \
#    && apt-get install -y bastet \
#    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
