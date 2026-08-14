alias k=kubectl

	# inicializa minikube com 3 node passando a versão do kubernetes e qual o nome do cluster
minikube start --nodes 3 --kubernetes-version=v1.32.3 -p homelab


	# exime os nodes existentes com status, rules, ages..
k get nodes

	# exibe os comando do kubectl
k --help

	# sobe um pod basedo em uma imagem
k run webapp-123 --image=nginx

	# exibe quais pods estão rodando
k get pods

	# descreve as configurações dos pods que estão rodando
k describe pods webapp-123

	# exibe os logs do pod
k logs webapp-123

	# exibe os logs do pod em tempo real
k logs -f webapp-123

	# expõe o app em uma porta do nosso computador. No caso fica portal_local:porta_do_app
k port-forward webapp-123 8080:80

	# deleta o pod
k delete pods webapp-123

	# exbibe o manifesto do meu pod
k get pods webapp-123 -o yaml

	# explica o recurso. no caso explica o pod
k explain pods

	# aprofundando na doc dos sub-itens
k explain pods.metadata

	# idem
k explain pods.metadata.annotations



-----------------------------------
------ pod.yaml  --- esse vai dar erro para debugar
-----------------------------------
apiVersion: v1
kind: Pod
metadata:
  name: webserver
  labels:
    name: exemplo_didatico
    type: webserver
spec:
  containers:
  - name: ngix
    image: ngix
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: 80
  - name: apache
    image: httpd
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: 80
-----------------------------------

k get nodes

k describe pods webserver

k logs webserver

k logs webserver -c apache

k logs webserver -c nginx

k delete pod webserver

k apply -f pod.yaml

	# para não ter q deletar o pod e subir outro podemos dar o comando replace com o --force
k replace -f pod.yaml --force

	#atualizando a imagem do pod que está rodando
k set image pods webserver apache=nginx:alpine
