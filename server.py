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

provider = FileSystemProvider(root=Path(__file__).parent / "mcp_server", reload=True)

mcp_Server = FastMCP(
    "rfp_notifications",
    providers=[provider],
)

client = Client(mcp_Server)

gemini_client = genai.Client(api_key=gemini_api_key)

logger = logging.getLogger(__name__)


# async def main():
#     async with client:
#         # Basic server interaction
#         await client.ping()
#         await client.call_tool("initialize_driver", {})

#         # List available operations
#         tools = await client.list_tools()
#         resources = await client.list_resources()
#         prompts = await client.list_prompts()

#         # Execute operations
#         try:
#             await client.call_tool("open_url", {"url": "https://rfpnotification.com"})
#             await client.call_tool("save_webpage_as_pdf", {})
#             await client.call_tool("close_driver", {})
#         except Exception as e:
#             logger.error(e)


async def main():
    async with client:
        try:
            response = await gemini_client.aio.models.generate_content(
                model="gemini-3.1-flash-lite-preview",
                contents="open and save https://rfpnotification.com as pdf and markdown. Close the driver after performing the task",
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[client.session],  # Pass the FastMCP client session
                ),
            )
            print(response.text)
        except Exception as e:
            logger.error(e)


asyncio.run(main())
