#README

###1. Create cluster:

 eksctl create cluster --name mycluster --version 1.14 --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 4  --managed
[ℹ]  eksctl version 0.11.1
[ℹ]  using region us-east-1
[ℹ]  setting availability zones to [us-east-1d us-east-1b]
[ℹ]  subnets for us-east-1d - public:192.168.0.0/19 private:192.168.64.0/19
[ℹ]  subnets for us-east-1b - public:192.168.32.0/19 private:192.168.96.0/19
[ℹ]  using Kubernetes version 1.14
[ℹ]  creating EKS cluster "mycluster" in "us-east-1" region with managed nodes
[ℹ]  will create 2 separate CloudFormation stacks for cluster itself and the initial managed nodegroup
[ℹ]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-east-1 --cluster=mycluster'
[ℹ]  CloudWatch logging will not be enabled for cluster "mycluster" in "us-east-1"
[ℹ]  you can enable it with 'eksctl utils update-cluster-logging --region=us-east-1 --cluster=mycluster'
[ℹ]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "mycluster" in "us-east-1"
[ℹ]  2 sequential tasks: { create cluster control plane "mycluster", create managed nodegroup "standard-workers" }
[ℹ]  building cluster stack "eksctl-mycluster-cluster"
[ℹ]  deploying stack "eksctl-mycluster-cluster"
[ℹ]  building managed nodegroup stack "eksctl-mycluster-nodegroup-standard-workers"
[ℹ]  deploying stack "eksctl-mycluster-nodegroup-standard-workers"
[✔]  all EKS cluster resources for "mycluster" have been created
[✔]  saved kubeconfig as "C:\\Users\\a636174/.kube/config"
[ℹ]  nodegroup "standard-workers" has 2 node(s)
[ℹ]  node "ip-192-168-19-11.ec2.internal" is ready
[ℹ]  node "ip-192-168-58-128.ec2.internal" is ready
[ℹ]  waiting for at least 1 node(s) to become ready in "standard-workers"
[ℹ]  nodegroup "standard-workers" has 2 node(s)
[ℹ]  node "ip-192-168-19-11.ec2.internal" is ready
[ℹ]  node "ip-192-168-58-128.ec2.internal" is ready
[ℹ]  kubectl command should work with "C:\\Users\\a636174/.kube/config", try 'kubectl get nodes'
[✔]  EKS cluster "mycluster" in "us-east-1" region is ready

###2. Verify:

eksctl get cluster --name mycluster --region us-east-1
NAME            VERSION STATUS  CREATED                 VPC                     SUBNETS                                                                                                 SECURITYGROUPS
mycluster       1.14    ACTIVE  2020-01-13T18:47:09Z    vpc-07b2e90f57fab034b   subnet-0110d24819d40a3e3,subnet-0144b2ad59145dd3a,subnet-0820e8824fca19022,subnet-097df0afb12527e94     sg-0c09257c7d89ee9bd

kubectl get nodes
NAME                             STATUS   ROLES    AGE    VERSION
ip-192-168-19-11.ec2.internal    Ready    <none>   2m     v1.14.7-eks-1861c5
ip-192-168-58-128.ec2.internal   Ready    <none>   2m5s   v1.14.7-eks-1861c5


Now all clusters are working fine. 

#Install Python App that 

kubectl apply -f python-hello-app\k8s.yaml

deployment.apps/frontend created
service/frontend created


kubectl get svc

NAME         TYPE           CLUSTER-IP     EXTERNAL-IP                                                              PORT(S)        AGE
frontend     LoadBalancer   10.100.61.16   a73860f86363711eab0700e42eb1f8f6-114174152.us-east-1.elb.amazonaws.com   80:30779/TCP   34s
kubernetes   ClusterIP      10.100.0.1     <none>                                                                   443/TCP        9m17s

kubectl get pod -w
NAME                        READY   STATUS    RESTARTS   AGE
frontend-5c65ccfc8d-w9qhl   1/1     Running   0          41s

curl http://a73860f86363711eab0700e42eb1f8f6-114174152.us-east-1.elb.amazonaws.com/get-multiply/10
100

# Install using helm chart

cd micronaut-api-chart

helm upgrade --install micronaut-api --values micronaut-api-chart/values_prod.yaml ./micronaut-api-chart

Release "micronaut-api" does not exist. Installing it now.
NAME: micronaut-api
LAST DEPLOYED: Mon Jan 13 20:02:07 2020
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w micronaut-api-micronaut-api-chart'
  export SERVICE_IP=$(kubectl get svc --namespace default micronaut-api-micronaut-api-chart --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:80
  
  
kubectl get services
NAME                                TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE
kubernetes                          ClusterIP      10.100.0.1       <none>                                                                    443/TCP        7m57s
micronaut-api-micronaut-api-chart   LoadBalancer   10.100.236.143   a314d985a363711eab0700e42eb1f8f6-1872118509.us-east-1.elb.amazonaws.com   80:31793/TCP   65s



# Delete the cluster

eksctl delete cluster --name mycluster --region us-east-1
[ℹ]  eksctl version 0.11.1
[ℹ]  using region us-east-1
[ℹ]  deleting EKS cluster "mycluster"
[ℹ]  deleted 0 Fargate profile(s)
[✔]  kubeconfig has been updated
[ℹ]  cleaning up LoadBalancer services
[ℹ]  2 sequential tasks: { delete nodegroup "standard-workers", delete cluster control plane "mycluster" [async] }
[ℹ]  will delete stack "eksctl-mycluster-nodegroup-standard-workers"
[ℹ]  waiting for stack "eksctl-mycluster-nodegroup-standard-workers" to get deleted
[ℹ]  will delete stack "eksctl-mycluster-cluster"
[✔]  all cluster resources were deleted  