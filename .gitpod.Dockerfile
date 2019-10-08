FROM gitpod/workspace-full

USER root

RUN apt-get update \
   && git clone https://github.com/llvm/llvm-project.git llvm \
   && cd llvm \
   && mkdir build && cd build \
   && cmake -DLLVM_ENABLE_PROJECTS=clang -G "Unix Makefiles" ../llvm \
   && make \
   && export PATH=$PATH:/llvm/llvm/build/bin \
   && cd ../.. \
   && git clone git://github.com/gccxml/gccxml.git \
   && cd gccxml \
   && mkdir gccxml-build && cd gccxml-build && cmake ../gccxml && make && make install
# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN apt-get update \
#    && apt-get install -y bastet \
#    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
