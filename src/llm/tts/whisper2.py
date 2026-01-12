import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

generate_kwargs = {
    "return_timestamps": True,
}

#dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
#sample = dataset[0]["audio"]
#result = pipe(sample, generate_kwargs=generate_kwargs)

result = pipe("./python/llm/tts/demo1.mp3", chunk_length_s=30, stride_length_s=5, return_timestamps=True)  # 支持分块处理长音频
print(result["chunks"])
