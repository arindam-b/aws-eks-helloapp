Install eksctl

chocolatey install -y eksctl aws-iam-authenticator



eksctl create cluster --name mycluster --version 1.14 --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 4  --managed


eksctl get cluster --name mycluster --region us-east-1 
	kubectl get nodes

	kubectl apply -f python-hello-app\k8s.yaml



eksctl delete cluster --name mycluster --region us-east-1


