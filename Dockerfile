# Use the specified base image
FROM public.ecr.aws/lambda/python:3.11

# Install system packages for building LightGBM
RUN yum install -y gcc-c++ make cmake3 && \
    ln -s /usr/bin/cmake3 /usr/bin/cmake

# Set the working directory
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the Python requirements file
COPY requirements.txt .

# Install Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Lambda function code
COPY lambda_function.py .

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["lambda_function.lambda_handler"]
