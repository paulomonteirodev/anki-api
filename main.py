from app import create_app
from fastapi.responses import RedirectResponse
import api.login_api as login_api
import api.deck_api as deck_api

app = create_app()
app.include_router(login_api.router)
app.include_router(deck_api.router)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")
