# Free Fire Info API (Vercel Edition)

A Vercel-compatible Flask API for fetching Free Fire player information.

## Features
- **Vercel Optimized**: Uses `vercel.json` for serverless routing.
- **Lazy Loading**: Token refresh occurs only when needed, avoiding threading issues on serverless functions.
- **Dependencies**: Includes `pycryptodome` for data decryption and `protobuf` for parsing.

## Deployment
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the root directory.
3. The API will be available at `https://your-project.vercel.app/api/info?uid=PLAYER_ID`

## Structure
- `main.py`: Entry point for Flask.
- `utils/`: Helper scripts for AES and Protobuf.
- `vercel.json`: Configuration for deployment.