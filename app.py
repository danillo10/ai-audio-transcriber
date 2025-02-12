from flask import Flask, request, jsonify, render_template
import whisper
import os
import ffmpeg

app = Flask(__name__)

# Carregar modelo do Whisper (tiny, base, small, medium, large)
model = whisper.load_model("small")

# Criar pasta de uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def convert_audio(input_path):
    """Converte áudios do WhatsApp (.opus, .ogg) para WAV compatível com Whisper."""
    output_path = input_path.rsplit(".", 1)[0] + ".wav"  # Troca extensão para .wav
    try:
        ffmpeg.input(input_path).output(output_path, ar=16000, ac=1, acodec="pcm_s16le").run(overwrite_output=True, quiet=True)
        return output_path
    except Exception as e:
        print(f"Erro ao converter o áudio: {e}")
        return None

@app.route("/")
def index():
    return render_template("index.html")  # Página para upload

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["audio"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Se o arquivo for .opus ou .ogg, converte para WAV
    if filepath.endswith(".opus") or filepath.endswith(".ogg"):
        converted_path = convert_audio(filepath)
        if not converted_path:
            return jsonify({"error": "Erro ao converter o arquivo"}), 500
        filepath = converted_path  # Atualiza para o novo arquivo WAV

    # Transcrever o áudio
    result = model.transcribe(filepath, language="English")

    return jsonify({"transcription": result["text"]})

if __name__ == "__main__":
    app.run(debug=True)
