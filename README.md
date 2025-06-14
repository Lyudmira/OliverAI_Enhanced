# OliverAI Enhanced

This project provides a minimal FastAPI backend.

## Setup

Install dependencies with wheels (offline):

```bash
pip install --no-index --find-links /path/to/wheelhouse -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

The environment variables are:

- `SUPABASE_URL`
- `SUPABASE_KEY`
- `GEMINI_API_KEY`

## Running the server

```bash
uvicorn ai_backend.app.main:app --reload
```

## Testing

```bash
pytest
```


