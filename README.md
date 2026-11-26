# HumanBridge AI

**Connect. Belong. Thrive.**

An early cross-platform wellbeing prototype for adults aged 18–40. Our goal is meaningful human connection, not AI companionship. No evidence of product effectiveness is claimed yet.

## Status: v0.1.0

Mobile: onboarding, optional check-in, action plan, rule-based coaching, sample activities and progress. All state is temporary; no account, tracking or real events. Backend: independent development API; not yet wired to mobile. No LLM, database or production authentication. Do not use with real participant data.

## Windows setup

Install Node.js 22 LTS, Python 3.11+ and Git. For mobile:

```powershell
cd apps/mobile
npm install
npx expo install --fix
npm run typecheck
npx expo start
```

Use a compatible Expo Go version or development build. See https://docs.expo.dev/versions/v56.0.0/. On a separate terminal, from repo root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs for API exploration. Backend binds to loopback by default. Do not expose it publicly.

## Documentation

- [Research and evaluation](docs/RESEARCH.md)
- [Product requirements](docs/REQUIREMENTS.md)
- [System architecture](docs/ARCHITECTURE.md)
- [Safety and privacy](docs/SAFETY.md)
- [Roadmap](docs/ROADMAP.md)

No open-source licence has been selected. Public visibility does not grant a general licence to reuse code. The provisional app identifiers must be confirmed before publishing.
