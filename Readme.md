1) ön hazırlık
    python
    vs code
    git
    github
2) frontend repo
ai-roadmap-frontend/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
3) frontend kodlarının streamlit ile yazılması
4) bağlımlıkları kurma ve streamlit çalıştırma
    pip install -r requirements.txt
    streamlit run app.py
5) frontend dockerfile, docker compose, .dockerignore
    docker compose up --build
6) github
    repo: python-web-uygulama-ai-roadmap-frontend
        git init
        git add .
        git commit -m "first frontend commit"
        git branch -M main
        git remote add origin https://github.com/turkiyeyapayzekaakademisi/python-web-uygulama-ai-roadmap-frontend.git
        git push -u origin main
7) streamlit community cloud deploy: https://streamlit.io/cloud