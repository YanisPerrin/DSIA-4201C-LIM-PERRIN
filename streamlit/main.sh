#!/bin/bash
exec python mongo_init.py &
exec streamlit run main.py --server.port=8501 --server.address=0.0.0.0