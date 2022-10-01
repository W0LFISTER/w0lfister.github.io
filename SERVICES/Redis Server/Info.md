---
---
---
# Redis server  
---
## What is Redis?

Redis (**RE**mote **DI**ctionary **S**erver) is an open-source advanced NoSQL key-value data store used as a  database, cache, and message broker. The data is stored in a dictionary format having key-value pairs. It is  typically used for short term storage of data that needs fast retrieval. Redis does backup data to hard drives  to provide consistency

### The server
Redis runs as server-side software so its core functionality is in its server component. The server listens for connections from clients, programmatically or through the command-line interface.

### The CLI  
The command-line interface (CLI) is a powerful tool that gives you complete access to Redis’s data and its functionalities if you are developing a software or tool that needs to interact with it.  

### Database  
The database is stored in the server's RAM to enable fast data access. Redis also writes the contents of the  database to disk at varying intervals to persist it as a backup, in case of failure.