#!/usr/bin/env python3
"""
PayPal MCP Server - FIELD Sovereign Finance Module
Version: 1.0.0
Created: 2025-12-18
Sacred Geometry: ● OBI-WAN (963 Hz) - External account observation

Purpose: Connects to PayPal REST API for:
- Transaction history retrieval
- Balance checking
- Gift card status monitoring
- Payment method tokens (stored instruments)

Integrates with: sovereign_finance_ooo.py, sovereign_finance_db.py
"""

import os
import sys
import json
import hashlib
import requests
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, List, Any, Optional
from pathlib import Path

# Add FIELD ontology to path
sys.path.append('/Users/jbear/FIELD/▼TATA/ontology')
from sovereign_finance_ooo import (
    DigitalWallet, GiftCard, Transaction, FinancialStatement
)
from sovereign_finance_db import FinanceDatabase

# ═══════════════════════════════════════════════════════════════════════════
# PAYPAL API CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

PAYPAL_API_BASE = os.getenv('PAYPAL_API_BASE', 'https://api-m.sandbox.paypal.com')  # Use sandbox by default
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', '')
PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET', '')

# MCP Server Configuration
MCP_PORT = int(os.getenv('PAYPAL_MCP_PORT', '8080'))
DB_PATH = Path(os.getenv('ATLAS_KNOWLEDGE_DB', '/Users/jbear/FIELD-LIVING/data/atlas_knowledge.db'))

# Sacred Geometry Alignment
VERTEX_SYMBOL = "●"
VERTEX_FREQUENCY = "963 Hz"
VERTEX_PURPOSE = "PayPal Account Observation & Balance Tracking"

# ═══════════════════════════════════════════════════════════════════════════
# PAYPAL API CLIENT
# ═══════════════════════════════════════════════════════════════════════════

class PayPalAPIClient:
    """
    PayPal REST API client with OAuth 2.0 authentication.
    Based on official PayPal REST API specifications.
    """

    def __init__(self, client_id: str, client_secret: str, base_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url.rstrip('/')
        self.access_token = None
        self.token_expires_at = None
        # Use session for connection pooling and better performance
        self.session = requests.Session()

    def authenticate(self) -> bool:
        """
        Obtain OAuth 2.0 access token.
        Endpoint: POST /v1/oauth2/token
        """
        if self.access_token and self.token_expires_at:
            if datetime.now() < self.token_expires_at:
                return True  # Token still valid

        url = f"{self.base_url}/v1/oauth2/token"
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en_US'
        }
        data = {
            'grant_type': 'client_credentials'
        }

        try:
            response = self.session.post(
                url,
                headers=headers,
                data=data,
                auth=(self.client_id, self.client_secret),
                timeout=10
            )
            response.raise_for_status()

            token_data = response.json()
            self.access_token = token_data['access_token']
            expires_in = token_data.get('expires_in', 3600)
            self.token_expires_at = datetime.now() + timedelta(seconds=expires_in - 60)

            return True
        except Exception as e:
            print(f"PayPal authentication failed: {e}")
            return False

    def close(self) -> None:
        """Close the requests session to free resources."""
        if self.session:
            self.session.close()

    def _make_request(self, method: str, endpoint: str, params: Dict = None, data: Dict = None) -> Optional[Dict]:
        """Make authenticated API request."""
        if not self.authenticate():
            return None

        url = f"{self.base_url}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        try:
            if method == 'GET':
                response = self.session.get(url, headers=headers, params=params, timeout=15)
            elif method == 'POST':
                response = self.session.post(url, headers=headers, json=data, timeout=15)
            else:
                return None

            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"PayPal API request failed: {e}")
            return None

    # ─────────────────────────────────────────────────────────────────────
    # Transaction Search API (v1)
    # Spec: /Users/jbear/FIELD-DEV/paypal-rest-api-specifications/openapi/reporting_transactions_v1.json
    # ─────────────────────────────────────────────────────────────────────

    def list_transactions(self, start_date: str, end_date: str, limit: int = 100) -> Optional[Dict]:
        """
        List transactions for a date range.

        Args:
            start_date: Start date (ISO 8601: YYYY-MM-DD)
            end_date: End date (ISO 8601: YYYY-MM-DD)
            limit: Maximum number of transactions (1-500)

        Returns:
            {
                "transaction_details": [...],
                "account_number": "...",
                "start_date": "...",
                "end_date": "...",
                "total_items": N
            }
        """
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'fields': 'all',
            'page_size': min(limit, 500)
        }
        return self._make_request('GET', '/v1/reporting/transactions', params=params)

    def get_balance(self) -> Optional[Dict]:
        """
        Get PayPal account balance.

        Returns:
            {
                "balances": [
                    {
                        "currency": "USD",
                        "primary": true,
                        "total_balance": {
                            "currency_code": "USD",
                            "value": "123.45"
                        },
                        "available_balance": {
                            "currency_code": "USD",
                            "value": "100.00"
                        }
                    }
                ]
            }
        """
        return self._make_request('GET', '/v1/reporting/balances')

    # ─────────────────────────────────────────────────────────────────────
    # Payment Method Tokens API (v3) - For Gift Cards
    # Spec: /Users/jbear/FIELD-DEV/paypal-rest-api-specifications/openapi/vault_payment_tokens_v3.json
    # ─────────────────────────────────────────────────────────────────────

    def list_payment_tokens(self, customer_id: Optional[str] = None) -> Optional[Dict]:
        """
        List payment method tokens (stored payment methods, including gift cards).

        Args:
            customer_id: Optional customer ID filter

        Returns:
            {
                "payment_tokens": [
                    {
                        "id": "...",
                        "customer": {"id": "..."},
                        "payment_source": {...},
                        "links": [...]
                    }
                ]
            }
        """
        params = {}
        if customer_id:
            params['customer_id'] = customer_id

        return self._make_request('GET', '/v3/vault/payment-tokens', params=params)

    def get_payment_token(self, token_id: str) -> Optional[Dict]:
        """
        Get details for a specific payment token (gift card).

        Args:
            token_id: Payment token ID

        Returns:
            {
                "id": "...",
                "payment_source": {
                    "card": {
                        "brand": "VISA",
                        "last_digits": "1234",
                        "expiry": "2025-12"
                    }
                },
                "status": "ACTIVE"
            }
        """
        return self._make_request('GET', f'/v3/vault/payment-tokens/{token_id}')

