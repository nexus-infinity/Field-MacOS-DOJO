/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  env: {
    MERKABA_ARCHITECTURE: process.env.MERKABA_ARCHITECTURE || 'descending_flow',
  },
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Merkaba-Flow',
            value: 'Divine-to-Material'
          },
          {
            key: 'X-Merkaba-Direction',
            value: 'Descending'
          },
          {
            key: 'X-Frequency-Descent',
            value: '741Hz-DOJO-to-396Hz-Akron'
          },
          {
            key: 'X-Kings-Chamber',
            value: 'Diamond-Translation-852Hz'
          },
          {
            key: 'X-Sacred-Geometry',
            value: 'Bidirectional-Tetrahedra'
          },
          {
            key: 'X-FIELD-Architecture',
            value: 'Merkaba-Bidirectional'
          }
        ]
      }
    ]
  }
}

module.exports = nextConfig
