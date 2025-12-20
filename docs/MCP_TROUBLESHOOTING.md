# GitHub MCP Server Troubleshooting Guide

## Common Issues and Solutions

### 1. MCP Server Not Appearing in Claude Desktop

**Symptoms:**
- Claude Desktop doesn't show GitHub integration
- No GitHub-related capabilities available

**Solutions:**

1. **Verify configuration file location:**
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. **Check JSON syntax:**
   ```bash
   # On macOS/Linux
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json | python3 -m json.tool
   ```

3. **Ensure proper formatting:**
   - No trailing commas
   - Double quotes only (no single quotes)
   - Proper nesting

4. **Restart Claude Desktop completely:**
   - Quit application (not just close window)
   - Relaunch from Applications/Start Menu

### 2. Authentication Errors

**Symptoms:**
- "Authentication failed" messages
- "Invalid token" errors

**Solutions:**

1. **Verify token hasn't expired:**
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Check if token is still active

2. **Check token permissions:**
   Required scopes:
   - `repo` - Full control of private repositories
   - `read:org` - Read org and team membership
   - `read:user` - Read user profile data
   - `user:email` - Access user email addresses

3. **Regenerate token if needed:**
   - Delete old token
   - Create new one with correct scopes
   - Update configuration file

4. **Check for special characters:**
   - Ensure token is copied correctly
   - No extra spaces or newlines
   - Token should start with `ghp_`

### 3. Node.js/NPX Issues

**Symptoms:**
- "Command not found: npx"
- "Node.js version error"

**Solutions:**

1. **Install Node.js:**
   ```bash
   # Check if Node.js is installed
   node --version
   
   # Should be v18.0.0 or higher
   ```
   
   Download from: https://nodejs.org/

2. **Verify npx is available:**
   ```bash
   npx --version
   ```

3. **Update npm:**
   ```bash
   npm install -g npm@latest
   ```

4. **Clear npx cache:**
   ```bash
   npx clear-npx-cache
   ```

### 4. MCP Server Crashes

**Symptoms:**
- Server starts but immediately crashes
- "MCP server exited with error" messages

**Solutions:**

1. **Check Node.js version:**
   ```bash
   node --version
   # Must be v18.0.0 or higher
   ```

2. **Test server manually:**
   ```bash
   npx -y @modelcontextprotocol/server-github
   ```

3. **Clear npm cache:**
   ```bash
   npm cache clean --force
   ```

4. **Reinstall MCP package:**
   ```bash
   npm uninstall -g @modelcontextprotocol/server-github
   npx -y @modelcontextprotocol/server-github
   ```

### 5. Network/Firewall Issues

**Symptoms:**
- Cannot connect to GitHub
- Timeout errors

**Solutions:**

1. **Check internet connection:**
   ```bash
   ping github.com
   ```

2. **Check GitHub status:**
   - Visit: https://www.githubstatus.com/

3. **Configure proxy if needed:**
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token",
           "HTTP_PROXY": "http://proxy.example.com:8080",
           "HTTPS_PROXY": "http://proxy.example.com:8080"
         }
       }
     }
   }
   ```

4. **Check firewall settings:**
   - Allow Node.js/npx through firewall
   - Allow connections to github.com

### 6. Permission Issues

**Symptoms:**
- "Access denied" errors
- Cannot read/write configuration file

**Solutions:**

1. **Check file permissions:**
   ```bash
   # macOS/Linux
   ls -la ~/Library/Application\ Support/Claude/
   chmod 644 ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. **Create directory if missing:**
   ```bash
   # macOS
   mkdir -p ~/Library/Application\ Support/Claude/
   
   # Linux
   mkdir -p ~/.config/Claude/
   ```

3. **Run with proper user:**
   - Don't run Claude Desktop as root/administrator
   - Use regular user account

### 7. Multiple MCP Servers Configuration

**Symptoms:**
- Other MCP servers stop working
- Configuration conflicts

**Solutions:**

1. **Proper format for multiple servers:**
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_PERSONAL_ACCESS_TOKEN": "token1"
         }
       },
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
       },
       "other-server": {
         "command": "other-command",
         "args": ["arg1", "arg2"]
       }
     }
   }
   ```

2. **Test each server individually:**
   - Comment out other servers
   - Test one at a time
   - Add back gradually

### 8. Rate Limiting

**Symptoms:**
- "Rate limit exceeded" errors
- Slow responses from GitHub

**Solutions:**

1. **Check rate limit status:**
   ```bash
   curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit
   ```

2. **Wait for reset:**
   - GitHub has hourly rate limits
   - Authenticated requests: 5,000/hour
   - Check `X-RateLimit-Reset` header

3. **Use authenticated token:**
   - Always include GITHUB_PERSONAL_ACCESS_TOKEN
   - Authenticated requests have higher limits

## Debugging Steps

### Enable Verbose Logging

1. **Check Claude Desktop logs:**
   - macOS: `~/Library/Logs/Claude/`
   - Windows: `%APPDATA%\Claude\logs\`
   - Linux: `~/.config/Claude/logs/`

2. **Test MCP server directly:**
   ```bash
   GITHUB_PERSONAL_ACCESS_TOKEN="your_token" npx -y @modelcontextprotocol/server-github
   ```

3. **Validate configuration:**
   ```bash
   python3 -m json.tool < ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

### Collecting Information for Support

When reporting issues, include:

1. **System information:**
   - Operating system and version
   - Node.js version (`node --version`)
   - npm version (`npm --version`)
   - Claude Desktop version

2. **Configuration:**
   - Content of `claude_desktop_config.json` (redact token!)
   - Any error messages from logs

3. **Steps to reproduce:**
   - What you did
   - What you expected
   - What actually happened

4. **Testing results:**
   - Can you run npx manually?
   - Does the token work with GitHub API?
   - Are other MCP servers working?

## Quick Diagnostic Script

Save this as `diagnose_mcp.sh`:

```bash
#!/bin/bash

echo "=== MCP Server Diagnostic ==="
echo ""

echo "1. Node.js version:"
node --version || echo "❌ Node.js not found"
echo ""

echo "2. NPX version:"
npx --version || echo "❌ NPX not found"
echo ""

echo "3. Configuration file exists:"
if [[ "$OSTYPE" == "darwin"* ]]; then
    CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    CONFIG="$HOME/.config/Claude/claude_desktop_config.json"
fi

if [ -f "$CONFIG" ]; then
    echo "✓ Found: $CONFIG"
    echo ""
    echo "4. JSON validation:"
    cat "$CONFIG" | python3 -m json.tool > /dev/null && echo "✓ Valid JSON" || echo "❌ Invalid JSON"
else
    echo "❌ Not found: $CONFIG"
fi
echo ""

echo "5. GitHub API connectivity:"
curl -s https://api.github.com/zen > /dev/null && echo "✓ GitHub API reachable" || echo "❌ Cannot reach GitHub API"
echo ""

echo "6. MCP package test:"
npx -y @modelcontextprotocol/server-github --version 2>&1 | head -1 || echo "❌ Cannot run MCP package"
```

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Claude Desktop Support](https://support.anthropic.com/)
- [Node.js Downloads](https://nodejs.org/)

## Still Having Issues?

If none of these solutions work:

1. Try the automated setup script: `./setup_github_mcp.sh`
2. Review the detailed setup guide: `docs/MCP_SETUP.md`
3. Check GitHub MCP server issues: https://github.com/modelcontextprotocol/servers/issues
4. Contact Claude Desktop support with diagnostic information
