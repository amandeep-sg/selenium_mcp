import os
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from fastmcp import Client, FastMCP
from google import genai
from fastmcp.server.providers import FileSystemProvider
import logging
from pydantic import BaseModel, HttpUrl, Field
from typing import List

# Load environment variables
load_dotenv(".env")

# Get Gemini API key from env variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure logging
logging.basicConfig(
    filename="test.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    level=logging.INFO,
    force=True,
)

# Get logger instances
logger = logging.getLogger(__name__)

# Configure selenium logger
selenium_logger = logging.getLogger("selenium")
selenium_logger.setLevel(logging.INFO)

# Configure mcp provider
provider = FileSystemProvider(root=Path(__file__).parent / "mcp_server", reload=True)

mcp_Server = FastMCP(
    "selenium_mcp",
    providers=[provider],
)

## MCP client using gemini SDK
mcp_client = Client(mcp_Server)
gemini_client = genai.Client(api_key=gemini_api_key)


class URLS(BaseModel):
    links: List[str] = Field(
        description='List of urls in json format. example: {"links": ["url1", "url2", "url3"]}'
    )


async def main():
    async with mcp_client:
        logger.info("MCP client connected")
        try:
            response = await gemini_client.aio.models.generate_content(
                model="gemini-3.1-flash-lite-preview",
                contents="Open https://sbi.bank.in/web/sbi-in-the-news/procurement-news and return the list of pdf urls. Do not make multiple tools calls",
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[mcp_client.session],  # Pass the FastMCP client session
                    automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                        maximum_remote_calls=5  # Increase from default
                    ),
                    response_mime_type="application/json",
                    response_json_schema=URLS.model_json_schema(),
                ),
            )
            for part in response.candidates[0].content.parts:
                print(part)
        except Exception as e:
            print(e)
            logger.error(e)


asyncio.run(main())
