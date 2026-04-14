# Alembic Migration

Alembic is a library in Python used as a database migration tool used with SQLAlchemy that helps manage and version-control changes to the database schema. It allows developers to generate migration scripts, apply them to the database, and roll them back if needed.

# Alembic is a database migration tool for SQLAlchemy

Alembic helps you track and apply changes to your database schema over time.

# What is a Migration ?

"""
A Migration = a version-controlled change to your database.
"""

# Steps
1. Create Migration
    - alembic init
2. Create Script
    - alembic revision --autogenerate -m "Initial migration"
    - alembic current
    - alembic history
3. Execute
    - alembic upgrade head
    - alembic downgrade
    - alembic stamp head

# Alembic Commands

| Command | Description |
|---------|-------------|
| alembic init | Initialize Alembic |
| alembic revision --autogenerate -m "Initial migration" | Create migration script |
| alembic current | Show current migration |
| alembic history | Show migration history |
| alembic upgrade head | Upgrade to latest migration |
| alembic downgrade | Downgrade to previous migration |
| alembic stamp head | Stamp current migration |
*It does not change the schema, create tables, or execute upgrade()/downgrade() functions. It only modifies the alembic_version table.

# Flow 
Change Model -> Generate Migration -> Apply Migration -> DB Updated

# Difference
| Without          | With Alembic       |
| ---------------- | ------------------ |
| Manual SQL       | Automated          |
| Error-prone      | Safe               |
| No history       | Version controlled |
| Hard to rollback | Easy rollback      |