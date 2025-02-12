# 🎙️ Transcrição de Áudio com Whisper e Flask

![Transcrição de Áudio](https://img.shields.io/badge/Flask-2.0%2B-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow) ![Whisper](https://img.shields.io/badge/Whisper-Speech--to--Text-green)

Este projeto é uma aplicação web para **transcrição de áudio** usando **Flask + Whisper (OpenAI)**.  
Ele permite o **upload de arquivos de áudio (incluindo áudios do WhatsApp)** e retorna a **transcrição em texto**. 🎧➡️📜  

---

## 🚀 **Demonstração da Interface**
<img src="https://www.c9tecnologia.com.br/ai-audio-transcriber.png" alt="Demonstração da Interface" width="700px">

---

## 📌 **Recursos**
✅ Upload de arquivos `.mp3`, `.wav`, `.ogg` e `.opus`  
✅ Suporte a **áudios do WhatsApp** (conversão automática)  
✅ Transcrição usando **OpenAI Whisper**  
✅ **Barra de rolagem lateral** para transcrições longas  

---

## 🛠️ **Instalação e Configuração**
### 1️⃣ **Clone o repositório**
```bash
git clone https://github.com/danillo10/ai-audio-transcriber
cd ai-audio-transcriber
```

### **Criar ambiente virtual(opcional)**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

### **Instalar dependências** ###
```
pip install -r requirements.txt
```
### **Executar a aplicação**
```
python app.py
```


