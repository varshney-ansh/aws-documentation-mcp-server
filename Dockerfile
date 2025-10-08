# Use AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.11

# Copy dependency files
COPY uv-requirements.txt requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r uv-requirements.txt && pip install -r requirements.txt

# Copy all source code
COPY . ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD ["main.lambda_handler"]