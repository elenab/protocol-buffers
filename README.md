## Protocol buffers
Google Protobuf with examples and exercises.


### protoc
Use `protoc` to generate code:

- Python:
```
protoc -I=proto --python_out=python proto/*.proto 
```

- JAVA:
```
protoc -I=proto --java_out=java proto/*.proto 
```

- CPP:
```
protoc -I=proto --cpp_out=cpp proto/*.proto 
```