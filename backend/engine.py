from hailo_platform import VDevice
from hailo_platform.genai import LLM

class ModelEngine:
    def __init__(self):
        self.HailoNPU = VDevice()
        self.ryuuModel = LLM(vdevice=self.HailoNPU, hef_path="models/Qwen2.5-1.5B-Instruct.hef")

    def chatPrompt(self, inputPrompt):
        ModelResponse = self.ryuuModel.generate(inputPrompt)
        return ModelResponse      