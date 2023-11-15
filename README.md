# Smedia Bot

This project is a test task for Smedia.

## Main Technologies Used

- Python
- Asyncio
- PostgreSQL
- Pyrogram
- SQLAlchemy
- Docker

## Deploying the Project

### Requirements
- Docker and Docker Compose installed
- GNU Make

### Instructions:
1. Run this sample code to get your pyrogram session https://docs.pyrogram.org/start/auth
2. Clone the repository
   ```bash
   git clone https://github.com/kirillovme/smedia_bot.git
   ```
3. Complete .env with your TELEGRAM_API_ID and TELEGRAM_API_HASH. You should get it from https://core.telegram.org/api/obtaining_api_id
4. Place session file into bot folder
5. Start the containers
   ```bash
   make up-d
   ```

## Project Branch Structure

- `main` - Current production branch of the project
- `develop` - Main development branch
