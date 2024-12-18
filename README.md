# Enhanced Google Online Boutique Store - Like Service  

This project extends the existing [Google Online Boutique Store](https://github.com/GoogleCloudPlatform/microservices-demo) by introducing a **Like Service**. The feature allows users to express their appreciation for products in the store by clicking a **like button**. This enhancement aims to improve **user engagement** and provide valuable feedback for future product improvements.  

---

## **Feature: Like Button for Products**  
- Users can "like" a product by clicking the like button on the product page.  
- Each "like" is recorded and stored, allowing the system to track product popularity.  
- This feature enhances user interaction and provides insights into customer preferences.  

---

## **Prerequisites**  
Before building and running the project, ensure you have the following tools installed:  

1. **Docker** (e.g., Docker Desktop) - To build and run containerized services.  
2. **Minikube** - To set up a local Kubernetes cluster.  
3. **Skaffold** - To streamline local deployment of Kubernetes manifests.  
4. **kubectl** - To manage Kubernetes clusters.  

---

## **Setup Instructions to build and deploy services locally**

### **Clone the Repository**  
Clone this repo


### Start Minikube  
Start a Minikube Kubernetes cluster:  
```bash
minikube start
```

### Enable Minikube Docker Environment  
Ensure Docker builds use Minikube’s Docker daemon:  
```bash
eval $(minikube docker-env)
```

### Build the Docker Images  
Rebuild the Like Service and other services:  
```bash
skaffold build
```

> **Note**: `skaffold.yaml` is already configured to include the Like Service.

### Deploy Services to Minikube  
Deploy the application with Skaffold:  
```bash
skaffold run
```
(or use skaffold dev instead of build and run)

### Verify Services  
Check if the services are running:  
```bash
kubectl get pods
```
Ensure all pods are in the `Running` state.

### Access the Application  
Once deployed, access the online store in your browser:  
```bash
minikube service frontend-external
```

This will open the Online Boutique frontend in your default browser.  

---

## **Testing the Like Service**  

To verify the Like Service functionality:  

1. Open the online store and navigate to a product page.  
2. Click the **Like Button**.  
3. The "like" should be successfully recorded, and you should see confirmation in the logs.  

You can inspect the logs for the Like Service:  
```bash
kubectl logs -l app=likeservice
```

---

## **Clean Up**  
To stop and delete the local Kubernetes cluster:  
```bash
skaffold delete
minikube stop
minikube delete
```

---

## **Technical Details**  

### **Like Service Implementation**  
- The Like Service was added as a new gRPC microservice.  
- It communicates with the frontend to handle user interactions and record likes for products.  

### **Changes in the Codebase**  
1. **New Microservice**: `likeservice` was added under a dedicated folder with its own:  
   - gRPC protobuf definitions (`likeservice.proto`)  
   - Server implementation (`server.py` or `server.go`)  
   - Dockerfile for building the container image.  
2. **Frontend Changes**:  
   - Added a "Like Button" to the product page.  
   - Connected the frontend to the Like Service using gRPC.  

---

## **Authors**  
- Patrick Gottschling  
- Martin Kühner  
- Maximilian Thorn  

**Technische Universität Berlin**  
**Course: Continuous Software Engineering**  

---

## **License**  
This project builds upon the [GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo) repository, which is licensed under the Apache License 2.0.  

---

### **Happy Liking! 🚀**
