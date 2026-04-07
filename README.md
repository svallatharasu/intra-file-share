# Simple intra file sharing app
# 1. JWT Authentication
# 2. Google Sigin
# 3. Top right corner ( Human symbol )
# 4. Search Groups and Individual Persons
# 5. File shared and messages
# 6. Search + Add other users
# 7. Viewed -> How much time he spend on the document ?
# 8. Search through semantics

<!-- Your Features & Effort Estimation
1. JWT Authentication ✅

FastAPI: fastapi-jwt-auth or fastapi-users

React: store token in localStorage or httpOnly cookies.

Effort: ~1 day if starting from scratch (but easy if you have templates).

2. Google Sign-In ✅

FastAPI: Use google-auth or OAuth2 flow

React: Use react-google-login

Effort: ~0.5–1 day (mostly front + backend token exchange).

3. Top-right corner Human icon ✅

React UI only. Dropdown for profile / logout.

Effort: ~0.25 day

4. Search Groups and Individual Persons

Backend: Search DB (LIKE, ILIKE)

Frontend: Autocomplete component (React-Select / MUI)

Effort: ~0.5–1 day

5. File shared and messages

Upload: FastAPI UploadFile

DB: store file info, messages

UI: chat-style or group-style message view

Effort: ~1–1.5 days

6. Search + Add other users ✅

Extend #4 + API to add a user to a group

Effort: ~0.5 day

7. Viewed → How much time spent on document? ⏱️

This is innovative and adds measurable value.

Approach:

Use inline file preview (PDF.js / ViewerJS / iframe for images/docs).

Track focus events in React:

onFocus, onBlur, mousemove, scroll → keep a timer while user is “active”

Send heartbeat API to FastAPI every few seconds with elapsed time

Store cumulative time per file per user

Effort: ~1–2 days (React heavy, backend is simple logging)

8. Semantic Search 🔍

You want search by meaning, not just filename.

Options for FastAPI stack:

OpenAI / HuggingFace embeddings

Embed file content & messages → store embeddings in DB

Query with cosine similarity

FastAPI: sentence-transformers or OpenAI embeddings

React: search input → hits backend → returns semantically relevant results

Weaviate / Pinecone / FAISS (vector DB for large scale)

Effort:

Small scale (~few hundred docs): 1–2 days using sentence-transformers + SQLite/Postgres

Large scale / production: 1 week+

✅ Feasible Two-Day “Innovative Version”

If you only have 2 days, I’d suggest doing:

JWT + Google Sign-In ✅

File sharing + messages ✅

Inline file preview + “time spent on document” ⏱️ (makes it innovative!)

Basic search (filename / user / group)

Skip semantic search for now — can be added later as an upgrade.

💡 Summary:

Frontend: React handles previews, timers, search, and UI

Backend: FastAPI handles auth, file upload/download, logging time, search API

Optional innovation:

Inline comments on files

Watermarking user on download -->
