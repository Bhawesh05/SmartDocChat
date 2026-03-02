#!/bin/bash
# SmartDocChat - Environment Setup Script
# Author: Bhawesh Patankar | GitHub: Bhawesh05

mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"bhawesh05@github.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml
