bl_info = {
    "name": "Hybrid Image Character Importer",
    "author": "Juhapekka Ollikainen",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Tools",
    "description": "Imports and visualizes hybrid story characters from open data API",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}

import bpy
import requests

# ------------------------------------------------------------------------
#    Operator: Fetch and Import Hybrid Character
# ------------------------------------------------------------------------

class HYBRID_OT_ImportCharacter(bpy.types.Operator):
    """Fetch a hybrid character from the Hybrid Image API and create a placeholder object"""
    bl_idname = "hybrid.import_character"
    bl_label = "Import Hybrid Character"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        api_url = "https://api.hybridimage.org/v1/characters/random"
        self.report({'INFO'}, f"Fetching character from {api_url} ...")

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            name = data.get("name", "Hybrid_Character")
            description = data.get("description", "No description available.")
            self.report({'INFO'}, f"Imported: {name}")

            # Create a simple placeholder mesh (UV sphere)
            bpy.ops.mesh.primitive_uv_sphere_add()
            obj = bpy.context.active_object
            obj.name = name

            # Add custom metadata
            obj["description"] = description

            # Print to console
            print(f"Character Imported: {name}")
            print(f"Description: {description}")

        except Exception as e:
            self.report({'ERROR'}, f"Failed to fetch data: {e}")

        return {'FINISHED'}


# ------------------------------------------------------------------------
#    UI Panel in Sidebar
# ------------------------------------------------------------------------

class HYBRID_PT_MainPanel(bpy.types.Panel):
    bl_label = "Hybrid Image Platform"
    bl_idname = "HYBRID_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'StoryChar'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hybrid Image Character Importer")
        layout.operator("hybrid.import_character", icon='OUTLINER_OB_MESH')


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    HYBRID_OT_ImportCharacter,
    HYBRID_PT_MainPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
✅ How to use in Blender:

Save this file as storychar_importer.py

Open Blender → Edit → Preferences → Add-ons → Install…

Select the file and enable the add-on

In the 3D View, open the Sidebar (N key) → StoryChar tab

Click Import Hybrid Character to fetch and visualize a random entity

Would you like me to add a small local test mode (so it works even without an internet connection, using a sample JSON response)?






Sinä sanoit:
yes pls add


ChatGPT sanoi:
Perfect — here’s the updated storychar_importer.py Blender add-on with an offline test mode that generates sample data if the API is unreachable.

This way, you can demo or prototype the tool even without an internet connection or a live API.

python
Kopioi koodi
bl_info = {
    "name": "Hybrid Image Character Importer",
    "author": "Juhapekka Ollikainen",
    "version": (0, 2),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > StoryChar",
    "description": "Imports and visualizes hybrid story characters from open data API (with offline test mode)",
    "category": "Import-Export",
}

import bpy
import requests
import random

# ------------------------------------------------------------------------
#    Offline sample data (for testing without API)
# ------------------------------------------------------------------------

SAMPLE_CHARACTERS = [
    {
        "name": "Spirit-Pike Warrior",
        "description": "A mythic hero merging human intellect and fish spirit strength.",
    },
    {
        "name": "Iron Owl Shaman",
        "description": "A hybrid of nocturnal wisdom and metallic resilience.",
    },
    {
        "name": "Cloud Elk Guardian",
        "description": "A sky-traveling protector blending natural grace with stormy energy.",
    },
    {
        "name": "Lynx Oracle",
        "description": "A seer whose hybrid essence merges feline stealth and human intuition.",
    },
]

# ------------------------------------------------------------------------
#    Operator: Fetch and Import Hybrid Character
# ------------------------------------------------------------------------

class HYBRID_OT_ImportCharacter(bpy.types.Operator):
    """Fetch a hybrid character from the Hybrid Image API or use offline mode"""
    bl_idname = "hybrid.import_character"
    bl_label = "Import Hybrid Character"
    bl_options = {'REGISTER', 'UNDO'}

    use_offline: bpy.props.BoolProperty(
        name="Offline Mode",
        description="Use local sample data instead of API request",
        default=False,
    )

    def fetch_character(self):
        """Try fetching from API, fallback to local sample"""
        api_url = "https://api.hybridimage.org/v1/characters/random"
        if self.use_offline:
            return random.choice(SAMPLE_CHARACTERS)

        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[HybridImage] API fetch failed: {e}")
            return random.choice(SAMPLE_CHARACTERS)

    def execute(self, context):
        data = self.fetch_character()
        name = data.get("name", "Hybrid_Character")
        description = data.get("description", "No description available.")

        # Create a simple placeholder mesh (UV sphere)
        bpy.ops.mesh.primitive_uv_sphere_add()
        obj = bpy.context.active_object
        obj.name = name

        # Store metadata
        obj["description"] = description

        self.report({'INFO'}, f"Imported character: {name}")
        print(f"\n--- Hybrid Image Import ---\nName: {name}\nDescription: {description}\n")

        return {'FINISHED'}


# ------------------------------------------------------------------------
#    UI Panel
# ------------------------------------------------------------------------

class HYBRID_PT_MainPanel(bpy.types.Panel):
    bl_label = "Hybrid Image Platform"
    bl_idname = "HYBRID_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'StoryChar'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hybrid Image Character Importer")
        layout.operator("hybrid.import_character", icon='OUTLINER_OB_MESH')


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    HYBRID_OT_ImportCharacter,
    HYBRID_PT_MainPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    print("Hybrid Image Character Importer registered.")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("Hybrid Image Character Importer unregistered.")

if __name__ == "__main__":
    register()
🧭 Usage in Blender
Save this as storychar_importer.py

In Blender → Edit → Preferences → Add-ons → Install…, select this file

Enable the add-on

Open Sidebar (N key) → StoryChar tab → click Import Hybrid Character

If you’re offline or the API is unavailable, a random local hybrid character will be used automatically.
