# Anime & Manga Explorer (ame)

Anime & Manga Explorer (ame) is a web application that helps users discover and explore anime and manga titles using real-time data from public APIs such as AniList or Jikan API. Users can search by genre, rating, and other filters, and even save their favorite titles for later reference.

## Features

- **API Integration:** Retrieves up-to-date anime and manga data from external APIs.
- **RESTful API:** Built with FastAPI, providing endpoints for search, filtering, and managing user favorites.
- **Interactive Frontend:** Built with Reflex.
- **Database Persistence:** Utilizes PostgreSQL via SQLAlchemy to store user data and favorites.
- **Auto-Generated Docs:** Interactive API documentation is available at `/docs`.

## Technologies Used

- **Backend:** FastAPI, Uvicorn
- **Database:** SQLAlchemy, PostgreSQL
- **API Consumption:** Requests
- **Frontend:** Reflex

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ronnyascencio/ame.git
   cd ame
   ```
