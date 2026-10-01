from fastapi import APIRouter, HTTPException
from tavily import TavilyClient

from app.core.config import search_settings
from app.schemas.web_search import WebSearchRequest

search_router = APIRouter()


@search_router.post("/search")
def web_search(request: WebSearchRequest):
    if not search_settings.TAVILY_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="Web search is not configured. Set TAVILY_API_KEY.",
        )

    time_range = request.time_range
    if request.recent_only and time_range is None:
        time_range = "week"

    search_options = {
        "query": request.query,
        "max_results": request.max_results,
        "include_published_date": True,
    }
    if time_range is not None:
        search_options["time_range"] = time_range
        search_options["filter_by_published_date"] = True

    try:
        results = TavilyClient(api_key=search_settings.TAVILY_API_KEY).search(
            **search_options
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="The web search provider could not complete the request.",
        ) from exc

    return {
        **results,
        "recent_data_check": {
            "enabled": time_range is not None,
            "time_range": time_range,
            "results_checked": len(results.get("results", [])),
        },
    }