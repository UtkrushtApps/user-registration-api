# User Registration API

## Task Overview
A membership platform requires a simple user registration API that prevents duplicate accounts using the same email address. The current system allows multiple entries with identical emails, leading to data inconsistencies and potential security issues. Your task is to address this by enforcing unique user registration, ensuring that each email address can only be registered once.

## Guidance
- This project uses FastAPI for developing RESTful endpoints and PostgreSQL as the database for persistent storage.
- Organize your application using routers for route definitions, Pydantic models for data validation, and async SQLAlchemy for database interactions.
- Ensure that all endpoints use async/await patterns and provide clear error messages for invalid requests.
- Follow best practices for environment configuration, containerization, and error handling.

## Objectives
- Implement a user registration endpoint that accepts a user's name and email address.
- Enforce a unique constraint on the email field so each email can only be registered once.
- Return an appropriate HTTP status and a clear error message if a duplicate email is submitted.
- Structure the project into logical modules including routers, models, services, and database connections.
- Containerize both the FastAPI application and the PostgreSQL database.

## How to Verify
- Registering a new user with a unique email should succeed and return the user details.
- Attempting to register with an email that already exists should result in an error response indicating the email is already registered.
- The database should not contain duplicate entries for the same email.
- All endpoints should be documented in the OpenAPI schema and respond with the correct status codes.
