from hailo_platform import VDevice
from hailo_platform.genai import LLM
from .rag import ryuuRetrieve, ryuuIngest

SYSTEM_PROMPT = "You are Ryuu (竜), a private, wise, and Japanese inspired local AI assistant. Answer directly and precisely, with a hint of wisdom and playfulness."

class ModelEngine:
    def __init__(self):
        self.HailoNPU = VDevice()
        self.ryuuModel = LLM(vdevice=self.HailoNPU, model_path="models/Qwen2.5-1.5B-Instruct.hef")

    def chatPrompt(self, inputPrompt):
        context = ryuuRetrieve(inputPrompt)
        GenInput = [
             {"role": "system", "content": SYSTEM_PROMPT},
             {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {inputPrompt}" if context else inputPrompt}
        ]
        ModelResponse = ""
        with self.ryuuModel.generate(GenInput, max_generated_tokens=500) as tokenGen:
            for token in tokenGen:
                ModelResponse += token
        return ModelResponse.strip().replace("<|im_end|>","").strip()      