# ═══════════════════════════════════════════════════════════════════════════
# PAYPAL → FIELD ONTOLOGY CONVERTER
# ═══════════════════════════════════════════════════════════════════════════

class PayPalToFieldConverter:
    """Converts PayPal API responses to FIELD ontology objects."""

    @staticmethod
    def to_digital_wallet(account_data: Dict) -> DigitalWallet:
        """Convert PayPal account to DigitalWallet object."""
        balance_data = account_data.get('balances', [{}])[0]
        total_balance = balance_data.get('total_balance', {})

        return DigitalWallet(
            id=f"paypal-{account_data.get('account_number', 'main')}",
            name="PayPal Main Account",
            account_number=account_data.get('account_number', ''),
            balance=float(total_balance.get('value', 0.0)),
            currency=total_balance.get('currency_code', 'USD'),
            platform="PayPal",
            email=account_data.get('primary_email'),
            mcp_server_endpoint="http://localhost:8080",
            credentials_id="cred-paypal-main-001"
        )

    @staticmethod
    def to_gift_card(token_data: Dict) -> GiftCard:
        """Convert PayPal payment token to GiftCard object."""
        payment_source = token_data.get('payment_source', {})
        card_data = payment_source.get('card', {})

        return GiftCard(
            id=f"paypal-gc-{token_data.get('id', 'unknown')}",
            name=f"PayPal Gift Card ({card_data.get('last_digits', '****')})",
            account_number=token_data.get('id', ''),
            balance=0.0,  # PayPal API doesn't provide balance for tokens
            currency="USD",
            card_number=f"****-****-****-{card_data.get('last_digits', '****')}",
            vendor="PayPal",
            mcp_server_endpoint="http://localhost:8080",
            credentials_id="cred-paypal-main-001"
        )

    @staticmethod
    def to_transaction(txn_data: Dict, account_id: str) -> Transaction:
        """Convert PayPal transaction to Transaction object."""
        transaction_info = txn_data.get('transaction_info', {})

        return Transaction(
            id=f"paypal-tx-{transaction_info.get('transaction_id', 'unknown')}",
            name=transaction_info.get('transaction_subject', 'PayPal Transaction'),
            from_account_id=account_id,
            to_account_id=txn_data.get('payer_info', {}).get('account_id', 'external'),
            amount=abs(float(transaction_info.get('transaction_amount', {}).get('value', 0.0))),
            currency=transaction_info.get('transaction_amount', {}).get('currency_code', 'USD'),
            transaction_type='payment',
            status='completed' if transaction_info.get('transaction_status') == 'S' else 'pending',
            timestamp=datetime.fromisoformat(transaction_info.get('transaction_initiation_date', datetime.now().isoformat()).replace('Z', '+00:00')),
            purpose=transaction_info.get('transaction_note', ''),
            metadata={
                'paypal_transaction_id': transaction_info.get('transaction_id'),
                'transaction_event_code': transaction_info.get('transaction_event_code'),
                'fee_amount': transaction_info.get('fee_amount', {}).get('value'),
                'protection_eligibility': transaction_info.get('protection_eligibility')
            }
        )

# ═══════════════════════════════════════════════════════════════════════════
# MCP SERVER HTTP HANDLER
# ═══════════════════════════════════════════════════════════════════════════

