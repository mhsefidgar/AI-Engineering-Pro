# Node.js Backend Foundations

Node.js runs JavaScript/TypeScript services on a runtime designed around asynchronous I/O.

## Topics

- Event loop and task scheduling
- Promises and async/await
- Modules and package management
- Environment variables
- Streams and buffers
- File system APIs
- HTTP servers
- Graceful shutdown
- Process signals
- Dependency management

## Mental model

CPU-heavy synchronous work can block the event loop. Network and filesystem I/O should generally use asynchronous APIs. Long-running or CPU-heavy workloads may need worker threads or an external job system.

## Production baseline

Pin dependencies, validate configuration at startup, set network timeouts, handle process signals, close database/queue connections during shutdown, and expose health checks.