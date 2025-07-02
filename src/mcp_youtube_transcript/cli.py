#  cli.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php
import click
import uvicorn

from mcp_youtube_transcript import server


@click.command()
@click.option(
    "--webshare-proxy-username",
    metavar="NAME",
    envvar="WEBSHARE_PROXY_USERNAME",
    help="Webshare proxy service username.",
)
@click.option(
    "--webshare-proxy-password",
    metavar="PASSWORD",
    envvar="WEBSHARE_PROXY_PASSWORD",
    help="Webshare proxy service password.",
)
@click.option("--http-proxy", metavar="URL", envvar="HTTP_PROXY", help="HTTP proxy server URL.")
@click.option("--https-proxy", metavar="URL", envvar="HTTPS_PROXY", help="HTTPS proxy server URL.")
@click.version_option()
def main(
    webshare_proxy_username: str | None,
    webshare_proxy_password: str | None,
    http_proxy: str | None,
    https_proxy: str | None,
) -> None:
    """YouTube Transcript MCP server."""
    mcp = server(webshare_proxy_username, webshare_proxy_password, http_proxy, https_proxy)
    uvicorn.run(mcp.streamable_http_app, host="0.0.0.0", port=8080, log_level="info")
