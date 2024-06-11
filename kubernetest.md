### Kubernetes Handouts

#### 1. Pods
**Definition**: A Pod is the smallest and simplest Kubernetes object. It represents a single instance of a running process in your cluster.

**YAML Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
```

#### 2. Deployment
**Definition**: A Deployment provides declarative updates to applications and is the recommended way to manage stateless applications.

**YAML Example**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: nginx
        ports:
        - containerPort: 80
```

#### 3. Job
**Definition**: A Job creates one or more Pods and ensures that a specified number of them successfully terminate.

**YAML Example**:
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: my-job
spec:
  template:
    spec:
      containers:
      - name: my-container
        image: busybox
        command: ["echo", "Hello Kubernetes!"]
      restartPolicy: OnFailure
```

#### 4. CronJob
**Definition**: A CronJob creates Jobs on a time-based schedule.

**YAML Example**:
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: my-cronjob
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: my-container
            image: busybox
            command: ["echo", "Hello Kubernetes!"]
          restartPolicy: OnFailure
```

#### 5. DaemonSet
**Definition**: A DaemonSet ensures that all (or some) Nodes run a copy of a Pod.

**YAML Example**:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: my-daemonset
spec:
  selector:
    matchLabels:
      name: my-daemonset-pod
  template:
    metadata:
      labels:
        name: my-daemonset-pod
    spec:
      containers:
      - name: my-container
        image: nginx
        ports:
        - containerPort: 80
```

#### 6. StatefulSet
**Definition**: A StatefulSet is the workload API object used to manage stateful applications.

**YAML Example**:
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: my-statefulset
spec:
  selector:
    matchLabels:
      app: my-app
  serviceName: "my-service"
  replicas: 3
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: nginx
        ports:
        - containerPort: 80
  volumeClaimTemplates:
  - metadata:
      name: my-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
```

#### 7. Services
**Definition**: A Service is an abstract way to expose an application running on a set of Pods.

**YAML Example**:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

#### 8. ConfigMap
**Definition**: A ConfigMap is used to store configuration data in key-value pairs.

**YAML Example**:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  key1: value1
  key2: value2
```

#### 9. Secrets
**Definition**: A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key.

**YAML Example**:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
```
*Note: The data is base64 encoded.*

#### 10. Volumes
**Definition**: A Volume is a directory accessible to the containers in a Pod. Kubernetes supports several types of volumes.

**YAML Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    volumeMounts:
    - mountPath: "/data"
      name: my-volume
  volumes:
  - name: my-volume
    hostPath:
      path: "/path/on/host"
      type: Directory
```
