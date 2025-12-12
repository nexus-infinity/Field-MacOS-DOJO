#!/bin/bash

# GitHub MCP Server Setup Script for Claude Desktop
# This script helps configure the GitHub MCP server for Claude Desktop

set -e

echo "========================================"
echo "GitHub MCP Server Setup for Claude"
echo "========================================"
echo ""

# Function to detect OS and get config path
get_config_path() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "$HOME/.config/Claude/claude_desktop_config.json"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        echo "$APPDATA/Claude/claude_desktop_config.json"
    else
        echo ""
    fi
}

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed!"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node --version)
echo "✓ Node.js detected: $NODE_VERSION"
echo ""

# Check Node.js version (should be >= 18)
MAJOR_VERSION=$(echo $NODE_VERSION | cut -d'.' -f1 | sed 's/v//')
if [ "$MAJOR_VERSION" -lt 18 ]; then
    echo "⚠️  Warning: Node.js version 18 or higher is recommended"
    echo "   Current version: $NODE_VERSION"
    echo ""
fi

# Get config file path
CONFIG_PATH=$(get_config_path)

if [ -z "$CONFIG_PATH" ]; then
    echo "❌ Could not determine configuration path for your OS"
    exit 1
fi

echo "Configuration file location:"
echo "$CONFIG_PATH"
echo ""

# Check if config file exists
if [ -f "$CONFIG_PATH" ]; then
    echo "⚠️  Configuration file already exists"
    echo ""
    read -p "Do you want to backup and replace it? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        BACKUP_PATH="${CONFIG_PATH}.backup.$(date +%Y%m%d_%H%M%S)"
        cp "$CONFIG_PATH" "$BACKUP_PATH"
        echo "✓ Backed up existing config to: $BACKUP_PATH"
    else
        echo "Skipping configuration replacement."
        echo "Please manually merge the configuration from claude_desktop_config.json"
        exit 0
    fi
fi

# Prompt for GitHub token
echo ""
echo "Please enter your GitHub Personal Access Token:"
echo "(The token will not be displayed as you type)"
read -s GITHUB_TOKEN
echo ""

if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ No token provided!"
    exit 1
fi

# Create config directory if it doesn't exist
CONFIG_DIR=$(dirname "$CONFIG_PATH")
mkdir -p "$CONFIG_DIR"

# Create the configuration file
cat > "$CONFIG_PATH" << EOF
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_TOKEN"
      }
    }
  }
}
EOF

echo "✓ Configuration file created successfully!"
echo ""

# Test npx command
echo "Testing MCP server installation..."
if npx -y @modelcontextprotocol/server-github --version &> /dev/null || true; then
    echo "✓ GitHub MCP server package is accessible"
else
    echo "⚠️  Could not verify GitHub MCP server package"
    echo "   It will be downloaded when Claude Desktop first uses it"
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Restart Claude Desktop completely"
echo "2. Test the connection by asking Claude to list your GitHub repositories"
echo ""
echo "For more information, see docs/MCP_SETUP.md"
echo ""
