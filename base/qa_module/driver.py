from QAModel import QAModel

model = QAModel(model="deepset/xlm-roberta-large-squad2", useCuda=False)
context = '''
so in this video I'm going to explain what kubernetes is we're going to start off with the definition to see what official definition is and what it does then we're going to look at the problem solution case study of Cabezas basically why did kubernetes even come around and what problems does it solve we're gonna look at the basic architecture what are the master nodes and the slave nodes and what are the kubernetes processes that actually make up the platform mechanism then we going to see some basic concepts and the components of kubernetes which are pots and containers and services and what is the role of each one of those components and finally we going to look at a simple configuration that you as a kubernetes cluster user would use to create those components and configure the cluster to your needs so let's jump in right into the definition what is kubernetes so kubernetes is an open source container orchestration framework which was originally developed by google so on the foundation it manages containers be docker containers or from some other technology which basically means that kubernetes helps you manage applications that are made up of hundreds or maybe thousands of containers and it helps you manage them in different environments like physical machines virtual machines or cloud environments or even hybrid deployment environments so what problems does kubernetes solve and what are the tasks of a container orchestration tool actually so to go through this chronologically the rise of micro services cause increased usage of container technologies because the containers actually offer the perfect host for small independent applications like Microsoft a nurse and the micro service technology actually resulted in applications that they're now comprised of hundreds or sometime maybe even thousands of containers now managing those loads of containers across multiple environments using scripts and self-made tools can be really complex and sometimes even impossible so that specific scenario actually caused the need for having container orchestration technologies so what those orchestration tools like kubernetes do is actually guarantee following features one is high availability in simple words high availability means that the application has no downtime so it's always accessible by the users a second one is scalability which means that application has a high performance it loads fast and users have a very high response rates from the application and the third one is disaster recovery which basically means that if an infrastructure has some problems like data is lost or the server's explode or something bad happens with the server center the infrastructure has to have some kind of mechanism to pick up the data and to restore it to the latest state so that application doesn't actually lose any data and the containerized application can run from the latest stayed after the recovery and all of these are functionalities that container orchestration technologies like kubernetes offer so how does the kubernetes basic architecture actually look like the kubernetes cluster is made up with at least one master node and then connected to it you have a couple of worker nodes where each node has a cubelet process running on it and cubelet is actually a kubernetes process that makes it possible for the cluster to talk to each other to communicate to each other and actually execute some tasks on those nodes like running application processes each worker node has docker containers of different applications deployed on it so depending on how the workload is distributed you would have different number of docker containers running on worker nodes and worker nodes are where the actual work is happening so here is where where your applications are running so the question is what is running on master node master node actually runs several kubernetes processes that are absolutely necessary to run and manage the cluster properly one of such processes is an API server which also is a container an API server is actually the entry point to the kubernetes cluster so this is the process which the different kubernetes clients will talk to like UI if you're using kubernetes dashboard an API if you're using some scripts and automating technologies and a command-line tool so all of these will talk to the API server another process that is running on master node is a controller manager which basically keeps an overview of what's happening in the cluster whether something needs to be repaired or maybe if a container died and it needs to be restarted etc and another one is scheduler which is basically responsible for scheduling containers on different nodes based on the workload and the available server resources on each node so it's an intelligent process that decides on which worker node the next container should be scheduled on based on the available resources on those worker notes and the load that that container meets and another very important component of the whole cluster is actually an etcd key value storage which basically holds at any time the current state of the kubernetes cluster so it has all the configuration data inside and all the status data of each node and each container inside of that node and the backup and restore that we mentioned previously is actually made from these etcd snapshots because you can recover the whole cluster state using that etcd snapshot and last but not least also a very important component of kubernetes which enables those notes worker notes master notes talk to each other is the virtual network that spends all the notes that are part of the cluster and in simple words virtual network actually turns all the notes inside of the cluster into one powerful machine that has the sum of all the resources of individual notes one thing to be noted here is that work who knows because they actually have most load because they are running the applications on inside of it usually are much bigger and have more resources because they will be running hundreds of containers inside of them where is master node will be running just a handful of master processes like we see in this diagram so it doesn't need that many resources however as you can imagine master node is much more important than the individual worker notes because if for example you lose a master node excess you will not be able to access the cluster anymore and that means that you absolutely have to have a backup of your master at any time so in production environments usually you would have at least two masters inside of your kubernetes cluster but in more cases of course you're going to have multiple masters where if one master node is down the cluster continues to function smoothly because you have other masters available so now look at some kubernetes basic concepts like pots and containers in kubernetes pod is the smallest unit that you as a kubernetes user will configure and interact with in pod is basically a wrapper of a container and on each worker node you're gonna have multiple pods and inside of a pod you can actually have multiple containers usually per application you would have one pod so the only time you would need more than one containers inside of a pod is when you have a main application that needs some helper containers so usually you would have one pod per application so a database for example would be one pod a message broker will be another pod a server will be again another pod in Europe no J's application for example or a java application will be its own pod and as we mentioned previously as well there is a virtual network dispense the kubernetes cluster so what that does is that it assigns each pod its own IP address so each pod is its own self containing server with its own IP address and the way that they can communicate with each other is we using that internal IP addresses and to note here we don't actually configure or create containers inside of kubernetes cluster but we only work with the pods which is an abstraction layer over containers and pod is a component of kubernetes that manages the containers running inside itself without our intervention so for example if a container stops or dies inside of a pod it will be automatically restarted inside of the pod however pods are ephemeral components which means that pots can also die very frequently and when a pod dies a new one gets created and here is where the notion of service comes into play so what happens is that whenever a pod gets restarted or weak a new pod is created and it gets a new IP address so for example if you have your application talking to a database pod using the IP address the pods have and the pod restarts it gets a new IP address obviously it would be very inconvenient but just that IP address all the time so because of that another component of Cabrini's called service is used which basically is an alternative or a substitute to those IP addresses so instead of having this dynamic IP addresses their services sitting in front of each pod that talk to each other so now if a pod behind the service dies and gets recreated the service stays in place because their life cycles are not tied to each other and the service has two main functionalities one is an IP address so it's a permanent IP address which you can use to communicate with between the pods and at the same time it is a load balancer so now that we have seen the basic concepts of kubernetes how do we actually create those components like pods and services to configure the kubernetes cluster all the configuration in kubernetes cluster actually goes through a master node with the process called API server which we mentioned briefly earlier so kubernetes clients which could be a UI a kubernetes dashboard for example or an API which could be a script or curl command or a command line tool like cube CTL they all talk to the API server and they send their configuration requests to the API server which is the main entry point or the only entry point into the cluster in this requests have to be either in yellow format or JSON format and this is how a example configuration in the ML format actually looks like so with this we are sending a request to kubernetes to configure a component called deployment which is basically a template or a blueprint for creating pots and in this specific configuration example we tell kubernetes to create to replica pots for us called my app with each pod replica having a container based on my image running inside in addition to that we configure what the environment variables and the port configuration of this container inside of the pot should be and as you see the configuration requests in kubernetes our declarative form so we declare what is our desired outcome from kubernetes and kubernetes tries to meet those requirements meaning for example since we declare we want to replica pots of my app deployment to be running in the cluster and one of those pots dies the controller manager will see that the east and shoot states now are different the actual state is one part our desired state is two so it goes to work to make sure that this desired state is recovered automatically restarting the second replica of that pot and this is how kubernetes configuration works with all of its component be the parts or the services or deployments what have you thanks for watching the video I hope it was helpful and if it was don't forget to like it if you want to be notified whenever a new video comes out then subscribe to my channel if you have any questions if something wasn't clear in the video please post them in a comment section below and I will try to answer them so thank you and see you in the next video
'''

questions = [
    'what is kubernetes?',
    'who developped kubernetes?',
    'how does kubernetes help?'
]

for q in questions:
    q = input("Enter Question: ")
    answers = model.getAnswers(context=context, question=q)
    for ans in answers:
        print(ans[0])
    print()