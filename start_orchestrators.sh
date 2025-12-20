#!/bin/bash
# FIELD Sacred Pyramid Orchestrator Startup

echo "════════════════════════════════════════"
echo "FIELD Sacred Pyramid Orchestrators"
echo "════════════════════════════════════════"
echo

echo "Starting custom MCP orchestrators..."
echo

echo "◼︎ Starting DOJO (Port 8766 - 741 Hz)..."
python3 ~/FIELD-macOS-DOJO/mcp/server.py > ~/FIELD-macOS-DOJO/logs/dojo.log 2>&1 &
DOJO_PID=$!
echo "   PID: $DOJO_PID"

echo "◻ Starting Akron Gateway (Port 8396 - 396 Hz)..."
python3 ~/FIELD-macOS-DOJO/akron-gateway/server.py > ~/FIELD-macOS-DOJO/logs/akron.log 2>&1 &
AKRON_PID=$!
echo "   PID: $AKRON_PID"

echo "⊗ Starting King's Chamber (Port 8852 - 852 Hz)..."
python3 ~/FIELD-macOS-DOJO/kings-chamber/server.py > ~/FIELD-macOS-DOJO/logs/kings-chamber.log 2>&1 &
CHAMBER_PID=$!
echo "   PID: $CHAMBER_PID"

echo
echo "Waiting for servers to initialize..."
sleep 3

echo
echo "════════════════════════════════════════"
echo "Verification"
echo "════════════════════════════════════════"

for port in 8766 8396 8852; do
    if lsof -i :$port > /dev/null 2>&1; then
        echo "✅ Port $port - OPERATIONAL"
    else
        echo "❌ Port $port - NOT RESPONDING"
    fi
done

echo
echo "════════════════════════════════════════"
echo "Sacred Pyramid Status"
echo "════════════════════════════════════════"
echo
echo "           ◼︎ DOJO (8766)"
echo "          /    741 Hz   \\"
echo "         /               \\"
echo "        /    ⊗ King's    \\     ← Bridge"
echo "       /    Chamber       \\"
echo "      /      (8852)        \\"
echo "     /                      \\"
echo "   ●----------▼----------▲"
echo "   |                      |"
echo "◻ Akron (8396)"
echo
echo "All orchestrators operational."
echo "Logs: ~/FIELD-macOS-DOJO/logs/"
echo
