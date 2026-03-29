import os
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from fastmcp import Client, FastMCP
from google import genai
from fastmcp.server.providers import FileSystemProvider
import logging


load_dotenv(".env")

gemini_api_key = os.getenv("GEMINI_API_KEY")

logging.basicConfig(
    filename="test.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    level=logging.DEBUG,
    force=True,
)

logger = logging.getLogger(__name__)
selenium_logger = logging.getLogger("selenium")
selenium_logger.setLevel(logging.INFO)

provider = FileSystemProvider(root=Path(__file__).parent / "mcp_server", reload=True)

mcp_Server = FastMCP(
    "rfp_notifications",
    providers=[provider],
)

mcp_client = Client(mcp_Server)

gemini_client = genai.Client(api_key=gemini_api_key)

logger = logging.getLogger(__name__)


async def main():
    async with mcp_client:
        logger.info("MCP client connected")
        try:
            response = await gemini_client.aio.models.generate_content(
                model="gemini-3.1-flash-lite-preview",
                contents="Open https://rfpnotification.com and join the waiting list by entering the email address: [test_user@example.com]",
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[mcp_client.session],  # Pass the FastMCP client session
                    automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                        maximum_remote_calls=20  # Increase from default
                    ),
                ),
            )
            for part in response.candidates[0].content.parts:
                print(part)
        except Exception as e:
            print(e)
            logger.error(e)


asyncio.run(main())
