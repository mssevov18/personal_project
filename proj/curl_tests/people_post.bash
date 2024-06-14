#!/usr/bin/env bash
curl -X POST http://localhost:8000/people/api/ \
-H "Content-Type: application/json" \
-d '{
    "first_name": "John",
    "middle_name": "M",
    "last_name": "Doe",
    "birthdate": "1990-01-01",
    "emails": "john.doe@example.com",
    "discord": "john_doe#1234",
    "steam": "john_doe",
    "battlenet": "john_doe#5678",
    "instagram": "john_doe",
    "facebook": "john.doe",
    "github": "john_doe",
    "leagueoflegends": "john_doe"
}'
