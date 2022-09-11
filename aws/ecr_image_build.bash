export AWS_REGION=us-east-1
export AWS_ACCOUNT_ID=123456789
export IMAGE_NAME=dataflowops
export IMAGE_TAG=latest

docker build -t $IMAGE_NAME .
# to check the files in the container
docker run --rm -it dataflowops

aws ecr create-repository --repository-name $IMAGE_NAME --region $AWS_REGION
docker tag "$IMAGE_NAME":"$IMAGE_TAG" "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$IMAGE_NAME":"$IMAGE_TAG"
aws ecr get-login-password | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
docker push "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$IMAGE_NAME":"$IMAGE_TAG"

