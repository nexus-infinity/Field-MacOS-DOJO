import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Hollywood Production - FIELD Video Manifestation',
  description: 'Descending Flow: DOJO → Kings Chamber → Hollywood → Akron Archive',
  other: {
    'merkaba-flow': 'descending',
    'sacred-geometry': 'bidirectional-tetrahedra',
    'frequency-descent': '741Hz-to-396Hz'
  }
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        <div style={{
          minHeight: '100vh',
          background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
          color: '#ffffff',
          fontFamily: 'system-ui, -apple-system, sans-serif'
        }}>
          {children}
        </div>
      </body>
    </html>
  )
}
