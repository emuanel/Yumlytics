# Use the official Nginx image from the Docker Hub
FROM nginx:stable

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy a new configuration file from the current directory
COPY src/nginx/nginx.conf /etc/nginx/conf.d/

# Expose port 80
EXPOSE 80

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]
