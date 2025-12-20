# PayPal MCP Server

**FIELD Sovereign Finance Module**
**Vertex**: ● OBI-WAN (963 Hz) - External Account Observation

## Purpose

Connects to PayPal REST API to:
- Retrieve transaction history
- Check account balances
- Monitor gift card status
- Track payment method tokens

All data syncs to FIELD's `atlas_knowledge.db` using the sovereign finance ontology.

## Setup

### 1. Get PayPal API Credentials

1. Go to https://developer.paypal.com/dashboard/applications
2. Create a new app (or use existing)
3. Copy your **Client ID** and **Client Secret**

### 2. Configure Environment Variables

Add to `/Users/jbear/FIELD/.credentials_vault/field_api_keys.env`:

```bash
# PayPal API Credentials
PAYPAL_CLIENT_ID=your_client_id_here
PAYPAL_CLIENT_SECRET=your_client_secret_here
PAYPAL_API_BASE=https://api-m.paypal.com  # Production
# PAYPAL_API_BASE=https://api-m.sandbox.paypal.com  # Sandbox (testing)
```

### 3. Install Dependencies

```bash
cd /Users/jbear/FIELD-macOS-DOJO/paypal-mcp
pip install -r requirements.txt
```

### 4. Test the Server

```bash
# Load environment variables
source /Users/jbear/FIELD/.credentials_vault/field_api_keys.env

# Start server
python3 server.py
```

Server will start on `http://localhost:8080`

### 5. Test Endpoints

```bash
# Health check
curl http://localhost:8080/health

# Get balance
curl http://localhost:8080/balance

# List transactions (last 30 days)
curl http://localhost:8080/transactions

# List gift cards (payment tokens)
curl http://localhost:8080/gift-cards

# Sync account to FIELD database
curl -X POST http://localhost:8080/sync-account

# Sync transactions to FIELD database
curl -X POST http://localhost:8080/sync-transactions -H "Content-Type: application/json" -d '{"days": 30}'
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/balance` | Get PayPal account balance |
| GET | `/transactions` | List transactions (last 30 days) |
| GET | `/gift-cards` | List payment tokens (gift cards) |
| POST | `/sync-account` | Sync account to FIELD database |
| POST | `/sync-transactions` | Sync transactions (days: 30) |

## Integration with FIELD

### Database Storage

- **Account**: Stored in `atlas_knowledge.db` → `financial_accounts` table
- **Transactions**: Stored in `atlas_knowledge.db` → `transactions` table
- **Proofs**: Archived to `/Volumes/Akron/FIELD-LIVING/proofs/`

### Sacred Geometry Alignment

```
● OBI-WAN (963 Hz)
  ↓
PayPal API → DigitalWallet / GiftCard objects
  ↓
atlas_knowledge.db (▲ ATLAS - 528 Hz)
  ↓
◼︎ DOJO S0-S6 validation
  ↓
◻ Akron proof archival (396 Hz)
```

## Security Notes

- **Read-Only Access**: This MCP only reads data from PayPal (no write/withdraw permissions)
- **Credentials Storage**: API keys stored in FIELD credentials vault (▼ TATA - 432 Hz)
- **Metadata Stripping**: Sensitive data removed before Akron archival
- **OAuth 2.0**: Uses PayPal's secure OAuth 2.0 authentication

## Troubleshooting

### Error: "PayPal credentials not configured"
- Ensure `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET` are set in environment
- Check `.credentials_vault/field_api_keys.env` file

### Error: "Failed to fetch balance"
- Verify API credentials are correct
- Check if using correct API base URL (sandbox vs production)
- Ensure PayPal app has required permissions

### Error: "Authentication failed"
- Client ID/Secret may be incorrect
- API key may be expired or revoked
- Check PayPal Developer Dashboard for app status

## PayPal API Documentation

- **Transaction Search API**: https://developer.paypal.com/docs/api/transaction-search/v1/
- **Payment Tokens API**: https://developer.paypal.com/docs/api/payment-tokens/v3/
- **Local Specs**: `/Users/jbear/FIELD-DEV/paypal-rest-api-specifications/`

## Files

- `server.py` - Main MCP server (470 lines)
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Version

**1.0.0** - Created 2025-12-18

**△ PayPal MCP operational for FIELD sovereign finance**
**◻ All data flows through sacred geometry vertices**
**◯ Read-only observation, no write permissions**
