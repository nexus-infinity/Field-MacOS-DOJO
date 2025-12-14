#!/bin/bash
# .field/scripts/discover.sh
# DISCOVERS existing FIELD structure - doesn't create

echo "🔍 Discovering FIELD structure..."
echo ""

# Check directories
DIRS=(
  "$HOME/FIELD"
  "$HOME/FIELD-DEV"
  "$HOME/FIELD-LIVING"
  "$HOME/SACRED"
  "$HOME/.field"
)

for dir in "${DIRS[@]}"; do
  if [ -d "$dir" ]; then
    echo "✓ Found: $dir"
    ls -1 "$dir" 2>/dev/null | head -5 | sed 's/^/    /'
  else
    echo "○ Not found: $dir (will not create)"
  fi
done

echo ""
echo "🔍 Discovering running agents..."

# Check common ports
PORTS=(2850 3960 4320 5280 6390 9630 43200)
for port in "${PORTS[@]}"; do
  if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "✓ Port $port: Active"
  else
    echo "○ Port $port: Available"
  fi
done

echo ""
echo "✅ Discovery complete"