# StarkBank Challenge

This application is hosted on Google Cloud Platform (GCP), running on an `e2-micro` instance at the IP address `34.136.162.44`. You can verify that the server is running by making a GET request to `https://34.136.162.44`. The server will respond with a message confirming that it is running.

**Note:** When making an HTTPS request, you will notice that the server currently uses a **self-signed certificate**. While I used this approach for the purposes of this job interview challenge, I fully understand that self-signed certificates are not suitable for production systems. In a production environment, a valid certificate from a trusted Certificate Authority (CA), should always be used to ensure secure and trusted communication.

The GCP machine is designed to:
1. Receive webhooks from external services.
2. Create invoices at the specified time.
3. Automatically process transfers when webhooks notify that invoices have been paid.

## Running Tests

To run the tests for this project, make sure you have Python installed and navigate to the project's root directory.

### Using `unittest`

If the tests are written using the `unittest` framework, you can run them using the following command:

```sh
python -m unittest discover -s tests
```