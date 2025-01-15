# Smart Invoice Dispatcher

This application is hosted on Google Cloud Platform (GCP), running on an `e2-micro` instance at the IP address `34.136.162.44`. You can verify that the server is running by making a GET request to `https://34.136.162.44`. The server will respond with a message confirming that it is running.

**Note:** When making an HTTPS request, you will notice that the server currently uses a **self-signed certificate**. While I used this approach on this challenge, I fully understand that self-signed certificates are not suitable for production systems. In a production environment, a valid certificate from a trusted Certificate Authority (CA), should always be used to ensure secure and trusted communication.

The responsibilities of the application running on GCP are:
1. Receive webhooks from external services.
2. Create invoices at the specified time.
3. Automatically process transfers when webhooks notify that invoices have been paid.

## Running in Production

To run this application in production, follow these steps:

1. **Add a Private Key File**:  
   You must add a `private-key.pem` file to the base folder of the repository. This file is required for authentication and secure communication.

2. **Update Environment and Project ID**:  
   You might also want to change the environment and project ID in the `src/StarkBankAuth.py` file to match your production settings.

## Building and Running with Docker

To build and run the application using Docker, follow these steps:

1. **Build the Docker Image**:  
   Use the following command to build the Docker image:  
   ```sh
   sudo docker build . -t smart-invoice-dispatcher
   ```

2. **Run the Docker Container**:  
   To run the container in detached mode and map port 443, use the following command:  
   ```sh
   docker run -d -p 443:443 smart-invoice-dispatcher
   ```

## Running Tests

To run the tests for this project, make sure you have Python installed and navigate to the project's root directory.

### Using `unittest`

If the tests are written using the `unittest` framework, you can run them using the following command:

```sh
python -m unittest discover -s tests
```
