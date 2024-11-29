# home_task_dynamic_port
## overview:
This project demonstrates how to set up two Kubernetes pods that communicate with each other, where one pod uses a static port and the other selects a dynamic port at runtime. The communication is enabled through a custom service discovery mechanism using etcd as a service registry.
### Key Components:
* Pod One (Static Port): Runs a Python application (client.py) that continuously discovers the IP and port of Pod Two by querying the service registry. It then communicates with Pod Two using this information.

* Pod Two (Dynamic Port): Runs a Python application (app.py) that selects an available dynamic port at startup. It registers its IP and selected port with the service registry so that other pods can discover it.

* Service Registry (etcd): Acts as a central registry where services can register themselves and discover others. Pod Two registers its dynamic port and IP address here, and Pod One queries it to find Pod Two.
