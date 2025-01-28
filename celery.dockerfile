# ---- Base Stage ----
FROM python:3.11.11-slim-bookworm as base

ARG USERNAME=non-root
ARG USER_UID=1000
ARG USER_GID=$USER_UID
WORKDIR /home/$USERNAME/app
ARG GDRIVE_CREDENTIALS_DATA=$GDRIVE_CREDENTIALS_DATA

ARG ENVIRONMENT
# Ensure the environment variable is valid
RUN if [ "$ENVIRONMENT" != "prod" && "$ENVIRONMENT" != "dev" ]; then echo "ENVIRONMENT must be either 'prod' or 'dev'"; exit 1; fi

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a non-root user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# ---- Base Stage ----
FROM base as builder

ENV TZ=Europe
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy dirs
COPY src/shared_scripts/schema ./src/api/schema
COPY src/celery_worker ./src/celery_worker
COPY src/shared_scripts/schema ./celery_worker/schema
RUN mkdir -p src/log

# install package
RUN --mount=type=cache,target=/root/.cache/pip \
    python3.11 -m pip install -r src/celery_worker/requirements.txt --target=/usr/lib/python3/dist-packages

# ---- Final Stage ----
FROM base as final

# Copy installed packages from builder stage
COPY --from=builder --chown=$USER_UID:$USER_GID /usr/lib/python3/dist-packages /home/$USERNAME/python-packages

# Copy project from builder stage
COPY --from=builder --chown=$USER_UID:$USER_GID /home/$USERNAME/app/src/celery_worker /home/$USERNAME/app/src/celery_worker
COPY --from=builder --chown=$USER_UID:$USER_GID /home/$USERNAME/app/src/log /home/$USERNAME/app/src/log

# Set the environment variable PYTHONUSERBASE to use the copied packages
ENV PYTHONUSERBASE=/home/$USERNAME/python-packages
ENV PATH="/home/${USERNAME}/python-packages/bin:${PATH}"
ENV PYTHONPATH="/home/$USERNAME/python-packages:$PYTHONPATH"

# Prepare environment specific prestart script
RUN chown -R non-root:non-root /home/non-root/app/src/log
RUN chmod u+x "src/celery_worker/prestart.${ENVIRONMENT}.sh"

USER $USERNAME

ENTRYPOINT ["/bin/bash", "src/celery_worker/prestart.${ENVIRONMENT}.sh"]
