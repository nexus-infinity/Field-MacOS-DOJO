# GitHub MCP Server Setup Guide

## Overview

This guide explains how to set up the GitHub MCP (Model Context Protocol) server for use with Claude Desktop, allowing Claude to interact with GitHub repositories directly.

## Prerequisites

- Claude Desktop application installed
- Node.js and npm installed (version 18 or higher)
- GitHub Personal Access Token

## Step 1: Create a GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Claude MCP Server")
4. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org and team membership)
   - `read:user` (Read user profile data)
   - `user:email` (Access user email addresses)
5. Click "Generate token"
6. **Important**: Copy the token immediately - you won't be able to see it again!

## Step 2: Locate Claude Desktop Configuration

The Claude Desktop configuration file is located at:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

## Step 3: Configure the GitHub MCP Server

1. If the configuration file doesn't exist, create it
2. Copy the contents from `claude_desktop_config.json` in this repository
3. Replace `<YOUR_GITHUB_TOKEN_HERE>` with your actual GitHub Personal Access Token
4. Save the file

### Example Configuration

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

## Step 4: Restart Claude Desktop

After saving the configuration:

1. Completely quit Claude Desktop
2. Relaunch the application
3. The GitHub MCP server should now be available

## Verifying the Connection

Once Claude Desktop restarts, you can verify the connection by asking Claude to:

- List repositories in your GitHub account
- Get information about a specific repository
- Read files from a repository
- Check pull requests or issues

Example prompts:
- "List my GitHub repositories"
- "Show me the README file from repository X"
- "What are the open pull requests in repository Y?"

## Troubleshooting

### MCP Server Not Connecting

1. **Check token validity**: Ensure your GitHub token hasn't expired
2. **Verify token permissions**: Make sure the token has the required scopes
3. **Check Node.js installation**: Run `node --version` to confirm Node.js is installed
4. **Review Claude logs**: Check Claude Desktop's logs for error messages
5. **Test npx command**: Run `npx -y @modelcontextprotocol/server-github` manually to test

### Common Issues

**Issue**: "Command not found: npx"
- **Solution**: Install Node.js from https://nodejs.org/

**Issue**: "Authentication failed"
- **Solution**: Double-check your GitHub token is correct and has proper scopes

**Issue**: "MCP server crashed"
- **Solution**: Ensure you're using Node.js version 18 or higher

### Configuration File Format

The configuration file must be valid JSON. Common mistakes:
- Missing commas between entries
- Trailing commas (not allowed in JSON)
- Incorrect quote types (must use double quotes)
- Unescaped special characters

## Additional MCP Servers

You can add multiple MCP servers to the same configuration file:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    }
  }
}
```

## Security Best Practices

1. **Never commit tokens to git**: Keep your tokens secure and private
2. **Use environment variables**: Consider using a separate env file for tokens
3. **Rotate tokens regularly**: Generate new tokens periodically
4. **Use minimal scopes**: Only grant the permissions actually needed
5. **Monitor token usage**: Check GitHub settings for token activity

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [GitHub MCP Server Repository](https://github.com/modelcontextprotocol/servers)
- [Claude Desktop Documentation](https://docs.anthropic.com/claude/docs)

## Support

If you continue to experience issues:

1. Check the GitHub MCP server issues page
2. Review Claude Desktop documentation
3. Contact support with:
   - Your operating system
   - Node.js version (`node --version`)
   - Claude Desktop version
   - Error messages from logs
