alias k=kubectl

-----------------------------------
------ replicaset.yaml  --- com o replicaset os pods se tornam resilientes. ao matar um o replicaset provisiona outro. ele monitora os pods com a label desejada
-----------------------------------
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      container: principal
  template:
    metadata:
      labels:
        container: principal
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
-----------------------------------


k apply -f kubernetes/02-replicaset/replicaset.yaml

    # mostram 2 conforme o manifesto
k get pods

k get replicaset

    # matando um pod
k delete pods nginx-rs-<hash do pod>

    # vai mostrar dois novamente pois ele ja provisiona outro
k get pods

k describe replicaset nginx-rs

    # escala o numero de pods de 2 para 5
k scale replicaset nginx-rs --replicas=5

k get pods

k scale replicaset nginx-rs --replicas=2

k get pods

    # atualiza qual é a imagem que o replica set está cuidando
k set image replicaset nginx-rs nginx=nginx:1.26

    # mostra a imagem atualizada
k describe replicaset

k get pods 

    # mostra que a imagem dos pods não foi atualizada ainda mas não fas o rollout da versão
k describe pods nginx-rs-5m6qq 