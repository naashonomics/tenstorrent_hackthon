# tenstorrent_hackthon

## Hackathon Documentation Summary: Implementing Bark with Tenstorrent Hardware and PyBuda
### Overview
In this hackathon project, we implemented the Bark model using Tenstorrent hardware and the PyBuda framework. Bark, developed by Suno, is a cutting-edge transformer-based text-to-audio model capable of generating highly realistic, multilingual speech, as well as other audio outputs such as music, background noise, and simple sound effects. The model is also adept at producing nonverbal communications, including laughing, sighing, and crying.
### Key Features
- **Multilingual Speech Generation:** Bark can synthesize natural-sounding speech in multiple languages, making it versatile for various applications.
- **Diverse Audio Outputs:** Beyond speech, the model can generate music, background noise, and sound effects, enhancing its utility in multimedia projects.
- **Nonverbal Communication:** The model can express emotions and reactions through nonverbal cues, adding a layer of realism to the generated audio.
### Implementation Details
- **Hardware:** The project leveraged Tenstorrent hardware to accelerate the model's computations, enabling efficient and fast audio generation.
- **Framework:** PyBuda was used as the primary framework for model deployment and execution, offering a seamless interface for integrating the Bark model.
### Conclusion
This hackathon project demonstrates the potential of transformer-based models in text-to-audio conversion. By leveraging state-of-the-art hardware and software tools, we successfully showcased the capabilities of the Bark model, opening up new possibilities for realistic and expressive audio generation in various applications.


**Pre exeuction:**
```
pip install streamlit scipy transformers
```

**What we are building ?**

![image](https://github.com/user-attachments/assets/4043b12c-cc0a-40fd-88a5-b800ce588cdd)


**Does did we confirm it works on Grayscale and Wormhole?**
![image](https://github.com/user-attachments/assets/b88772a7-c353-477e-a87e-c281af947a97)
![image](https://github.com/user-attachments/assets/ba6b1091-9bb0-4880-8efa-8d8919f82996)
![image](https://github.com/user-attachments/assets/0c8c7921-939e-4cb9-b621-d6e1dd4ea3a0)


**How to run the code?**

```
streamlit run cpu_buda_text2voice_converter.py
```

```
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: <url>
  Network URL: <url>
  External URL: <url>
```
[![Watch the video]([https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg](https://github.com/user-attachments/assets/0c8c7921-939e-4cb9-b621-d6e1dd4ea3a0))](https://www.youtube.com/watch?v=xTSIQGpY7jc)

**Project 2** : In this hackathon project, we implemented a Visual Question Answering (VQA) system. The VQA system combines several advanced transformer-based models to analyze images, generate captions, and answer questions based on those captions. The models include CLIP, VisionEncoderDecoder, and Roberta, which work together to provide a seamless VQA experience. Our implementation also features an interface built with Gradio for easy interaction.

**Key Features**

**Image Captioning**:

The system uses the CLIP model to process images and generate captions with the VisionEncoderDecoder model.

**Question Answering**: 

Based on the generated captions, the Roberta model answers questions, supporting both text and audio inputs for questions.

**Text-to-Speech Conversion**: 

The answers are converted to audio using gTTS, providing an auditory response for users.

**Implementation Details**

**Hardware**:

Initially, we attempted to leverage Tenstorrent hardware to accelerate the models' computations using PyBUDA. However, due to compatibility issues, we reverted to using standard hardware (CPU) without PyBUDA.

**Framework**: 

The models were deployed and executed using standard PyTorch and Transformers libraries without the PyBUDA framework.

**User Interface**: 

The Gradio interface allows users to upload images, input questions (either via text or audio), and receive answers in both text and audio formats.
Challenges and Solutions

**PyBUDA** 

Compatibility Issues: During the implementation, we encountered compatibility issues with CUDA and the PyBUDA framework, resulting in errors when attempting to run the models on Tenstorrent hardware. The specific error encountered was related to the ushort format, indicating that the audio data dimensions were not correctly handled.


**Solution**: Due to these compatibility issues, we decided to run the models without PyBUDA, using standard hardware for the computations. This allowed us to successfully implement the VQA system without encountering the data handling issues.

![image](https://github.com/user-attachments/assets/4fc27f9d-95f3-4bef-9b87-8ac09aef5da6)
![image](https://github.com/user-attachments/assets/5f871962-94f5-4602-b542-876d2e276b0b)


https://github.com/naashonomics/tenstorrent_hackthon/blob/main/visual_qa.ipynb
