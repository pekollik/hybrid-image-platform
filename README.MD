
# Hybrid Image Platform  
### Open Story Data API & Blender Add-on for Hybrid Character Generation  
**Author:** Juhapekka Ollikainen  
**Reference:** *Hybrid Image of Multiple Fantastical Characters*, Proceedings, Paris France, 2022, p. 262–265  

---

## 1. Overview

The **Hybrid Image Platform** is an open-source research and creative-coding project for generating hybrid fantastical characters from open story data.  
It bridges creative writing, AI-assisted character generation, and 3D modelling.  

This repository provides:  
- an **Open Data API** specification for narrative and character data;  
- a **Blender add-on skeleton** (`storychar_importer.py`) for 3D visualization and manipulation;  
- documentation for developers and research collaborators.  

The platform expands on the ideas presented in the paper *Hybrid Image of Multiple Fantastical Characters*, exploring how open public-domain story corpora can inspire new hybrid entities in games, comics, and digital art.  

---

## 2. Phase I – Open Data API (Concept and Specification)

### 🎯 Goal  
Provide an accessible REST API for retrieving and remixing open narrative data (e.g., mythological characters, motifs, and story fragments).  

### 🔌 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/api/v1/characters` | GET | Returns a list of all available hybrid characters |
| `/api/v1/characters/{id}` | GET | Returns data for a single hybrid character |
| `/api/v1/generate` | POST | Generates a new hybrid character from text corpus inputs |
| `/api/v1/corpus` | GET | Returns metadata about available story corpora (e.g., Kalevala, folk tales) |

### 🧩 Data Model (JSON)

```json
{
  "id": "suomuhauki_001",
  "name": "Hybrid Suomuhauki",
  "sources": ["Kalevala", "Finnish folklore"],
  "traits": {
    "human": "heroic figure",
    "animal": "pike",
    "spiritual": "lake spirit"
  },
  "description": "A merged entity combining human bravery and aquatic mysticism.",
  "media": {
    "image": "url_to_concept_art.png",
    "3d_model": "url_to_blend_file.blend"
  }
}
Example Request
bash
Kopioi koodi
curl -X POST https://api.hybridimage.org/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{"sources": ["Kalevala"], "traits": ["human","animal","spirit"]}'
Example Response
json
Kopioi koodi
{
  "id": "hybrid_12345",
  "name": "Spirit-Pike Warrior",
  "description": "A mythic hero merging human intellect and fish spirit strength."
}
3. Phase II – Blender Add-on (Prototype Skeleton)
The second phase focuses on 3D visualization and creative prototyping through Blender’s Python API.

File: storychar_importer.py
python
Kopioi koodi
bl_info = {
    "name": "Hybrid Image Character Importer",
    "author": "Juhapekka Ollikainen",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Tools",
    "description": "Imports and visualizes hybrid story characters from open data API",
    "category": "Import-Export",
}

import bpy
import requests

class HYBRID_OT_ImportCharacter(bpy.types.Operator):
    bl_idname = "hybrid.import_character"
    bl_label = "Import Hybrid Character"

    def execute(self, context):
        url = "https://api.hybridimage.org/api/v1/characters/random"
        response = requests.get(url)
        data = response.json()

        # Create simple placeholder geometry
        bpy.ops.mesh.primitive_uv_sphere_add()
        obj = bpy.context.active_object
        obj.name = data.get("name", "Hybrid_Character")

        self.report({'INFO'}, f"Imported: {obj.name}")
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(HYBRID_OT_ImportCharacter.bl_idname)

def register():
    bpy.utils.register_class(HYBRID_OT_ImportCharacter)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(HYBRID_OT_ImportCharacter)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()
This script sets up a basic interface for connecting to the open data API and generating placeholder geometry in Blender for prototyping.

4. Collaborative Development
To whom:

Game designers writing video- or board-game characters

3D artists and modelers seeking hybrid concept inspiration

Computational creativity researchers

Next steps:

Conduct workshops with creative writers and game developers.

Extend API to include story fragments, emotional profiles, and randomized hybrid traits.

Integrate with Blender’s geometry-nodes system for parametric character generation.

5. Installation (GitHub Repository)
Go to https://github.com → + New Repository

Name it hybrid-image-platform

Set to Public and do not auto-add a README

Upload manually:

README.md

storychar_importer.py

docs/hybrid_image_specification.pdf (optional)

Click Commit changes

Verify that README.md appears as the main page

6. Contributing
Contributions are welcome.

Fork the repository

Create a new branch (feature/your-idea)

Commit your changes

Submit a Pull Request with a short summary of your contribution

Please keep comments and commit messages concise and technical.

7. License
All materials (text, code, and media) are released under Creative Commons BY 4.0
→ You may remix, adapt, and build upon this work, with attribution to the author.

Citation:
Ollikainen, J. (2022). Hybrid Image of Multiple Fantastical Characters. Proceedings of the Conference on Creative Coding and Computational Creativity, Paris, France.
