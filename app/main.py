try:
    from fastapi import FastAPI
except Exception:  # pragma: no cover - fallback for environments without fastapi
    # Minimal stub to allow static analysis / simple runs when FastAPI is not installed
    class FastAPI:
        def __init__(self, *args, **kwargs):
            pass

        def get(self, *args, **kwargs):
            def _decor(fn):
                return fn
            return _decor


app = FastAPI()


@app.get("/check")
def quick_check():
    return {"message": "Quick check passed!"}