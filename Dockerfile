FROM public.ecr.aws/lambda/python:3.10

COPY ./requirements.txt ./
COPY ./user ${LAMBDA_TASK_ROOT}/user

RUN pip install -r requirements.txt

CMD ["user.adapters.controllers.create_user_controller.create_user"]
