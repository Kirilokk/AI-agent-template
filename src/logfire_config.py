import logfire


def init_logfire():
    """Initialize Logfire instrumentation."""
    logfire.configure(
        service_name='starter-project',
        console=False,
    )
    logfire.instrument_mcp()
    logfire.instrument_pydantic_ai()
    logfire.instrument_httpx(capture_all=True)