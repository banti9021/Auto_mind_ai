import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class LocalLLM:
    """
    A class to manage and run a local language model (LLM).
    """

    def __init__(self, model_name_or_path: str, device: str = None):
        """
        Initialize the LocalLLM class.

        Args:
            model_name_or_path (str): Path to the model or model name from Hugging Face.
            device (str, optional): Device to run the model on ('cpu' or 'cuda'). Defaults to auto-detection.
        """
        self.model_name_or_path = model_name_or_path
        self.device = device if device else ('cuda' if torch.cuda.is_available() else 'cpu')

        # Load the model and tokenizer
        self.tokenizer = None
        self.model = None
        self._load_model()

    def _load_model(self):
        """
        Load the model and tokenizer.
        """
        try:
            print(f"Loading model from {self.model_name_or_path} on {self.device}...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name_or_path)
            self.model.to(self.device)
            print("Model loaded successfully.")
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {e}")

    def generate(self, prompt: str, max_length: int = 50, temperature: float = 1.0, top_k: int = 50):
        """
        Generate text from the model based on a given prompt.

        Args:
            prompt (str): Input prompt for the model.
            max_length (int, optional): Maximum length of the generated text. Defaults to 50.
            temperature (float, optional): Sampling temperature. Defaults to 1.0.
            top_k (int, optional): Top-k sampling. Defaults to 50.

        Returns:
            str: Generated text.
        """
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(
                inputs["input_ids"],
                max_length=max_length,
                temperature=temperature,
                top_k=top_k,
                pad_token_id=self.tokenizer.eos_token_id
            )
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            raise RuntimeError(f"Failed to generate text: {e}")

    def save_model(self, save_path: str):
        """
        Save the model and tokenizer to a specified path.

        Args:
            save_path (str): Path to save the model and tokenizer.
        """
        try:
            os.makedirs(save_path, exist_ok=True)
            self.tokenizer.save_pretrained(save_path)
            self.model.save_pretrained(save_path)
            print(f"Model saved to {save_path}.")
        except Exception as e:
            raise RuntimeError(f"Failed to save model: {e}")

if __name__ == "__main__":
    # Example usage
    model_path = "gpt2"  # Replace with your local model path or Hugging Face model name
    llm = LocalLLM(model_path)

    prompt = "Once upon a time"
    print("Generating text...")
    generated_text = llm.generate(prompt, max_length=100)
    print("Generated text:", generated_text)

    # Save the model (optional)
    save_directory = "./saved_model"
    llm.save_model(save_directory)