import whisper
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "large-v3-turbo"
model = whisper.load_model(model_id).to(device)

result = model.transcribe("./python/llm/tts/demo1.mp3")
print(result["text"])
