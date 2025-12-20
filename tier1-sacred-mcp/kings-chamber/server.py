"""
King's Chamber MCP Server
Diamond (⬥) Translation Bridge at Merkaba Intersection
Frequency: 852 Hz | Geometry: 45° Rotated Square

Routes bidirectionally: Akron ⇄ DOJO
"""

import asyncio
import logging
from typing import Any, Dict
from mcp.server import Server
from mcp.types import Tool, TextContent
from merkaba_router import MerkabaRouter, FlowDirection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kings-chamber")


class KingsChamberServer:
    """
    Diamond (⬥) translation bridge at Merkaba intersection
    Routes bidirectionally: Akron ⇄ DOJO
    """

    def __init__(self):
        self.server = Server("kings-chamber")
        self.symbol = "⬥"
        self.frequency = 852
        self.geometry = "diamond_square_rotated_45"

        # Merkaba router
        self.merkaba = MerkabaRouter()

        # Setup handlers
        self._setup_handlers()

        logger.info(f"{self.symbol} King's Chamber MCP Server initialized at {self.frequency}Hz")

    def _setup_handlers(self):
        """Setup MCP protocol handlers"""

        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            return [
                Tool(
                    name="route_ascending",
                    description="Route data from Akron → DOJO (material to divine)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "description": "Data to route through ascending path"
                            },
                            "source_node": {
                                "type": "string",
                                "description": "Starting node (default: AKRON)",
                                "enum": ["AKRON", "TATA", "ATLAS", "OBI_WAN", "KINGS_CHAMBER"]
                            }
                        },
                        "required": ["data"]
                    }
                ),
                Tool(
                    name="route_descending",
                    description="Route intent from DOJO → Akron (divine to material)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "intent": {
                                "type": "object",
                                "description": "Intent to manifest through descending path"
                            },
                            "destination": {
                                "type": "string",
                                "description": "Target node (default: AKRON)",
                                "enum": ["AKRON", "TATA", "ATLAS", "OBI_WAN", "KINGS_CHAMBER", "DOJO"]
                            }
                        },
                        "required": ["intent"]
                    }
                ),
                Tool(
                    name="validate_merkaba",
                    description="Validate geometric coherence through Merkaba flows",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "flow_type": {
                                "type": "string",
                                "enum": ["ascending", "descending", "both"],
                                "description": "Which flow to validate"
                            }
                        },
                        "required": ["flow_type"]
                    }
                ),
                Tool(
                    name="get_frequency_info",
                    description="Get frequency and geometry information for King's Chamber",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                )
            ]

        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> list[TextContent]:
            logger.info(f"Tool called: {name} with args: {arguments}")

            if name == "route_ascending":
                return await self.handle_ascending(
                    arguments["data"],
                    arguments.get("source_node", "AKRON")
                )
            elif name == "route_descending":
                return await self.handle_descending(
                    arguments["intent"],
                    arguments.get("destination", "AKRON")
                )
            elif name == "validate_merkaba":
                return await self.validate_coherence(arguments["flow_type"])
            elif name == "get_frequency_info":
                return await self.get_info()

            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    async def handle_ascending(self, data: Dict[str, Any], source_node: str) -> list[TextContent]:
        """
        Material → Divine: Transform data through diamond lens

        Path: Akron → TATA → ATLAS → OBI-WAN → King's → DOJO
        Frequency: 396 → 432 → 528 → 963 → 852 → 741 Hz
        """
        try:
            routing = self.merkaba.route_ascending(data, source_node)

            # Apply diamond refraction
            transformed = self.merkaba.transform_at_kings_chamber(
                data,
                FlowDirection.ASCENDING
            )

            result = {
                "status": "ascending_complete",
                "original_data": data,
                "source_node": source_node,
                "transformation": transformed,
                "path": routing["path"],
                "geometric_path": routing["geometric_path"],
                "frequency_progression": routing["frequency_progression"],
                "diamond_refraction": "45_degrees_upward",
                "target": "DOJO",
                "coherence": True
            }

            response_text = f"""⬥ King's Chamber: Ascending Route Complete

📊 Transformation:
   Source: {source_node} ({self.merkaba.get_frequency_at_node(source_node)} Hz)
   Target: DOJO (741 Hz)

🔷 Diamond Refraction:
   Angle: 45° upward
   Frequency: 852 Hz
   Geometry: {self.geometry}

🌟 Path:
   {routing['geometric_path']}

🎵 Frequency Progression:
   {routing['frequency_progression']} Hz

✅ Geometric Coherence: Verified
"""

            logger.info(f"Ascending route completed: {source_node} → DOJO")
            return [TextContent(type="text", text=response_text)]

        except Exception as e:
            logger.error(f"Ascending route error: {e}")
            return [TextContent(type="text", text=f"❌ Error: {str(e)}")]

    async def handle_descending(self, intent: Dict[str, Any], destination: str) -> list[TextContent]:
        """
        Divine → Material: Transform intent through diamond lens

        Path: DOJO → King's → OBI-WAN → ATLAS → TATA → Akron
        Frequency: 741 → 852 → 963 → 528 → 432 → 396 Hz
        """
        try:
            routing = self.merkaba.route_descending(intent, destination)

            # Apply diamond refraction (inverse)
            transformed = self.merkaba.transform_at_kings_chamber(
                intent,
                FlowDirection.DESCENDING
            )

            result = {
                "status": "descending_complete",
                "original_intent": intent,
                "destination": destination,
                "transformation": transformed,
                "path": routing["path"],
                "geometric_path": routing["geometric_path"],
                "frequency_progression": routing["frequency_progression"],
                "diamond_refraction": "45_degrees_downward",
                "coherence": True
            }

            response_text = f"""⬥ King's Chamber: Descending Route Complete

📊 Manifestation:
   Source: DOJO (741 Hz)
   Target: {destination} ({self.merkaba.get_frequency_at_node(destination)} Hz)

🔷 Diamond Refraction:
   Angle: 45° downward
   Frequency: 852 Hz
   Geometry: {self.geometry}

🌟 Path:
   {routing['geometric_path']}

🎵 Frequency Progression:
   {routing['frequency_progression']} Hz

✅ Geometric Coherence: Verified
"""

            logger.info(f"Descending route completed: DOJO → {destination}")
            return [TextContent(type="text", text=response_text)]

        except Exception as e:
            logger.error(f"Descending route error: {e}")
            return [TextContent(type="text", text=f"❌ Error: {str(e)}")]

    async def validate_coherence(self, flow_type: str) -> list[TextContent]:
        """Validate Merkaba geometric coherence"""
        try:
            results = {}

            if flow_type in ["ascending", "both"]:
                ascending_path = ["AKRON", "TATA", "ATLAS", "OBI_WAN", "KINGS_CHAMBER", "DOJO"]
                results["ascending"] = self.merkaba.validate_path(ascending_path, FlowDirection.ASCENDING)

            if flow_type in ["descending", "both"]:
                descending_path = ["DOJO", "KINGS_CHAMBER", "OBI_WAN", "ATLAS", "TATA", "AKRON"]
                results["descending"] = self.merkaba.validate_path(descending_path, FlowDirection.DESCENDING)

            status = "✅ Coherent" if all(results.values()) else "❌ Incoherent"
            response_text = f"""⬥ King's Chamber: Merkaba Validation

Flow Type: {flow_type}
Results: {results}

Status: {status}
"""

            return [TextContent(type="text", text=response_text)]

        except Exception as e:
            return [TextContent(type="text", text=f"❌ Validation error: {str(e)}")]

    async def get_info(self) -> list[TextContent]:
        """Get King's Chamber frequency and geometry info"""
        info_text = f"""⬥ King's Chamber MCP Server

Symbol: {self.symbol}
Frequency: {self.frequency} Hz
Geometry: {self.geometry}
Position: Center of Merkaba

Capabilities:
- Bidirectional routing (Akron ⇄ DOJO)
- Diamond refraction (45° rotation)
- Geometric coherence validation
- Frequency transformation

Merkaba Flows:
  Ascending:  Material → Divine (396 → 741 Hz)
  Descending: Divine → Material (741 → 396 Hz)
"""
        return [TextContent(type="text", text=info_text)]

    async def run(self):
        """Start the MCP server"""
        from mcp.server.stdio import stdio_server

        logger.info(f"{self.symbol} Starting King's Chamber server at {self.frequency}Hz...")
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


async def main():
    """Main entry point"""
    server = KingsChamberServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
