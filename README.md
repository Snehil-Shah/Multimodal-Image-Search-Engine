---
title: Multimodal Image Search Engine
emoji: 🔍
colorFrom: yellow
colorTo: yellow
sdk: gradio
sdk_version: 4.13.0
app_file: app.py
pinned: false
license: mit
---

<p align="center">
  <h1 align="center">Multi-Modal Image Search Engine</h1>
  <p align="center">
    A Semantic Search Engine that understands the Content & Context of your Queries. 
    <br>
    Use Multi-Modal inputs like Text-Image or a Reverse Image Search to Query a Vector Database of over 15k Images. <a href="https://huggingface.co/spaces/Snehil-Shah/Multimodal-Image-Search-Engine">Try it Out!</a>
    <br><br>
    <img src="https://github.com/Snehil-Shah/Multimodal-Image-Search-Engine/blob/main/assets/demo.gif?raw=true">
  </p>
</p>

<h3>• About The Project</h3>

At its core, the Search Engine is built upon the concept of **Vector Similarity Search**.
All the Images are encoded into vector embeddings based on their semantic meaning using a Transformer Model, which are then stored in a vector space.
When searched with a query, it returns the nearest neighbors to the input query which are the relevant search results.

<p align="center"><img src="https://raw.githubusercontent.com/Snehil-Shah/Multimodal-Image-Search-Engine/main/assets/encoding_flow.png"></p>

We use the Contrastive Language-Image Pre-Training (CLIP) Model by OpenAI which is a Pre-trained Multi-Modal Vision Transformer that can semantically encode Words, Sentences & Images into a 512 Dimensional Vector. This Vector encapsulates the meaning & context of the entity into a *Mathematically Measurable* format.

<p align="center"><p align="center"><img src="https://raw.githubusercontent.com/Snehil-Shah/Multimodal-Image-Search-Engine/main/assets/Visualization.png" width=1000></p>
<p align="center"><i>2-D Visualization of 500 Images in a 512-D Vector Space</i></p></p>

The Images are stored as vector embeddings in a Qdrant Collection which is a Vector Database. The Search Term is encoded and run as a query to Qdrant, which returns the Nearest Neighbors based on their Cosine-Similarity to the Search Query.

<p align="center"><img src="https://raw.githubusercontent.com/Snehil-Shah/Multimodal-Image-Search-Engine/main/assets/retrieval_flow.png"></p>

**The Dataset**: All images are sourced from the [Open Images Dataset](https://github.com/cvdfoundation/open-images-dataset) by Common Visual Data Foundation.

<h3>• Technologies Used</h3>

- Python
- Jupyter Notebooks
- Qdrant - Vector Database
- Sentence-Transformers - Library
- CLIP by OpenAI - ViT Model
- Gradio - UI
- HuggingFace Spaces - Deployment


