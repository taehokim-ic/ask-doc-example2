release: python -m snips_nlu download en
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --preload