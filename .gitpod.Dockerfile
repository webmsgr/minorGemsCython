FROM gitpod/workspace-full

USER root

# install llvm/clang
RUN apt-get update \
    && apt-get install llvm clang \
    && git clone https://github.com/CastXML/CastXML CastXML \
    && cd CastXML \
    && cmake . 
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN apt-get update \
#    && apt-get install -y bastet \
#    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
