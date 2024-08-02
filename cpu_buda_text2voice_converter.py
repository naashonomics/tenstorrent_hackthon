import os
import torch
import numpy as np
import scipy.io.wavfile
from transformers import AutoProcessor, AutoModel, AutoTokenizer
from pybuda.transformers.pipeline import pipeline as pybuda_pipeline
import streamlit as st
import pybuda
# Set environment variables for PyBUDA
os.environ["TT_BACKEND_TIMEOUT"] = '0'

# Function to process text to audio using PyBUDA
def text_to_audio_pybuda(prompt):
    # Set PyBUDA configurations
    compiler_cfg = pybuda.config._get_global_compiler_config()
    compiler_cfg.default_df_override = pybuda.DataFormat.Float16_b
    compiler_cfg.enable_auto_fusing = True
    compiler_cfg.balancer_policy = "Ribbon"

    # Initialize models
    processor = AutoProcessor.from_pretrained("suno/bark-small")
    model = AutoModel.from_pretrained("suno/bark-small")
    tokenizer = AutoTokenizer.from_pretrained("suno/bark-small")

    # Initialize the PyBUDA pipeline
    batch_size = 1
    asr_pipeline = pybuda_pipeline(
        "text-to-audio",
        model=model,
        tokenizer=processor.tokenizer,
        batch_size=batch_size,
    )

    prompts = [prompt] * batch_size
    speech_values = asr_pipeline(prompts)

    # Extract the generated audio
    audio_data = speech_values[0]['audio']
    sampling_rate = model.generation_config.sample_rate

    # Transpose audio data if needed
    if audio_data.ndim == 2:
        audio_data = audio_data.T

    # Ensure audio data is within valid range for WAV file format
    if audio_data.dtype != "int16":
        audio_data = (audio_data * 32767).astype(np.int16)

    # Save the audio to a file
    scipy.io.wavfile.write("bark_out.wav", rate=sampling_rate, data=audio_data)

    return "bark_out.wav"

# Function to process text to audio using CPU
def text_to_audio_cpu(prompt):
    processor = AutoProcessor.from_pretrained("suno/bark-small")
    model = AutoModel.from_pretrained("suno/bark-small")

    inputs = processor(
        text=[prompt],
        return_tensors="pt",
    )

    with torch.no_grad():
        speech_values = model.generate(**inputs, do_sample=True)
    sampling_rate = model.generation_config.sample_rate
    audio_data = speech_values.cpu().numpy().squeeze()

    # Transpose audio data if needed
    if audio_data.ndim == 2:
        audio_data = audio_data.T

    # Ensure audio data is within valid range for WAV file format
    if audio_data.dtype != "int16":
        audio_data = (audio_data * 32767).astype(np.int16)

    # Save the audio to a file
    scipy.io.wavfile.write("bark_out.wav", rate=sampling_rate, data=audio_data)

    return "bark_out.wav"

# Function to translate the prompt text
def translate_text(prompt):
    # Placeholder translation function
    translated_text = f"Translated text: {prompt}"
    return translated_text

# Streamlit UI
st.title("Text-to-Audio Generation with Translation")

# Option to select CPU or PyBUDA
st.sidebar.header("Configuration")
run_on = st.sidebar.radio("Run on", ["CPU", "PyBUDA"])

prompt = st.text_area("Enter your prompt here:", value="Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.")

if st.button("Generate Audio"):
    if prompt:
        translated_text = translate_text(prompt)
        
        if run_on == "PyBUDA":
            try:
                audio_path = text_to_audio_pybuda(prompt)
            except Exception as e:
                st.error(f"Error running on PyBUDA: {e}")
                st.stop()
        else:
            try:
                audio_path = text_to_audio_cpu(prompt)
            except Exception as e:
                st.error(f"Error running on CPU: {e}")
                st.stop()

        # Display the translated text
        st.text_area("Translated Text", translated_text, height=100)

        # Play the audio in the Streamlit app
        st.audio(audio_path)

        st.success("Audio generation complete!")
    else:
        st.error("Please enter a prompt to generate audio.")
