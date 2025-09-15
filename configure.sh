# Example for API
aws ecr create-repository --repository-name api
docker build -t api:latest poc/services/api
docker tag api:latest <account>.dkr.ecr.<region>.amazonaws.com/api:latest
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
docker push <account>.dkr.ecr.<region>.amazonaws.com/api:latest
# repeat for forecast and worker

# Apply manifests
kubectl apply -f poc/k8s/namespace.yaml
kubectl apply -f poc/k8s/redis.yaml
kubectl apply -f poc/k8s/api-deployment.yaml
kubectl apply -f poc/k8s/forecast-deployment.yaml
kubectl apply -f poc/k8s/worker-deployment.yaml

kubectl apply -f poc/k8s/ingress.yaml


docker build -t retail .
docker tag retail:latest <account>.dkr.ecr.<region>.amazonaws.com/retail:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/retail:latest

