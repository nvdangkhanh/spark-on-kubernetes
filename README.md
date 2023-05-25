# spark-on-kubernetes
1/ ./spark/bin/docker-image-tool.sh -r docker.io/erkansirin78 -t 3.1.1 -u 1000 -b java_image_tag=11-jre-slim -p ./spark/kubernetes/dockerfiles/spark/bindings/python/Dockerfile build
2/ docker build -t khanhdang/spark-k8s-app:1.0 .
3/ docker push khanhdang/spark-k8s-app:1.0
4/ helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
5/ helm install my-release spark-operator/spark-operator --namespace spark-operator --create-namespace
6/ kubectl create serviceaccount spark
7/ kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
8/ kubectl apply -f gcp_key.yaml 
9/ kubectl apply -f spark_k8s.yam

** Note: restart pod for each run
