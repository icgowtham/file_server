# File Server
* Python based application to serve static files on the web browser.

### Introduction
* `file_server` is a Python based application to serve static files on a web browser. It makes use of the `http.server` package provided by Python.

### Sample usage:
* Edit the `default.cfg` file under `cfgs\default.cfg` and change the values for `base_path` and `http_server_port`.
    * The `base_path` specifies the root directory whose contents can be viewed on the web browser.
    * `http_server_port` is the port used by the application.
* On a terminal run the file server application:
```bash
$ python3 file_server
```
* Open a web browser and navigate to http://<your machine's ip>:8888/. Note the trailing '/'.
    * For e.g., if the machine IP is 192.168.1.111, then type http://192.168.1.111:8888/
    * NOTE: Ingress and egress traffic on port 8888 should be enabled to view the application.


### Development
Clone the git repo and follow the steps below on any linux  machine.

    git clone https://github.com/icgowtham/file_server.git
    cd file_server

Setup python virtual environment.

    make setup-env
    source env3/bin/activate


### Compliance

To validate compliance, complexity and coverage:

    make compliance <code_path>

