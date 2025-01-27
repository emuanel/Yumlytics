FROM python:3.11.11-slim-bookworm

ARG ENVIRONMENT
ARG USERNAME=non-root
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Ensure the environment variable is valid
RUN if [ "$ENVIRONMENT" != "prod" && "$ENVIRONMENT" != "dev" ]; then echo "ENVIRONMENT must be either 'prod' or 'dev'"; exit 1; fi
# RUN if [ "$ENVIRONMENT" != "prod" ] && [ "$ENVIRONMENT" != "dev" ]; then echo "ENVIRONMENT must be either 'prod' or 'dev'"; exit 1; fi
WORKDIR /home/$USERNAME/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a non-root user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Copy src directory which includes setup.py and MANIFEST.in
COPY src/ ./src/
RUN mkdir -p /home/non-root/app/src/log

# build and install package
RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install --upgrade pip \
    && cd src && python3 -m pip install -r requirements/requirements.txt

# Cleanup unnecessary files
RUN rm -rf build src/*.egg-info

# Prepare environment specific prestart script
RUN chown -R non-root:non-root /home/non-root/app/src/log
RUN chmod u+x "src/api/prestart.${ENVIRONMENT}.sh"

USER $USERNAME

ENTRYPOINT ["/bin/bash", "src/api/prestart.${ENVIRONMENT}.sh"]