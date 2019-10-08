FROM gitpod/workspace-full

USER root

# install llvm/clang
RUN apt-get update \
    && apt-get install -y llvm clang llvm-dev clang-dev \
    && git clone https://github.com/CastXML/CastXML CastXML \
    && cd CastXML \
    && cmake . \ 
    && make \
    && make install \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN apt-get update \
#    && apt-get install -y bastet \
#    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
