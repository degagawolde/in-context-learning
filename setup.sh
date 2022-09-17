mkdir -p ~/streamlitap/.streamlit/

echo "\
[general]\n\
email = \"degagawolde@gmail.com\"\n\
" > ~/streamlitap/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/streamlitap/.streamlit/config.toml