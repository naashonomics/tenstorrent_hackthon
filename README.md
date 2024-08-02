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


