
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências de sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       git \
       curl \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências do projeto globalmente (durante o build)
# O build context está configurado para o diretório pai, assim podemos copiar requirements.txt
COPY ../requirements.txt /tmp/requirements.txt
COPY ../requirements-dev.txt /tmp/requirements-dev.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt \
    && python -m pip install --no-cache-dir -r /tmp/requirements-dev.txt \
    && rm /tmp/requirements.txt /tmp/requirements-dev.txt

# Criar usuário não-root (vscode) para desenvolvimento
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000
RUN groupadd --gid ${USER_GID} ${USERNAME} || true \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} || true

USER ${USERNAME}
WORKDIR /home/${USERNAME}/workspace

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