class PayPalMCPHandler(BaseHTTPRequestHandler):
    """HTTP handler for PayPal MCP server."""

    api_client = None
    db = None

    @classmethod
    def initialize(cls):
        """Initialize API client and database."""
        cls.api_client = PayPalAPIClient(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET, PAYPAL_API_BASE)
        cls.db = FinanceDatabase()

    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/health':
            self._send_json_response({'status': 'ok', 'vertex': VERTEX_SYMBOL, 'frequency': VERTEX_FREQUENCY})
        elif self.path == '/balance':
            self._handle_get_balance()
        elif self.path.startswith('/transactions'):
            self._handle_list_transactions()
        elif self.path == '/gift-cards':
            self._handle_list_gift_cards()
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
        elif self.path == '/sync-transactions':
            self._handle_sync_transactions(data)
        else:
            self._send_json_response({'error': 'Not found'}, status=404)

    def _send_json_response(self, data: Dict, status: int = 200):
        """Send JSON response."""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def _handle_get_balance(self):
        """Get PayPal account balance."""
        balance_data = self.api_client.get_balance()
        if not balance_data:
            self._send_json_response({'error': 'Failed to fetch balance'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'balance': balance_data,
            'vertex': VERTEX_SYMBOL,
            'frequency': VERTEX_FREQUENCY
        })

    def _handle_list_transactions(self):
        """List PayPal transactions."""
        # Default: last 30 days
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        txn_data = self.api_client.list_transactions(start_date, end_date)
        if not txn_data:
            self._send_json_response({'error': 'Failed to fetch transactions'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'transactions': txn_data.get('transaction_details', []),
            'count': txn_data.get('total_items', 0),
            'vertex': VERTEX_SYMBOL
        })

    def _handle_list_gift_cards(self):
        """List PayPal gift cards (payment tokens)."""
        tokens_data = self.api_client.list_payment_tokens()
        if not tokens_data:
            self._send_json_response({'error': 'Failed to fetch gift cards'}, status=500)
            return

        self._send_json_response({
            'status': 'success',
            'gift_cards': tokens_data.get('payment_tokens', []),
            'vertex': VERTEX_SYMBOL
        })

    def _handle_sync_account(self, data: Dict):
        """Sync PayPal account to FIELD database."""
        balance_data = self.api_client.get_balance()
        if not balance_data:
            self._send_json_response({'error': 'Failed to fetch account data'}, status=500)
            return

        # Convert to FIELD ontology
        wallet = PayPalToFieldConverter.to_digital_wallet(balance_data)

        # Save to database
        account_id = self.db.create_account(wallet)

        self._send_json_response({
            'status': 'success',
            'action': 'account_synced',
            'account_id': account_id,
            'balance': wallet.balance,
            'currency': wallet.currency,
            'vertex': VERTEX_SYMBOL
        })

    def _handle_sync_transactions(self, data: Dict):
        """Sync PayPal transactions to FIELD database."""
        days = data.get('days', 30)
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        txn_data = self.api_client.list_transactions(start_date, end_date)
        if not txn_data:
            self._send_json_response({'error': 'Failed to fetch transactions'}, status=500)
            return

        account_id = data.get('account_id', 'paypal-main')
        transactions = txn_data.get('transaction_details', [])

        synced_count = 0
        for txn in transactions:
            tx = PayPalToFieldConverter.to_transaction(txn, account_id)
            self.db.create_transaction(tx)
            synced_count += 1

        self._send_json_response({
            'status': 'success',
            'action': 'transactions_synced',
            'count': synced_count,
            'start_date': start_date,
            'end_date': end_date,
            'vertex': VERTEX_SYMBOL
        })

    def log_message(self, format, *args):
        """Override to add FIELD formatting."""
        print(f"{VERTEX_SYMBOL} PayPal MCP ({VERTEX_FREQUENCY}): {format % args}")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN SERVER
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Start PayPal MCP server."""
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        print(f"⚠️  PayPal credentials not configured!")
        print(f"   Set PAYPAL_CLIENT_ID and PAYPAL_CLIENT_SECRET environment variables")
        print(f"   Get credentials from: https://developer.paypal.com/dashboard/applications")
        return

    # Initialize handler
    PayPalMCPHandler.initialize()

    # Start server
    server_address = ('', MCP_PORT)
    httpd = HTTPServer(server_address, PayPalMCPHandler)

    print("=" * 70)
    print(f"{VERTEX_SYMBOL} FIELD PayPal MCP Server Starting...")
    print("=" * 70)
    print(f"   Vertex: {VERTEX_SYMBOL} OBI-WAN")
    print(f"   Frequency: {VERTEX_FREQUENCY}")
    print(f"   Purpose: {VERTEX_PURPOSE}")
    print(f"   Port: {MCP_PORT}")
    print(f"   API Base: {PAYPAL_API_BASE}")
    print(f"   Database: {DB_PATH}")
    print("=" * 70)
    print(f"   Endpoints:")
    print(f"     GET  /health           - Health check")
    print(f"     GET  /balance          - Get PayPal balance")
    print(f"     GET  /transactions     - List transactions (last 30 days)")
    print(f"     GET  /gift-cards       - List gift cards (payment tokens)")
    print(f"     POST /sync-account     - Sync account to FIELD database")
    print(f"     POST /sync-transactions - Sync transactions to FIELD database")
    print("=" * 70)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{VERTEX_SYMBOL} PayPal MCP Server stopping...")
        httpd.shutdown()

if __name__ == "__main__":
    main()
