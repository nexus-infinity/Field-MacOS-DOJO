# Universal Framework

## Overview

Universal Framework is a comprehensive, multi-platform project designed to support various deployment targets while maintaining a shared codebase. It includes modules for web, mobile, desktop, and other platforms, with a focus on modularity and extensive testing. The project is uniquely enhanced by an integrated AI management system that automates various aspects of development and maintenance.

## Project Structure

For a detailed overview of the project structure, please refer to the `project-structure.txt` file in the root directory. This file provides a comprehensive layout of all directories and key files in the project.

## AI Management System

Our project leverages a sophisticated AI management system that enhances various aspects of the development lifecycle:

- Automated code review and optimization
- Intelligent test generation and execution
- Dynamic resource allocation and scaling
- Predictive maintenance and error detection
- Natural language processing for documentation and query handling

For detailed information on how to use and configure the AI system, please refer to the [AI_INTEGRATION.md](./AI_INTEGRATION.md) file.

## Getting Started with AI Integration

1. Initialize the AI system: `npm run ai-init`
2. Run AI-powered code review: `npm run ai-review`
3. Generate AI-enhanced tests: `npm run ai-test`
4. Create AI-generated documentation: `npm run ai-docs`
5. Perform AI-driven performance optimization: `npm run ai-optimize`
6. Conduct AI security analysis: `npm run ai-security`
7. Update the AI system: `npm run ai-update`

## Configuration

AI-specific configuration can be found in `config/ai-config.json`. Adjust these settings to fine-tune the AI system's behavior.

## Best Practices for AI Integration

- Regularly run AI-powered code reviews before submitting pull requests
- Utilize AI-generated tests to complement manual test writing
- Keep the AI configuration up-to-date as the project evolves
- Provide feedback on AI-generated content to improve system accuracy
- Integrate AI-powered documentation generation into your workflow

## GitHub MCP Server Setup (Claude Desktop)

This repository includes configuration for the GitHub MCP (Model Context Protocol) server, which allows Claude Desktop to interact directly with GitHub repositories.

### Quick Setup

Run the automated setup script:

```bash
./setup_github_mcp.sh
```

This script will:
- Check for Node.js installation
- Prompt for your GitHub Personal Access Token
- Configure Claude Desktop with the GitHub MCP server
- Backup any existing configuration

### Manual Setup

For manual configuration or troubleshooting, see the detailed guide:
- [MCP Setup Documentation](./docs/MCP_SETUP.md)

### What You'll Need

1. **Claude Desktop** - Install from [Claude.ai](https://claude.ai)
2. **Node.js 18+** - Download from [nodejs.org](https://nodejs.org/)
3. **GitHub Personal Access Token** - Create one with `repo` and `read:org` scopes

### Quick Start

After setup, restart Claude Desktop and try:
- "List my GitHub repositories"
- "Show me the README from [repository-name]"
- "What are the open issues in [repository-name]?"