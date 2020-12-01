__version__ = '0.0.7'
from ecco.lm import LM, MockGPT, MockGPTTokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM

def from_pretrained(hf_model_id, activations=False, attention=False):
    if hf_model_id == "mockGPT":
        tokenizer = MockGPTTokenizer()
        model = MockGPT()
    else:
        tokenizer = AutoTokenizer.from_pretrained(hf_model_id)
        model = AutoModelForCausalLM.from_pretrained(hf_model_id,
                                                     output_hidden_states=True,
                                                     output_attentions=attention)
    if activations:
        return LM(model, tokenizer, collect_activations_flag=True)
    else:
        return LM(model, tokenizer)
