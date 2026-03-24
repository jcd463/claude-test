"""Proof that the GitHub MCP server is wired up and working."""

MCP_STATUS = "connected"
REPO = "jcd463/claude-test"

if __name__ == "__main__":
    print(f"MCP status : {MCP_STATUS}")
    print(f"Repo       : {REPO}")
    print("If you're reading this in GitHub, the MCP server works.")
