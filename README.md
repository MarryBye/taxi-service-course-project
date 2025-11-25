# Taxi course project

Taxi service web application with integrated database created as a part of the university course project.

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Project](#running-the-project)

## Overview

This course project is a taxi service application designed to simplify and automate the process of requesting and managing rides. The main goal of the project is to connect passengers who need transportation with available drivers in a fast, transparent, and reliable way.

The system allows passengers to create ride requests, automatically matches them with nearby drivers, and provides real-time status updates (such as driver assignment, arrival time, and trip progress). For drivers, the service offers tools to receive new orders, manage active rides, and track completed trips.

In addition to basic ride ordering, the project focuses on improving user experience and service quality: it supports fare calculation based on distance and time, different tariff options, and basic safety features (such as storing trip history and user information). The project is intended primarily as an educational example of designing and implementing a full-stack application: from business logic and data storage to interaction between different system components and user interfaces.

## Tech Stack

- **Language:** Python + JavaScript + HTML + CSS
- **Framework (Backend):** FastAPI + Pydantic, psycopg2, dotenv
- **Framework (Frontend):** TypeScript & React + React Router, Vite, SASS
- **Database:** PostgreSQL
- **Build / Tooling:** uvicorn, Vite, Docker

## Features

Highlight key features of the project:

- 1
- 2
- 3
- 4
- 5

## Getting Started

### Prerequisites

All requirements are listed in `requirements.txt` file.

- Node.js >= 22.8
- Python >= 3.13
- Pydantic >= 2.12.4
- FastAPI >= 0.121.3
- dotenv >= 0.9.9
- psycopg2 >= 2.9.11

### Installation

1. Clone the repo: `git clone URL_HERE`
2. Install dependencies: `pip install -r requirements.txt`
3. Install frontend dependencies: `cd frontend && npm install`

### Environment Variables

- `DB_HOST` - your database host
- `DB_PORT` - your database port
- `DB_USER` - your database username
- `DB_PASSWORD` - your database password
- `DB_NAME` - your database name

### Running the Project

1. Check .env configuration file for database credentials
2. Run the project: `docker-compose up`
3. Open `http://localhost:3000` in your browser