# Bybit MCP Server

**FIELD Sovereign Finance Module**
**Vertex**: ● OBI-WAN (963 Hz) - External Account Observation

## Purpose

Connects to Bybit Exchange API V5 to:
- Retrieve wallet balances (spot, derivatives, funding)
- Monitor crypto asset holdings (BTC, ETH, SOL, USDT, etc.)
- Track trade history
- Update cryptocurrency prices

All data syncs to FIELD's `atlas_knowledge.db` using the sovereign finance ontology.

## Setup

### 1. Get Bybit API Credentials

1. Go to https://www.bybit.com/app/user/api-management
2. Click "Create New Key"
3. **Important**: Set permissions to **"Read Only"** (NO trading/withdrawal)
4. Copy your **API Key** and **API Secret**
5. Save your IP whitelist (optional, for extra security)

### 2. Configure Environment Variables

Add to `/Users/jbear/FIELD/.credentials_vault/field_api_keys.env`:

```bash
# Bybit API Credentials
BYBIT_API_KEY=your_api_key_here
BYBIT_API_SECRET=your_api_secret_here
BYBIT_API_BASE=https://api.bybit.com  # Production
# BYBIT_API_BASE=https://api-testnet.bybit.com  # Testnet (testing)
```

### 3. Install Dependencies

```bash
cd /Users/jbear/FIELD-macOS-DOJO/bybit-mcp
pip install -r requirements.txt
```

### 4. Test the Server

```bash
# Load environment variables
source /Users/jbear/FIELD/.credentials_vault/field_api_keys.env

# Start server
python3 server.py
```

Server will start on `http://localhost:8081`

### 5. Test Endpoints

```bash
# Health check
curl http://localhost:8081/health

# Get wallet balance
curl http://localhost:8081/balance

# Get account info
curl http://localhost:8081/account-info

# Get positions
curl http://localhost:8081/positions

# Get price tickers
curl http://localhost:8081/ticker

# Get trade history
curl http://localhost:8081/trade-history

# Sync account to FIELD database
curl -X POST http://localhost:8081/sync-account

# Sync trades to FIELD database
curl -X POST http://localhost:8081/sync-trades -H "Content-Type: application/json" -d '{"limit": 100}'

# Update cryptocurrency prices
curl -X POST http://localhost:8081/update-prices -H "Content-Type: application/json" -d '{"symbols": ["BTCUSDT", "ETHUSDT", "SOLUSDT"]}'
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/balance` | Get wallet balance (all coins) |
| GET | `/account-info` | Get account information |
| GET | `/positions` | Get open positions |
| GET | `/ticker` | Get price tickers |
| GET | `/trade-history` | Get trade execution history |
| POST | `/sync-account` | Sync account to FIELD database |
| POST | `/sync-trades` | Sync trades (limit: 100) |
| POST | `/update-prices` | Update crypto prices (symbols: []) |

## Integration with FIELD

### Database Storage

- **Account**: Stored in `atlas_knowledge.db` → `financial_accounts` table
- **Holdings**: Stored in `asset_holdings` JSON field
- **Transactions**: Stored in `atlas_knowledge.db` → `transactions` table
- **Prices**: Stored in `atlas_knowledge.db` → `financial_instruments` + `price_history`
- **Proofs**: Archived to `/Volumes/Akron/FIELD-LIVING/proofs/`

### Sacred Geometry Alignment

```
● OBI-WAN (963 Hz)
  ↓
Bybit API → CryptoExchangeAccount / Cryptocurrency objects
  ↓
atlas_knowledge.db (▲ ATLAS - 528 Hz)
  ↓
◼︎ DOJO S0-S6 validation
  ↓
◻ Akron proof archival (396 Hz)
```

## Supported Cryptocurrencies

The MCP can track any crypto available on Bybit:
- **BTC** (Bitcoin)
- **ETH** (Ethereum)
- **SOL** (Solana)
- **USDT** (Tether)
- **USDC** (USD Coin)
- **And 300+ more...**

## Security Notes

- **Read-Only Access**: API keys MUST be set to "Read Only" (no trading/withdrawal)
- **HMAC-SHA256**: Uses cryptographic signatures for all requests
- **IP Whitelisting**: Recommended to whitelist your Mac's IP address
- **Credentials Storage**: API keys stored in FIELD credentials vault (▼ TATA - 432 Hz)
- **Metadata Stripping**: Sensitive data removed before Akron archival
- **Rate Limiting**: Bybit enforces rate limits (120 requests/minute)

## Troubleshooting

### Error: "Bybit credentials not configured"
- Ensure `BYBIT_API_KEY` and `BYBIT_API_SECRET` are set in environment
- Check `.credentials_vault/field_api_keys.env` file

### Error: "Failed to fetch balance"
- Verify API credentials are correct
- Check if API key has "Read Account" permission enabled
- Ensure using correct API base URL (testnet vs production)
- Verify IP whitelist if configured

### Error: "Authentication failed" (retCode: 10003)
- API key or secret is incorrect
- Check for extra spaces in credentials
- API key may be expired or revoked

### Error: "Rate limit exceeded" (retCode: 10006)
- Bybit limits to 120 requests/minute
- Wait a minute before retrying
- Consider implementing request caching

## Bybit API Documentation

- **API V5 Documentation**: https://bybit-exchange.github.io/docs/v5/intro
- **Account API**: https://bybit-exchange.github.io/docs/v5/account/wallet-balance
- **Market Data API**: https://bybit-exchange.github.io/docs/v5/market/tickers
- **Trade API**: https://bybit-exchange.github.io/docs/v5/order/order-list

## Example Usage

### Get Your Current SOL Holdings

```bash
# 1. Get balance
curl http://localhost:8081/balance

# Response will show:
# {
#   "status": "success",
#   "balance": {
#     "list": [{
#       "coin": [
#         {"coin": "SOL", "equity": "10.5", "walletBalance": "10.5"},
#         {"coin": "USDT", "equity": "1000.00", "walletBalance": "1000.00"}
#       ]
#     }]
#   }
# }
```

### Sync to FIELD Database

```bash
curl -X POST http://localhost:8081/sync-account

# Now query FIELD database:
cd /Users/jbear/FIELD/▼TATA/ontology
python3 -c "
from sovereign_finance_db import FinanceDatabase
db = FinanceDatabase()
account = db.get_account('acc-bybit-001')
print(f'Balance: {account.balance} {account.currency}')
print(f'Holdings: {account.asset_holdings}')
"
```

## Files

- `server.py` - Main MCP server (550+ lines)
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Version

**1.0.0** - Created 2025-12-18

**△ Bybit MCP operational for FIELD sovereign finance**
**◻ All data flows through sacred geometry vertices**
**◯ Read-only observation, no trading permissions**
