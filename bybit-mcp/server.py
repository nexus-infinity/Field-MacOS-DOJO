#!/usr/bin/env python3
"""
Bybit MCP Server - FIELD Sovereign Finance Module
Version: 1.0.0
Created: 2025-12-18
Sacred Geometry: ● OBI-WAN (963 Hz) - External account observation

Purpose: Connects to Bybit Exchange API v5 for:
- Account balance (spot, derivatives, funding)
- Asset holdings (BTC, ETH, SOL, USDT, etc.)
- Trade history
- Order status

Integrates with: sovereign_finance_ooo.py, sovereign_finance_db.py
"""

import os
import sys
import json
import hmac
import hashlib
import time
import requests
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, List, Any, Optional
from pathlib import Path
from urllib.parse import urlencode

# Add FIELD ontology to path
sys.path.append('/Users/jbear/FIELD/▼TATA/ontology')
from sovereign_finance_ooo import (
    CryptoExchangeAccount, Cryptocurrency, Transaction
)
from sovereign_finance_db import FinanceDatabase

# ═══════════════════════════════════════════════════════════════════════════
# BYBIT API CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

BYBIT_API_BASE = os.getenv('BYBIT_API_BASE', 'https://api-testnet.bybit.com')  # Testnet by default
BYBIT_API_KEY = os.getenv('BYBIT_API_KEY', '')
BYBIT_API_SECRET = os.getenv('BYBIT_API_SECRET', '')

# MCP Server Configuration
MCP_PORT = int(os.getenv('BYBIT_MCP_PORT', '8081'))
DB_PATH = Path(os.getenv('ATLAS_KNOWLEDGE_DB', '/Users/jbear/FIELD-LIVING/data/atlas_knowledge.db'))

# Sacred Geometry Alignment
VERTEX_SYMBOL = "●"
VERTEX_FREQUENCY = "963 Hz"
VERTEX_PURPOSE = "Bybit Exchange Account Observation & Crypto Holdings Tracking"

# ═══════════════════════════════════════════════════════════════════════════
# BYBIT API CLIENT (V5)
# ═══════════════════════════════════════════════════════════════════════════

