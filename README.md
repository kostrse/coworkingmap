# coworkingmap
A demo website with Kudu deployment for Azure Web Apps.

## How to build

To build this website you need *node.js*, *gulp* and *bower* installed on your machine:

```
npm install bower -g
npm install gulp -g
```

Then, just run this build script from the repository root:

```
python deploy/deploy.py
```

Or you can build it manually from the `website` directory:

```
cd website

npm install
bower install
gulp
```

## How to run

Publish this website using a HTTP server, for example **http-server**.

```
npm install http-server -g

cd website

http-server
```
