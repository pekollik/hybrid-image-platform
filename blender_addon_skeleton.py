# Hybrid Image Platform — README

### Overview
This repository documents the *Hybrid Image Platform*, a two-phase research and development initiative based on the paper *Hybrid Image of Multiple Fantastical Characters* (Juhapekka Ollikainen, 2022, International Conference on Computational Creativity, Paris).

The project combines artistic research and technical prototyping to explore new ways of generating hybrid story characters from open public-domain materials. It bridges cultural archives and computational creativity, producing an open API for story data and a Blender add-on for visualization and 3D prototyping.

---

## 🧩 Phase 1 — Open Data API

### Base URL
```
https://api.hybridimage.org/v1/
```

### Key Endpoints
- `GET /characters` — List available hybrid characters.  
- `GET /characters/{id}` — Retrieve detailed metadata and 3D asset link.  
- `POST /characters` — Submit new hybrid character entries.  
- `GET /stories/random` — Fetch a random hybrid story fragment.

### Example Response
```json
{
  "id": "suomuhauki",
  "origin": "Kalevala",
  "traits": ["human", "fish", "spiritual"],
  "description": "Hybrid of man and pike from Finnish myth.",
  "3d_asset_url": "https://assets.hybridimage.org/models/suomuhauki.glb"
}
```

### Example Python Call
```python
import requests
url = "https://api.hybridimage.org/v1/characters/suomuhauki"
data = requests.get(url).json()
print(data['description'])
```

---

## 🎨 Phase 2 — Blender Add-on: *StoryChar Importer*

A Blender extension that connects directly to the Hybrid Image API to fetch, visualize, and remix open hybrid characters.

### Features
- API connection and metadata retrieval  
- Character import via GLB/GLTF  
- Background threaded downloads  
- Simple UI panel under *View3D → Sidebar → StoryChar*

### Usage
1. Install `storychar_importer.py` in Blender’s Add-ons menu.  
2. Set API Base and optional key.  
3. Fetch metadata and import model assets.  
4. Extend with Python scripting for creative recombination.

---

## 🧠 Research and Collaboration
The project extends the ideas from *Hybrid Image of Multiple Fantastical Characters* (Ollikainen, 2022), which proposed using computational creativity to merge mythological and fictional archetypes into new, generative characters. The platform aims to enable creative coding practices where narrative fragments and 3D models coexist as open cultural resources.

### Planned Development
- Procedural hybridization endpoint (`/characters/hybridize`)  
- OAuth2 authentication for creative contributors  
- Blender-side parameters for morphological and textual traits  
- Workshop testing with writers, coders, and game designers

---

## 🚀 Installation
1. Clone this repository:
```bash
git clone https://github.com/<username>/hybrid-image-platform.git
```
2. Open Blender → Preferences → Add-ons → Install...
3. Select `storychar_importer.py` and enable it.
4. Open the *StoryChar* tab in the Sidebar to start fetching and importing characters.

---

## 🤝 Contributing
We welcome contributions from researchers, coders, and artists:  
- Submit bug reports and feature requests via GitHub Issues.  
- Fork the repository to experiment with new API endpoints or Blender features.  
- Ensure Python scripts follow PEP8 style and include documentation.  
- Credit original story sources when adding new character data.

---

## 📜 License
This project is licensed under the MIT License for code and Creative Commons Attribution 4.0 International (CC BY 4.0) for documentation and story data contributions.

---

## 📚 References
- Ollikainen, J. (2022). *Hybrid Image of Multiple Fantastical Characters.* International Conference on Computational Creativity, Paris.  
- Lehman, J., Risi, S., & Clune, J. (2016). *Creative generation of 3D objects with deep learning and innovation engines.* ICCC.  
- Boden, M. (2004). *The Creative Mind: Myths and Mechanisms.* Routledge.

---

**Author:** Juhapekka Ollikainen  
**Contact:** pekollik@gmail.com  
**Keywords:** creative coding, computational creativity, creative writing, Python, Blender, hybrid characters
