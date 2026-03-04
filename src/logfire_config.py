import logfire


def init_logfire():
    """Initialize Logfire instrumentation."""
    logfire.configure()
    logfire.instrument_mcp()
    logfire.instrument_pydantic_ai()
    logfire.instrument_httpx(capture_all=True)
