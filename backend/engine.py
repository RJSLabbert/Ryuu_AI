from hailo_platform import VDevice
from hailo_platform.genai import LLM

class ModelEngine:
    def __init__(self):
        self.HailoNPU = VDevice()
        self.ryuuModel = LLM(vdevice=self.HailoNPU, model_path="models/Qwen2.5-1.5B-Instruct.hef")

    def chatPrompt(self, inputPrompt):
        userInput = [{"role": "user", "content": inputPrompt}]
        ModelResponse = ""
        with self.ryuuModel.generate(userInput, max_generated_tokens=500) as tokenGen:
            for token in tokenGen:
                ModelResponse += token
        return ModelResponse      