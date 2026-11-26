# Independent backend decision

Do not deploy the full Supabase stack or modify the separate fork. Use FastAPI with SQLAlchemy and Alembic, SQLite for local single-instance development, PostgreSQL for production. Use standard password hashing (Argon2id), expiring revocable opaque sessions, hashed tokens in database, TLS and mobile secure storage. Never expose the database directly to devices.

Planned endpoints: registration, login, logout, profile, consent, assessment, check-ins, actions, saved resources, progress, export and deletion. Apply authenticated owner filtering for all user records. Add email verification and password recovery before external launch. Add abuse controls, migration tests, backup/restore tests and privacy review before real data. Local AI via Ollama is optional and must be evaluated; rule-based fallback clearly labelled.

Local development can run without paid services. Hosting, hardware, electricity, email delivery, domain and backups may cost money. GitHub hosts code, not the running API. No real user data in the public repo. This decision supersedes Supabase references in earlier planning documents.
