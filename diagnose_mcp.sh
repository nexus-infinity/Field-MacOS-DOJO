#!/bin/bash

# MCP Server Diagnostic Script
# This script checks the environment and configuration for GitHub MCP server

echo "================================================"
echo "GitHub MCP Server Diagnostic Tool"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print success
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Function to print error
print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Function to print warning
print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Function to get config path
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

ISSUES_FOUND=0

# Check 1: Node.js
echo "1. Checking Node.js installation..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    MAJOR_VERSION=$(echo $NODE_VERSION | cut -d'.' -f1 | sed 's/v//')
    print_success "Node.js installed: $NODE_VERSION"
    
    if [ "$MAJOR_VERSION" -lt 18 ]; then
        print_warning "Node.js version 18 or higher is recommended (current: $NODE_VERSION)"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
else
    print_error "Node.js is not installed"
    echo "   Install from: https://nodejs.org/"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
fi
echo ""

# Check 2: NPX
echo "2. Checking NPX availability..."
if command -v npx &> /dev/null; then
    NPX_VERSION=$(npx --version)
    print_success "NPX is available: $NPX_VERSION"
else
    print_error "NPX is not available"
    echo "   NPX comes with Node.js - please reinstall Node.js"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
fi
echo ""

# Check 3: Configuration file
echo "3. Checking Claude Desktop configuration..."
CONFIG_PATH=$(get_config_path)

if [ -z "$CONFIG_PATH" ]; then
    print_error "Could not determine configuration path for your OS"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
else
    echo "   Expected location: $CONFIG_PATH"
    
    if [ -f "$CONFIG_PATH" ]; then
        print_success "Configuration file exists"
        
        # Validate JSON
        if command -v python3 &> /dev/null; then
            if python3 -m json.tool "$CONFIG_PATH" > /dev/null 2>&1; then
                print_success "Configuration is valid JSON"
                
                # Check for GitHub MCP server entry
                if grep -q "github" "$CONFIG_PATH" 2>/dev/null; then
                    print_success "GitHub MCP server entry found"
                    
                    # Check for token placeholder (with or without angle brackets)
                    if grep -q "<YOUR_GITHUB_TOKEN_HERE>\|YOUR_GITHUB_TOKEN_HERE" "$CONFIG_PATH" 2>/dev/null; then
                        print_warning "GitHub token placeholder detected - replace with actual token"
                        ISSUES_FOUND=$((ISSUES_FOUND + 1))
                    fi
                else
                    print_warning "No GitHub MCP server entry found in configuration"
                    ISSUES_FOUND=$((ISSUES_FOUND + 1))
                fi
            else
                print_error "Configuration file contains invalid JSON"
                echo "   Run: python3 -m json.tool \"$CONFIG_PATH\" to see errors"
                ISSUES_FOUND=$((ISSUES_FOUND + 1))
            fi
        else
            print_warning "Cannot validate JSON (python3 not found)"
        fi
    else
        print_warning "Configuration file does not exist"
        echo "   Run ./setup_github_mcp.sh to create it"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
fi
echo ""

# Check 4: GitHub API connectivity
echo "4. Checking GitHub API connectivity..."
if command -v curl &> /dev/null; then
    if curl -s --max-time 5 https://api.github.com/zen > /dev/null 2>&1; then
        print_success "GitHub API is reachable"
    else
        print_error "Cannot connect to GitHub API"
        echo "   Check your internet connection and firewall settings"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
else
    print_warning "curl not found - cannot test GitHub connectivity"
fi
echo ""

# Check 5: MCP package accessibility
echo "5. Checking GitHub MCP package..."
if command -v npx &> /dev/null; then
    # Skip the lengthy package check, just note it will be downloaded on demand
    print_success "NPX is available - MCP package will download automatically on first use"
fi
echo ""

# Check 6: Environment variables (if .env exists)
echo "6. Checking environment configuration..."
if [ -f ".env" ]; then
    print_success ".env file exists"
    
    if grep -q "GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token_here" ".env" 2>/dev/null; then
        print_warning "GitHub token placeholder in .env - replace with actual token"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    elif grep -q "GITHUB_PERSONAL_ACCESS_TOKEN=" ".env" 2>/dev/null; then
        print_success "GitHub token configured in .env"
    fi
else
    print_warning ".env file not found"
    echo "   Create from .env.example if needed"
fi
echo ""

# Summary
echo "================================================"
echo "Diagnostic Summary"
echo "================================================"
echo ""

if [ $ISSUES_FOUND -eq 0 ]; then
    print_success "No issues found! Your setup appears to be correct."
    echo ""
    echo "Next steps:"
    echo "1. Make sure Claude Desktop is completely restarted"
    echo "2. Test by asking Claude to list your GitHub repositories"
else
    print_warning "Found $ISSUES_FOUND potential issue(s)"
    echo ""
    echo "Recommended actions:"
    echo "1. Address the issues listed above"
    echo "2. Run ./setup_github_mcp.sh for automated setup"
    echo "3. See docs/MCP_TROUBLESHOOTING.md for detailed help"
fi
echo ""

# System information
echo "================================================"
echo "System Information"
echo "================================================"
echo ""
echo "Operating System: $OSTYPE"
echo "Shell: $SHELL"
if command -v node &> /dev/null; then
    echo "Node.js: $(node --version)"
fi
if command -v npm &> /dev/null; then
    echo "npm: $(npm --version)"
fi
echo ""
