import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Insight Agent', layout='wide')

st.title('Insight Agent – UI Shell')
st.write('Placeholder Home page')

# Show handoff/status.json if present
p = Path('handoff/status.json')
if p.exists():
    try:
        import json
        data = json.loads(p.read_text())
        st.subheader('Handoff status')
        st.json(data)
    except Exception as e:
        st.write('Could not read handoff/status.json:', e)
else:
    st.write('No handoff/status.json found')
