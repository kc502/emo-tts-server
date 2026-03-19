import asyncio
import edge_tts
from flask import Flask, request, send_file
import os

app = Flask(__name__)

async def generate_tts(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

@app.route('/tts')
def tts():
    text = request.args.get('text', 'မင်္ဂလာပါ')
    # မြန်မာသံ Nilar သုံးထားပါတယ်
    voice = "my-MM-NilarNeural" 
    output_file = "voice.mp3"
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(generate_tts(text, voice, output_file))
    
    return send_file(output_file, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run()

