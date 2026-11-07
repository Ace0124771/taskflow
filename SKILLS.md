# Skills Covered in This Project

Building TaskFlow from scratch introduces a wide range of real software engineering skills. This document lists them by area, so learners and teachers can see at a glance what the project teaches. It pairs with the terminology guide: that guide explains the individual words, and this page maps the broader skills.

## Command line and environment
- Using the Linux terminal and basic shell commands
- Running Linux on Windows with WSL
- Enabling virtualization in the BIOS
- Installing software with a package manager
- Python virtual environments
- Managing dependencies with pip and a requirements file
- Working across several terminal windows at once

## Version control and GitHub
- Git basics: init, status, add, commit, push, log, and rm
- Commits as snapshots, and the main branch
- Writing clear commit messages
- Creating and pushing to a GitHub repository
- Authenticating and using the GitHub command line tool
- Using a gitignore file to keep a repository clean
- How authorship and credit work for your own and client projects

## Backend and API development
- Python programming
- Building an API with FastAPI
- REST ideas: endpoints, GET and POST, requests and responses
- HTTP status codes
- JSON as a data format
- Validating data with Pydantic
- Dependency injection for database access
- Automatically generated interactive API documentation
- Serving a web page from the API

## Databases
- What a relational database is
- Tables, rows, columns, and queries
- Using SQLAlchemy to work with a database from Python
- SQLite for local development and PostgreSQL for production
- Designing a data model
- Configuring the database through environment variables

## Queues, workers, and distributed systems
- What a message queue is and why it is useful
- Using Redis as a queue
- The producer and consumer pattern
- Writing a background worker
- Polling compared with blocking
- Splitting a system into separate cooperating services

## Reliability
- Automatic retries for failed work
- A limit so nothing retries forever
- A dead-letter queue for jobs that permanently fail
- Per-job timeouts
- Handling errors cleanly
- Tracking a job through its full lifecycle

## Frontend and dashboard
- Basic HTML, CSS, and JavaScript
- Calling a backend from the browser
- Building a dashboard that refreshes itself live

## Containers and DevOps
- What Docker, images, and containers are
- Writing a Dockerfile
- Running several services together with docker compose
- Service networking and environment variables
- Healthchecks and service dependencies
- Persisting data with volumes
- Practical debugging of real setup problems

## Testing and automation
- Writing automated tests with pytest
- Unit tests and API tests
- Isolating tests with an in-memory database and stubbed services
- Using a test client for the API
- Continuous integration with GitHub Actions

## Documentation and professional habits
- Writing a clear README
- Drawing an architecture diagram
- Technical writing aimed at beginners
- Organizing a project into a sensible structure
- Reading error messages and tracebacks to debug methodically
- Building in small steps, verifying each before moving on

## The habits that matter most
Beyond any single tool, this project builds the core habits of real engineering: reading errors carefully, tracing a problem to its source, staying calm through failures, and making steady progress one verified step at a time.
