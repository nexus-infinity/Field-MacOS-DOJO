# GitHub MCP Server Quick Reference

## One-Line Setup

```bash
./setup_github_mcp.sh
```

## Quick Diagnostics

```bash
./diagnose_mcp.sh
```

## Configuration Locations

| OS | Path |
|---|---|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |

## Minimal Configuration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

## GitHub Token Scopes Required

- ✅ `repo` - Full control of private repositories
- ✅ `read:org` - Read org and team membership  
- ✅ `read:user` - Read user profile data
- ✅ `user:email` - Access user email addresses

## Create Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes listed above
4. Copy token immediately

## Testing the Connection

After setup, restart Claude Desktop and try:

```
"List my GitHub repositories"
"Show me the README from my-repo"
"What are the open issues in my-repo?"
```

## Common Issues

| Issue | Solution |
|---|---|
| MCP not appearing | Restart Claude Desktop completely (quit, not just close) |
| Authentication failed | Check token validity at github.com/settings/tokens |
| Command not found: npx | Install Node.js from nodejs.org |
| Invalid JSON | Run `python3 -m json.tool config.json` to validate |

## File Structure

```
.
├── claude_desktop_config.json    # Template configuration
├── setup_github_mcp.sh           # Automated setup script
├── diagnose_mcp.sh               # Diagnostic tool
├── .env.example                  # Environment template
└── docs/
    ├── MCP_SETUP.md             # Detailed setup guide
    ├── MCP_TROUBLESHOOTING.md   # Troubleshooting guide
    └── MCP_QUICK_REFERENCE.md   # This file
```

## Environment Variables (Optional)

Instead of editing the config file directly, you can use environment variables:

1. Copy `.env.example` to `.env`
2. Add your token: `GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token`
3. Source it before running Claude: `source .env`

## Additional MCP Servers

Add more servers to the same config:

```json
{
  "mcpServers": {
    "github": { /* ... */ },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    }
  }
}
```

## Getting Help

- 📖 Detailed setup: `docs/MCP_SETUP.md`
- 🔧 Troubleshooting: `docs/MCP_TROUBLESHOOTING.md`
- 🐛 Run diagnostics: `./diagnose_mcp.sh`
- 💬 GitHub Issues: https://github.com/modelcontextprotocol/servers/issues

## Security Reminders

- ⚠️ Never commit tokens to git
- 🔒 Use minimal required scopes
- 🔄 Rotate tokens regularly
- 👁️ Monitor token usage in GitHub settings