class BybitAPIClient:
    """
    Bybit API V5 client with HMAC-SHA256 authentication.
    Reference: https://bybit-exchange.github.io/docs/v5/intro
    """

    def __init__(self, api_key: str, api_secret: str, base_url: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url.rstrip('/')
        self.recv_window = 5000  # 5 seconds
        # Use session for connection pooling and better performance
        self.session = requests.Session()

    def _generate_signature(self, timestamp: int, params: str) -> str:
        """Generate HMAC-SHA256 signature for request authentication."""
        param_str = f"{timestamp}{self.api_key}{self.recv_window}{params}"
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            param_str.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature

    def close(self) -> None:
        """Close the requests session to free resources."""
        if self.session:
            self.session.close()

    def _make_request(self, method: str, endpoint: str, params: Dict = None) -> Optional[Dict]:
        """Make authenticated API request to Bybit."""
        if not params:
            params = {}

        timestamp = int(time.time() * 1000)
        param_str = urlencode(sorted(params.items())) if params else ""

        signature = self._generate_signature(timestamp, param_str)

        headers = {
            'X-BAPI-API-KEY': self.api_key,
            'X-BAPI-SIGN': signature,
            'X-BAPI-TIMESTAMP': str(timestamp),
            'X-BAPI-RECV-WINDOW': str(self.recv_window),
            'Content-Type': 'application/json'
        }

        url = f"{self.base_url}{endpoint}"

        try:
            if method == 'GET':
                response = self.session.get(url, headers=headers, params=params, timeout=10)
            elif method == 'POST':
                response = self.session.post(url, headers=headers, json=params, timeout=10)
            else:
                return None

            response.raise_for_status()
            result = response.json()

            # Bybit response format: {"retCode": 0, "retMsg": "OK", "result": {...}}
            if result.get('retCode') == 0:
                return result.get('result', {})
            else:
                print(f"Bybit API error: {result.get('retMsg')}")
                return None

        except Exception as e:
            print(f"Bybit API request failed: {e}")
            return None

    # ─────────────────────────────────────────────────────────────────────
    # Account API (V5)
    # ─────────────────────────────────────────────────────────────────────

    def get_wallet_balance(self, account_type: str = 'UNIFIED') -> Optional[Dict]:
        """
        Get wallet balance.

        Args:
            account_type: 'UNIFIED', 'CONTRACT', 'SPOT', 'INVESTMENT', 'OPTION'

        Returns:
            {
                "list": [
                    {
                        "accountType": "UNIFIED",
                        "totalEquity": "1000.00",
                        "totalWalletBalance": "1000.00",
                        "coin": [
                            {
                                "coin": "BTC",
                                "equity": "0.1",
                                "walletBalance": "0.1",
                                "locked": "0"
                            },
                            {
                                "coin": "USDT",
                                "equity": "1000.00",
                                "walletBalance": "1000.00"
                            }
                        ]
                    }
                ]
            }
        """
        params = {'accountType': account_type}
        return self._make_request('GET', '/v5/account/wallet-balance', params)

    def get_account_info(self) -> Optional[Dict]:
        """
        Get account information (API key permissions, rate limits).

        Returns:
            {
                "unifiedMarginStatus": 1,
                "isMasterTrader": false,
                "updatedTime": "1234567890000"
            }
        """
        return self._make_request('GET', '/v5/account/info')

    # ─────────────────────────────────────────────────────────────────────
    # Position API (V5)
    # ─────────────────────────────────────────────────────────────────────

    def get_positions(self, category: str = 'spot', symbol: Optional[str] = None) -> Optional[Dict]:
        """
        Get position information.

        Args:
            category: 'spot', 'linear', 'inverse', 'option'
            symbol: Trading pair (e.g., 'BTCUSDT')

        Returns:
            {
                "list": [
                    {
                        "symbol": "BTCUSDT",
                        "side": "Buy",
                        "size": "0.1",
                        "avgPrice": "45000.00",
                        "unrealisedPnl": "100.00"
                    }
                ]
            }
        """
        params = {'category': category}
        if symbol:
            params['symbol'] = symbol
        return self._make_request('GET', '/v5/position/list', params)

    # ─────────────────────────────────────────────────────────────────────
    # Market Data API (V5) - Public endpoints (no auth required)
    # ─────────────────────────────────────────────────────────────────────

    def get_tickers(self, category: str = 'spot', symbol: Optional[str] = None) -> Optional[Dict]:
        """
        Get latest price ticker.

        Args:
            category: 'spot', 'linear', 'inverse', 'option'
            symbol: Trading pair (e.g., 'BTCUSDT')

        Returns:
            {
                "list": [
                    {
                        "symbol": "BTCUSDT",
                        "lastPrice": "45000.00",
                        "bid1Price": "44999.00",
                        "ask1Price": "45001.00",
                        "volume24h": "1234.56"
                    }
                ]
            }
        """
        params = {'category': category}
        if symbol:
            params['symbol'] = symbol

        # Public endpoint - no authentication
        url = f"{self.base_url}/v5/market/tickers"
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            result = response.json()
            return result.get('result', {}) if result.get('retCode') == 0 else None
        except Exception as e:
            print(f"Failed to fetch tickers: {e}")
            return None

    # ─────────────────────────────────────────────────────────────────────
    # Trade API (V5)
    # ─────────────────────────────────────────────────────────────────────

    def get_order_history(self, category: str = 'spot', limit: int = 50) -> Optional[Dict]:
        """
        Get order history.

        Args:
            category: 'spot', 'linear', 'inverse', 'option'
            limit: Number of records (max 50)

        Returns:
            {
                "list": [
                    {
                        "orderId": "...",
                        "symbol": "BTCUSDT",
                        "side": "Buy",
                        "orderType": "Market",
                        "qty": "0.001",
                        "price": "45000.00",
                        "orderStatus": "Filled",
                        "createdTime": "1234567890000",
                        "updatedTime": "1234567890000"
                    }
                ]
            }
        """
        params = {'category': category, 'limit': limit}
        return self._make_request('GET', '/v5/order/history', params)

    def get_trade_history(self, category: str = 'spot', limit: int = 100) -> Optional[Dict]:
        """
        Get execution (trade) history.

        Args:
            category: 'spot', 'linear', 'inverse', 'option'
            limit: Number of records (max 100)

        Returns:
            {
                "list": [
                    {
                        "symbol": "BTCUSDT",
                        "orderId": "...",
                        "side": "Buy",
                        "execQty": "0.001",
                        "execPrice": "45000.00",
                        "execValue": "45.00",
                        "execFee": "0.045",
                        "execTime": "1234567890000"
                    }
                ]
            }
        """
        params = {'category': category, 'limit': limit}
        return self._make_request('GET', '/v5/execution/list', params)

# ═══════════════════════════════════════════════════════════════════════════
# BYBIT → FIELD ONTOLOGY CONVERTER
# ═══════════════════════════════════════════════════════════════════════════

class BybitToFieldConverter:
    """Converts Bybit API responses to FIELD ontology objects."""

    @staticmethod
    def to_crypto_exchange_account(wallet_data: Dict, account_info: Dict = None) -> CryptoExchangeAccount:
        """Convert Bybit wallet to CryptoExchangeAccount object."""
        account = wallet_data.get('list', [{}])[0]
        coins = account.get('coin', [])

        # Build asset holdings dict
        holdings = {}
        for coin_data in coins:
            coin = coin_data.get('coin')
            equity = float(coin_data.get('equity', 0.0))
            holdings[coin] = equity

        # Calculate total balance in USDT equivalent
        total_equity = float(account.get('totalEquity', 0.0))

        return CryptoExchangeAccount(
            id="acc-bybit-001",
            name="Bybit Main Account",
            account_number="bybit-unified",
            balance=total_equity,
            currency="USDT",
            exchange_name="Bybit",
            sub_account_type=account.get('accountType', 'UNIFIED').lower(),
            asset_holdings=holdings,
            mcp_server_endpoint="http://localhost:8081",
            credentials_id="cred-bybit-api-001",
            metadata={
                'total_wallet_balance': account.get('totalWalletBalance'),
                'account_type': account.get('accountType'),
                'is_unified_margin': account_info.get('unifiedMarginStatus') if account_info else None
            }
        )

    @staticmethod
    def to_transaction(trade_data: Dict, account_id: str) -> Transaction:
        """Convert Bybit trade to Transaction object."""
        return Transaction(
            id=f"bybit-trade-{trade_data.get('execId', 'unknown')}",
            name=f"Bybit {trade_data.get('side')} {trade_data.get('symbol')}",
            from_account_id=account_id,
            to_account_id=account_id,  # Internal exchange trade
            amount=float(trade_data.get('execValue', 0.0)),
            currency="USDT",
            transaction_type='trade_buy' if trade_data.get('side') == 'Buy' else 'trade_sell',
            status='completed',
            timestamp=datetime.fromtimestamp(int(trade_data.get('execTime', 0)) / 1000),
            purpose=f"{trade_data.get('side')} {trade_data.get('execQty')} {trade_data.get('symbol')} @ {trade_data.get('execPrice')}",
            metadata={
                'bybit_exec_id': trade_data.get('execId'),
                'bybit_order_id': trade_data.get('orderId'),
                'symbol': trade_data.get('symbol'),
                'side': trade_data.get('side'),
                'exec_qty': trade_data.get('execQty'),
                'exec_price': trade_data.get('execPrice'),
                'exec_fee': trade_data.get('execFee'),
                'fee_currency': trade_data.get('feeRate')
            }
        )

# ═══════════════════════════════════════════════════════════════════════════
# MCP SERVER HTTP HANDLER
# ═══════════════════════════════════════════════════════════════════════════

class BybitMCPHandler(BaseHTTPRequestHandler):
    """HTTP handler for Bybit MCP server."""

    api_client = None
    db = None

    @classmethod
    def initialize(cls):
        """Initialize API client and database."""
        cls.api_client = BybitAPIClient(BYBIT_API_KEY, BYBIT_API_SECRET, BYBIT_API_BASE)
        cls.db = FinanceDatabase()

    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/health':
            self._send_json_response({'status': 'ok', 'vertex': VERTEX_SYMBOL, 'frequency': VERTEX_FREQUENCY})
        elif self.path == '/balance':
            self._handle_get_balance()
        elif self.path == '/account-info':
            self._handle_get_account_info()
        elif self.path.startswith('/positions'):
            self._handle_get_positions()
        elif self.path.startswith('/ticker'):
            self._handle_get_ticker()
        elif self.path == '/trade-history':
            self._handle_get_trade_history()
        else:
            self._send_json_response({'error': 'Not found'}, status=404)

    def do_POST(self):
        """Handle POST requests."""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._send_json_response({'error': 'Invalid JSON'}, status=400)
            return

        if self.path == '/sync-account':
            self._handle_sync_account(data)
        elif self.path == '/sync-trades':
            self._handle_sync_trades(data)
        elif self.path == '/update-prices':
            self._handle_update_prices(data)
        else:
            self._send_json_response({'error': 'Not found'}, status=404)

    def _send_json_response(self, data: Dict, status: int = 200):
        """Send JSON response."""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def _handle_get_balance(self):
        """Get Bybit wallet balance."""
        balance_data = self.api_client.get_wallet_balance()
        if not balance_data:
            self._send_json_response({'error': 'Failed to fetch balance'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'balance': balance_data,
            'vertex': VERTEX_SYMBOL,
            'frequency': VERTEX_FREQUENCY
        })

    def _handle_get_account_info(self):
        """Get Bybit account info."""
        info = self.api_client.get_account_info()
        if not info:
            self._send_json_response({'error': 'Failed to fetch account info'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'account_info': info,
            'vertex': VERTEX_SYMBOL
        })

    def _handle_get_positions(self):
        """Get Bybit positions."""
        positions = self.api_client.get_positions()
        if not positions:
            self._send_json_response({'error': 'Failed to fetch positions'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'positions': positions.get('list', []),
            'vertex': VERTEX_SYMBOL
        })

    def _handle_get_ticker(self):
        """Get Bybit price ticker."""
        tickers = self.api_client.get_tickers(category='spot')
        if not tickers:
            self._send_json_response({'error': 'Failed to fetch tickers'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'tickers': tickers.get('list', []),
            'vertex': VERTEX_SYMBOL
        })

    def _handle_get_trade_history(self):
        """Get Bybit trade history."""
        trades = self.api_client.get_trade_history()
        if not trades:
            self._send_json_response({'error': 'Failed to fetch trade history'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'trades': trades.get('list', []),
            'count': len(trades.get('list', [])),
            'vertex': VERTEX_SYMBOL
        })

    def _handle_sync_account(self, data: Dict):
        """Sync Bybit account to FIELD database."""
        balance_data = self.api_client.get_wallet_balance()
        account_info = self.api_client.get_account_info()

        if not balance_data:
            self._send_json_response({'error': 'Failed to fetch account data'}, status=500)
            return

        # Convert to FIELD ontology
        account = BybitToFieldConverter.to_crypto_exchange_account(balance_data, account_info)

        # Save to database
        account_id = self.db.create_account(account)

        self._send_json_response({
            'status': 'success',
            'action': 'account_synced',
            'account_id': account_id,
            'balance': account.balance,
            'currency': account.currency,
            'holdings': account.asset_holdings,
            'vertex': VERTEX_SYMBOL
        })

    def _handle_sync_trades(self, data: Dict):
        """Sync Bybit trades to FIELD database."""
        limit = data.get('limit', 100)
        trades_data = self.api_client.get_trade_history(limit=limit)

        if not trades_data:
            self._send_json_response({'error': 'Failed to fetch trades'}, status=500)
            return

        account_id = data.get('account_id', 'acc-bybit-001')
        trades = trades_data.get('list', [])

        synced_count = 0
        for trade in trades:
            tx = BybitToFieldConverter.to_transaction(trade, account_id)
            self.db.create_transaction(tx)
            synced_count += 1

        self._send_json_response({
            'status': 'success',
            'action': 'trades_synced',
            'count': synced_count,
            'vertex': VERTEX_SYMBOL
        })

    def _handle_update_prices(self, data: Dict):
        """Update cryptocurrency prices in FIELD database."""
        symbols = data.get('symbols', ['BTCUSDT', 'ETHUSDT', 'SOLUSDT'])

        updated_count = 0
        for symbol in symbols:
            ticker_data = self.api_client.get_tickers(category='spot', symbol=symbol)
            if ticker_data and ticker_data.get('list'):
                ticker = ticker_data['list'][0]
                price = float(ticker.get('lastPrice', 0.0))

                # Extract coin symbol (e.g., "BTCUSDT" -> "BTC")
                coin_symbol = symbol.replace('USDT', '').replace('USD', '')

                # Update price in atlas_knowledge.db
                self.db.update_price(coin_symbol, price, source='bybit')
                updated_count += 1

        self._send_json_response({
            'status': 'success',
            'action': 'prices_updated',
            'count': updated_count,
            'vertex': VERTEX_SYMBOL
        })

    def log_message(self, format, *args):
        """Override to add FIELD formatting."""
        print(f"{VERTEX_SYMBOL} Bybit MCP ({VERTEX_FREQUENCY}): {format % args}")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN SERVER
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Start Bybit MCP server."""
    if not BYBIT_API_KEY or not BYBIT_API_SECRET:
        print(f"⚠️  Bybit credentials not configured!")
        print(f"   Set BYBIT_API_KEY and BYBIT_API_SECRET environment variables")
        print(f"   Get credentials from: https://www.bybit.com/app/user/api-management")
        print(f"   Note: Set permissions to 'Read Only' for security")
        return

    # Initialize handler
    BybitMCPHandler.initialize()

    # Start server
    server_address = ('', MCP_PORT)
    httpd = HTTPServer(server_address, BybitMCPHandler)

    print("=" * 70)
    print(f"{VERTEX_SYMBOL} FIELD Bybit MCP Server Starting...")
    print("=" * 70)
    print(f"   Vertex: {VERTEX_SYMBOL} OBI-WAN")
    print(f"   Frequency: {VERTEX_FREQUENCY}")
    print(f"   Purpose: {VERTEX_PURPOSE}")
    print(f"   Port: {MCP_PORT}")
    print(f"   API Base: {BYBIT_API_BASE}")
    print(f"   Database: {DB_PATH}")
    print("=" * 70)
    print(f"   Endpoints:")
    print(f"     GET  /health           - Health check")
    print(f"     GET  /balance          - Get wallet balance")
    print(f"     GET  /account-info     - Get account information")
    print(f"     GET  /positions        - Get open positions")
    print(f"     GET  /ticker           - Get price tickers")
    print(f"     GET  /trade-history    - Get trade history")
    print(f"     POST /sync-account     - Sync account to FIELD database")
    print(f"     POST /sync-trades      - Sync trades to FIELD database")
    print(f"     POST /update-prices    - Update crypto prices in database")
    print("=" * 70)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{VERTEX_SYMBOL} Bybit MCP Server stopping...")
        httpd.shutdown()

if __name__ == "__main__":
    main()
